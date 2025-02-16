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
        "country": "us",
        }
    proxy_url = "https://proxy.scrapeops.io/v1/?" + urlencode(payload)
    return proxy_url


## Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



@dataclass
class SearchData:
    name: str = ""
    stars: float = 0
    g2_url: str = ""
    description: str = ""

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
    date: str = ""
    job_title: str = ""
    rating: float = 0
    full_review: str = ""
    review_source: str = ""
    validated: bool = False
    incentivized: bool = False


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



def scrape_search_results(keyword, location, page_number, data_pipeline=None, retries=3):
    formatted_keyword = keyword.replace(" ", "+")
    url = f"https://www.g2.com/search?page={page_number+1}&query={formatted_keyword}"
    tries = 0
    success = False
    
    while tries <= retries and not success:
        try:
            scrapeops_proxy_url = get_scrapeops_url(url, location=location)
            response = requests.get(scrapeops_proxy_url)
            logger.info(f"Recieved [{response.status_code}] from: {url}")
            if response.status_code == 200:
                success = True
            
            else:
                raise Exception(f"Failed request, Status Code {response.status_code}")
                
                ## Extract Data

            soup = BeautifulSoup(response.text, "html.parser")
            
            div_cards = soup.find_all("div", class_="product-listing mb-1 border-bottom")


            for div_card in div_cards:

                name = div_card.find("div", class_="product-listing__product-name")

                g2_url = name.find("a").get("href")

                has_rating = div_card.find("span", class_="fw-semibold")
                rating = 0.0

                if has_rating:
                    rating = has_rating.text

                description = div_card.find("p").text
                
                search_data = SearchData(
                    name=name.text,
                    stars=rating,
                    g2_url=g2_url,
                    description=description
                )
                

                data_pipeline.add_data(search_data)
            logger.info(f"Successfully parsed data from: {url}")
            success = True
        
                    
        except Exception as e:
            logger.error(f"An error occurred while processing page {url}: {e}")
            logger.info(f"Retrying request for page: {url}, retries left {retries-tries}")
    if not success:
        raise Exception(f"Max Retries exceeded: {retries}")




def start_scrape(keyword, pages, location, data_pipeline=None, max_threads=5, retries=3):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(
            scrape_search_results,
            [keyword] * pages,
            [location] * pages,
            range(pages),
            [data_pipeline] * pages,
            [retries] * pages
        )


def process_business(row, location, retries=3):
    url = row["g2_url"]
    tries = 0
    success = False

    while tries <= retries and not success:
        response = requests.get(get_scrapeops_url(url, location=location))
        try:
            if response.status_code == 200:
                logger.info(f"Status: {response.status_code}")

                soup = BeautifulSoup(response.text, "html.parser")


                review_cards = soup.find_all("div", class_="paper paper--white paper--box mb-2 position-relative border-bottom")


                review_pipeline = DataPipeline(csv_filename=f"{row['name'].replace(' ', '-')}.csv")
                anon_count = 0
                for review_card in review_cards:
                    review_date = review_card.find("time")
                    if review_date:
                        date = review_date.get("datetime")
                        name_present = review_card.find("a", class_="link--header-color")
                        name = name_present.text if name_present else "anonymous"
                        if name == "anonymous":
                            name = f"{name}-{anon_count}"
                            anon_count += 1


                        job_title_present = review_card.find("div", class_="mt-4th")
                        job_title = job_title_present.text if job_title_present else "n/a"

                        rating_container = review_card.find("div", class_="f-1 d-f ai-c mb-half-small-only")
                        rating_div = rating_container.find("div")

                        rating_class = rating_div.get("class")

                        stars_string = rating_class[-1]
                        stars_large_number = float(stars_string.split("-")[-1])
                        stars_clean_number = stars_large_number/2

                        review_body = review_card.find("div", attrs={"itemprop": "reviewBody"}).text

                        info_container = review_card.find("div", class_="tags--teal")
                        incentives_dirty = info_container.find_all("div")
                        incentives_clean = []
                        source = ""
                        for incentive in incentives_dirty:
                            if incentive.text not in incentives_clean:
                                if "Review source:" in incentive.text:
                                    source = incentive.text.split(": ")[-1]
                                else:
                                    incentives_clean.append(incentive.text)
                        validated = "Validated Reviewer" in incentives_clean
                        incentivized = "Incentivized Review" in incentives_clean


                        review_data = ReviewData(
                            name=name,
                            date=date,
                            job_title=job_title,
                            rating=stars_clean_number,
                            full_review=review_body,
                            review_source=source,
                            validated=validated,
                            incentivized=incentivized
                        )                    
                    
                        review_pipeline.add_data(review_data)


                review_pipeline.close_pipeline()
                success = True

            else:
                logger.warning(f"Failed Response: {response.status_code}")
                raise Exception(f"Failed Request, status code: {response.status_code}")
        except Exception as e:
            logger.error(f"Exception thrown: {e}")
            logger.warning(f"Failed to process page: {row['g2_url']}")
            logger.warning(f"Retries left: {retries-tries}")
            tries += 1
    if not success:
        raise Exception(f"Max Retries exceeded: {retries}")
    else:
        logger.info(f"Successfully parsed: {row['g2_url']}")




def process_results(csv_file, location, max_threads=5, retries=3):
    logger.info(f"processing {csv_file}")
    with open(csv_file, newline="") as file:
        reader = list(csv.DictReader(file))

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
            executor.map(
                process_business,
                reader,
                [location] * len(reader),
                [retries] * len(reader)
            )

if __name__ == "__main__":

    MAX_RETRIES = 3
    MAX_THREADS = 5
    PAGES = 1
    LOCATION = "us"

    logger.info(f"Crawl starting...")

    ## INPUT ---> List of keywords to scrape
    keyword_list = ["online bank"]
    aggregate_files = []

    ## Job Processes
    for keyword in keyword_list:
        filename = keyword.replace(" ", "-")

        crawl_pipeline = DataPipeline(csv_filename=f"{filename}.csv")
        start_scrape(keyword, PAGES, LOCATION, data_pipeline=crawl_pipeline, max_threads=MAX_THREADS, retries=MAX_RETRIES)
        crawl_pipeline.close_pipeline()
        aggregate_files.append(f"{filename}.csv")
    logger.info(f"Crawl complete.")

    for file in aggregate_files:
        process_results(file, LOCATION, max_threads=MAX_THREADS, retries=MAX_RETRIES)