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
        "wait": 2000
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
class ReplyData:
    name: str = ""
    reply: str = ""

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
    result_number = page_number * 10
    url = f"https://www.google.com/search?q={formatted_keyword}%20site%3Aquora.com&start={result_number}"
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
            div_cards = soup.select("div span")


            for div_card in div_cards:
                name = div_card.find("h3")
                link = div_card.find("a")

                if not name or not link:
                    continue

                result_number += 1
                ranking = result_number

                search_data = SearchData(
                    name=name.text,
                    url=link.get("href"),
                    rank=ranking
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


def process_post(row, location, retries=3):
    url = row["url"]
    tries = 0
    success = False

    while tries <= retries and not success:
        response = requests.get(get_scrapeops_url(url, location=location))
        try:
            if response.status_code == 200:
                logger.info(f"Status: {response.status_code}")

                soup = BeautifulSoup(response.text, "html.parser")
                main_content = soup.select_one("div[id='mainContent']")
                answer_cards = main_content.select("div div div div div[class='q-box']")

                answer_pipeline = DataPipeline(csv_filename=f"{row['name'].replace(' ', '-')}.csv")

                last_seen_name = ""
                for answer_card in answer_cards:
                    excluded_words = ["All related", "Recommended"]
                    array = answer_card.text.split("·")

                    if len(array) < 3:
                        continue

                    promoted = "Promoted" in array[0]
                    related =  "Related" in array[2][0:30] or "Related" in array[-2][0:30]
                    repeat_name = array[0] in last_seen_name or array[0] == last_seen_name

                    if promoted or related or repeat_name:
                        last_seen_name = array[0]
                        continue

                    reply_data = ReplyData(
                        name=array[0],
                        reply=array[-2]
                    )
                    answer_pipeline.add_data(reply_data)

                answer_pipeline.close_pipeline()
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
                process_post,
                reader,
                [location] * len(reader),
                [retries] * len(reader)
            )

if __name__ == "__main__":

    MAX_RETRIES = 3
    MAX_THREADS = 5
    PAGES = 5
    LOCATION = "us"

    logger.info(f"Crawl starting...")

    ## INPUT ---> List of keywords to scrape
    keyword_list = ["learn rust"]
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