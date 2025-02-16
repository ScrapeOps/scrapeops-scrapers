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

def get_scrapeops_url(url):
    payload = {
        "api_key": API_KEY,
        "url": url,
        "wait": 3000
        }
    proxy_url = "https://proxy.scrapeops.io/v1/?" + urlencode(payload)
    return proxy_url


## Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class SearchData:
    name: str = ""
    url: str = ""
    rank: int = 0
    rank_change: int = 0
    average_visit: str = ""
    pages_per_visit: float = 0.0
    bounce_rate: str = ""

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
class CompetitorData:
    name: str = ""
    url: str = ""
    affinity: str = ""
    monthly_visits: str = ""
    category: str = ""
    category_rank: int = None

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



def scrape_search_results(keyword, data_pipeline=None, retries=3):
    url = f"https://www.similarweb.com/top-websites/{keyword['category']}/{keyword['subcategory']}/"
    tries = 0
    success = False
    
    while tries <= retries and not success:
        try:
            scrapeops_proxy_url = get_scrapeops_url(url)
            response = requests.get(scrapeops_proxy_url)
            logger.info(f"Recieved [{response.status_code}] from: {url}")
            if response.status_code != 200:
                raise Exception(f"Failed request, Status Code {response.status_code}")
                
            soup = BeautifulSoup(response.text, "html.parser")            
            rows = soup.find_all("tr", class_="top-table__row")
            
            rank = 1
            for row in rows:
                link_holder = row.find("a", class_="tw-table__compare")
                site_name = link_holder.text
                link = f"https://www.similarweb.com/website/{site_name}/"

                rank_change_holder = row.find("td", class_="top-table__column top-table__column--rank-change")
                rank_change = 0
                up_or_down = rank_change_holder.find("span").get("class")[1]
                if "change--up" in up_or_down:
                    rank_change += int(rank_change_holder.text)
                elif "change--down" in up_or_down:
                    rank_change -= int(rank_change_holder.text)
                
                average_visit = row.find("span", class_="tw-table__avg-visit-duration").text
                pages_per_visit = float(row.find("span", class_="tw-table__pages-per-visit").text)
                bounce_rate = row.find("span", class_="tw-table__bounce-rate").text
                                
                search_data = SearchData(
                    name=site_name,
                    url=link,
                    rank=rank,
                    rank_change=rank_change,
                    average_visit=average_visit,
                    pages_per_visit=pages_per_visit,
                    bounce_rate=bounce_rate
                )
                rank+=1                

                data_pipeline.add_data(search_data)
            logger.info(f"Successfully parsed data from: {url}")
            success = True
        
                    
        except Exception as e:
            logger.error(f"An error occurred while processing page {url}: {e}, retries left {retries-tries}")
            tries+=1
    if not success:
        raise Exception(f"Max Retries exceeded: {retries}")


def start_scrape(keywords, data_pipeline=None, max_threads=5, retries=3):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(
            scrape_search_results,
            keywords,
            [data_pipeline] * len(keywords),
            [retries] * len(keywords)
        )


def process_website(row, retries=3):
    url = row["url"]
    tries = 0
    success = False

    while tries <= retries and not success:
        response = requests.get(url)
        try:
            if response.status_code != 200:
                raise Exception(f"Failed request, Status Code {response.status_code}")
            else:
                logger.info(f"Status: {response.status_code}")

                soup = BeautifulSoup(response.text, "html.parser")
                blocked = soup.find("div", class_="wa-limit-modal")
                if blocked:
                    raise Exception(f"Blocked")
                competitors = soup.find_all("div", class_="wa-competitors__list-item")

                competitor_pipeline = DataPipeline(csv_filename=f"{row['name'].replace(' ', '-')}.csv")
                for competitor in competitors:
                    site_name = competitor.find("span", class_="wa-competitors__list-item-title").text
                    link = f"https://www.similarweb.com/website/{site_name}/"
                    affinity = competitor.find("span", class_="app-progress__value").text
                    target_spans = competitor.find_all("span", "wa-competitors__list-column")

                    monthly_visits = target_spans[2].text
                    category = target_spans[3].text
                    category_rank = int(target_spans[4].text.replace("#", "").replace(",", "").replace("--", "0"))

                    competitor_data = CompetitorData(
                        name=site_name,
                        url=link,
                        affinity=affinity,
                        monthly_visits=monthly_visits,
                        category=category,
                        category_rank=category_rank
                    )
                    
                    competitor_pipeline.add_data(competitor_data)

                competitor_pipeline.close_pipeline()
                success = True

        except Exception as e:
            logger.error(f"Exception thrown: {e}")
            logger.warning(f"Failed to process page: {row['url']}, Retries left: {retries-tries}")
            tries += 1
    if not success:
        raise Exception(f"Max Retries exceeded: {retries}")
    else:
        logger.info(f"Successfully parsed: {row['url']}")


def process_results(csv_file, retries=3):
    logger.info(f"processing {csv_file}")
    with open(csv_file, newline="") as file:
        reader = list(csv.DictReader(file))

        for row in reader:
            process_website(row, retries=retries)

if __name__ == "__main__":

    MAX_RETRIES = 3
    MAX_THREADS = 5

    logger.info(f"Crawl starting...")

    ## INPUT ---> List of keywords to scrape
    keyword_list = [{"category": "arts-and-entertainment", "subcategory": "humor"}, {"category": "arts-and-entertainment", "subcategory": "animation-and-comics"}]
    aggregate_files = []

    ## Job Processes
    filename = "arts-and-entertainment"

    crawl_pipeline = DataPipeline(csv_filename=f"{filename}.csv")
    start_scrape(keyword_list, data_pipeline=crawl_pipeline, max_threads=MAX_THREADS, retries=MAX_RETRIES)
    crawl_pipeline.close_pipeline()
    aggregate_files.append(f"{filename}.csv")
    logger.info(f"Crawl complete.")

    for file in aggregate_files:
        process_results(file, retries=MAX_RETRIES)