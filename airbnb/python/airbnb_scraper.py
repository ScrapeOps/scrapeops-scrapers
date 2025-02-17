import os
import csv
import requests
import json
import logging
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import concurrent.futures
from dataclasses import dataclass, field, fields, asdict

API_KEY = ""

with open("config.json", "r") as config_file:
    config = json.load(config_file)
    API_KEY = config["api_key"]



def get_scrapeops_url(url, location="us"):
    payload = {
        "api_key": API_KEY,
        "url": url,
        "country": location,
        "wait": 5000,
        }
    proxy_url = "https://proxy.scrapeops.io/v1/?" + urlencode(payload)
    return proxy_url


## Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



@dataclass
class SearchData:
    name: str = ""
    description: str = ""
    dates: str = ""
    price: str = ""
    url: str = ""

    def __post_init__(self):
        self.check_string_fields()
        
    def check_string_fields(self):
        for field in fields(self):
            # Check string fields
            if isinstance(getattr(self, field.name), str):
                # If empty set default text
                if getattr(self, field.name) == "":
                    setattr(self, field.name, f"No {field.name}")
                    continue
                # Strip any trailing spaces, etc.
                value = getattr(self, field.name)
                setattr(self, field.name, value.strip())

@dataclass
class ReviewData:
    name: str = ""
    stars: int = 0
    review: str = ""


    def __post_init__(self):
        self.check_string_fields()
        
    def check_string_fields(self):
        for field in fields(self):
            # Check string fields
            if isinstance(getattr(self, field.name), str):
                # If empty set default text
                if getattr(self, field.name) == "":
                    setattr(self, field.name, f"No {field.name}")
                    continue
                # Strip any trailing spaces, etc.
                value = getattr(self, field.name)
                setattr(self, field.name, value.strip())


class DataPipeline:
    
    def __init__(self, csv_filename="", storage_queue_limit=50):
        self.names_seen = []
        self.storage_queue = []
        self.storage_queue_limit = storage_queue_limit
        self.csv_filename = csv_filename
        self.csv_file_open = False
    
    def save_to_csv(self):
        self.csv_file_open = True
        data_to_save = []
        data_to_save.extend(self.storage_queue)
        self.storage_queue.clear()
        if not data_to_save:
            return

        keys = [field.name for field in fields(data_to_save[0])]
        file_exists = os.path.isfile(self.csv_filename) and os.path.getsize(self.csv_filename) > 0
        with open(self.csv_filename, mode="a", newline="", encoding="utf-8") as output_file:
            writer = csv.DictWriter(output_file, fieldnames=keys)

            if not file_exists:
                writer.writeheader()

            for item in data_to_save:
                writer.writerow(asdict(item))

        self.csv_file_open = False
                    
    def is_duplicate(self, input_data):
        if input_data.name in self.names_seen:
            logger.warning(f"Duplicate item found: {input_data.name}. Item dropped.")
            return True
        self.names_seen.append(input_data.name)
        return False
            
    def add_data(self, scraped_data):
        if self.is_duplicate(scraped_data) == False:
            self.storage_queue.append(scraped_data)
            if len(self.storage_queue) >= self.storage_queue_limit and self.csv_file_open == False:
                self.save_to_csv()
                       
    def close_pipeline(self):
        if self.csv_file_open:
            time.sleep(3)
        if len(self.storage_queue) > 0:
            self.save_to_csv()

def find_pagination_urls(keyword, location, pages=4, retries=3):
    formatted_keyword = keyword.replace(", ", "--").replace(" ", "-")
    url = f"https://www.airbnb.com/s/{formatted_keyword}/homes"
    tries = 0
    success = False
    
    while tries <= retries and not success:
        try:
            scrapeops_proxy_url = get_scrapeops_url(url, location=location)
            response = requests.get(scrapeops_proxy_url)
            logger.info(f"Recieved [{response.status_code}] from: {url}")
            if response.status_code != 200:
                raise Exception(f"Failed request, Status Code {response.status_code}")            

            soup = BeautifulSoup(response.text, "html.parser")
            pagination_bar = soup.select_one("nav[aria-label='Search results pagination']")
            a_tags = pagination_bar.find_all("a")
            links = []
            links.append(url)
            acceptable_pages = ["1", "2", "3", "4"]
            for a in a_tags:
                if a.text in acceptable_pages and len(links) < pages:
                    href = a.get("href")
                    link = f"https://www.airbnb.com{href}"
                    links.append(link)
            success = True
            return links

        except Exception as e:
            logger.warning(f"Failed to fetch page list for {url} tries left {retries - tries}")
            logger.warning(f"Exception: {e}")
            tries += 1
    if not success:
        raise Exception("Failed to find pagination, max retries exceeded!")
    



def scrape_search_results(url, location, data_pipeline=None, retries=3):
    tries = 0
    success = False
    
    while tries <= retries and not success:
        try:
            scrapeops_proxy_url = get_scrapeops_url(url, location=location)
            response = requests.get(scrapeops_proxy_url)
            logger.info(f"Recieved [{response.status_code}] from: {url}")
            if response.status_code != 200:
                raise Exception(f"Failed request, Status Code {response.status_code}")
                
            soup = BeautifulSoup(response.text, "html.parser")            
            div_cards = soup.select("div[data-testid='card-container']")

            
            for div_card in div_cards:
                descripition = div_card.select_one("div[data-testid='listing-card-title']").text
                subtitle_array = div_card.select("div[data-testid='listing-card-subtitle']")

                name = subtitle_array[0].text
                dates = subtitle_array[-1].text

                price = div_card.select_one("span div span").text
                href = div_card.find("a").get("href")
                link = f"https://www.airbnb.com{href}"
                
                search_data = SearchData(
                    name=name,
                    description=descripition,
                    dates=dates,
                    price=price,
                    url=link
                )
                data_pipeline.add_data(search_data)
                
            logger.info(f"Successfully parsed data from: {url}")
            success = True       
                    
        except Exception as e:
            logger.error(f"An error occurred while processing page {url}: {e}")
            logger.info(f"Retrying request for page: {url}, retries left {retries-tries}")
            tries +=1

    if not success:
        raise Exception(f"Max Retries exceeded: {retries}")




def start_scrape(url_list, location, data_pipeline=None, max_threads=5, retries=3):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(
            scrape_search_results,
            url_list,
            [location] * len(url_list),
            [data_pipeline] * len(url_list),
            [retries] * len(url_list)
        )


def process_listing(row, location, retries=3):
    url = row["url"]
    tries = 0
    success = False

    while tries <= retries and not success:
        response = requests.get(get_scrapeops_url(url, location=location))
        try:
            if response.status_code == 200:
                logger.info(f"Status: {response.status_code}")

                soup = BeautifulSoup(response.text, "html.parser")
                review_cards = soup.select("div[role='listitem']")
                review_pipeline = DataPipeline(csv_filename=f"{row['name'].replace(' ', '-').replace('/', '-')}.csv")

                for review_card in review_cards:
                    name = review_card.find("h3").text
                    stars = len(review_card.find_all("svg"))
                    spans = review_card.find_all("span")
                    review = spans[-1].text

                    review_data = ReviewData(
                        name=name,
                        stars=stars,
                        review=review
                    )
                    review_pipeline.add_data(review_data)

                review_pipeline.close_pipeline()
                success = True

            else:
                logger.warning(f"Failed Response: {response.status_code}")
                raise Exception(f"Failed Request, status code: {response.status_code}")
        except Exception as e:
            logger.error(f"Exception thrown: {e}")
            logger.warning(f"Failed to process page: {row['url']}")
            logger.warning(f"Retries left: {retries-tries}")
            tries += 1
    if not success:
        raise Exception(f"Max Retries exceeded: {retries}")
    else:
        logger.info(f"Successfully parsed: {row['url']}")


def process_results(csv_file, location, max_threads=5, retries=3):
    logger.info(f"processing {csv_file}")
    with open(csv_file, newline="") as file:
        reader = list(csv.DictReader(file))

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
            executor.map(
                process_listing,
                reader,
                [location] * len(reader),
                [retries] * len(reader)
            )

if __name__ == "__main__":

    MAX_RETRIES = 3
    MAX_THREADS = 5
    PAGES = 4
    LOCATION = "us"

    logger.info(f"Crawl starting...")

    ## INPUT ---> List of keywords to scrape
    keyword_list = ["Myrtle Beach, South Carolina, United States"]
    aggregate_files = []

    ## Job Processes
    for keyword in keyword_list:
        filename = keyword.replace(", ", "-").replace(" ", "-")

        page_urls = find_pagination_urls(keyword, LOCATION, pages=PAGES, retries=MAX_RETRIES)
        
        crawl_pipeline = DataPipeline(csv_filename=f"{filename}.csv")
        start_scrape(page_urls, LOCATION, data_pipeline=crawl_pipeline, max_threads=MAX_THREADS, retries=MAX_RETRIES)
        crawl_pipeline.close_pipeline()
        aggregate_files.append(f"{filename}.csv")
    logger.info(f"Crawl complete.")

    for file in aggregate_files:
        process_results(file, LOCATION, max_threads=MAX_THREADS, retries=MAX_RETRIES)