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
    price: int = 0
    price_currency: str = ""
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
class PropertyData:
    name: str = ""
    bedrooms: int = 0
    bathrooms: float = 0.0
    square_feet: int = 0
    price_differential: int = 0


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



def scrape_search_results(search_info, location, page_number, data_pipeline=None, retries=3):
    formatted_locality = search_info["locality"].replace(" ", "-")
    url = f"https://www.redfin.com/city/{search_info['id_number']}/{search_info['state']}/{formatted_locality}/page-{page_number+1}"
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
            
            script_tags = soup.select("script[type='application/ld+json']")
            for script in script_tags:
                json_data = json.loads(script.text)
                if type(json_data) != list:
                    continue

                product = {}
                for element in json_data:
                    if element["@type"] == "Product":
                        product = element
                        break

                search_data = SearchData(
                    name=product["name"],
                    price=product["offers"]["price"],
                    price_currency=product["offers"]["priceCurrency"],
                    url=product["url"]
                )
                data_pipeline.add_data(search_data)               

            logger.info(f"Successfully parsed data from: {url}")
            success = True        
                    
        except Exception as e:
            logger.error(f"An error occurred while processing page {url}: {e}")
            logger.info(f"Retrying request for page: {url}, retries left {retries-tries}")
            tries+=1
    if not success:
        raise Exception(f"Max Retries exceeded: {retries}")




def start_scrape(search_info, pages, location, data_pipeline=None, max_threads=5, retries=3):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(
            scrape_search_results,
            [search_info] * pages,
            [location] * pages,
            range(pages),
            [data_pipeline] * pages,
            [retries] * pages
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
                
                bedrooms = 0
                bedroom_holder = soup.select_one("div[data-rf-test-id='abp-beds']")
                if bedroom_holder:
                    bedrooms = int(bedroom_holder.find("div", class_="statsValue").text.replace("—", "0"))
                bathrooms = 0.0
                bathroom_holder = soup.select_one("div[data-rf-test-id='abp-baths']")
                if bathroom_holder:
                    bathrooms = float(bathroom_holder.find("div", class_="statsValue").text.replace("—", "0"))
                square_feet = 0
                size_holder = soup.select_one("div[data-rf-test-id='abp-sqFt']")
                if size_holder:
                    square_feet = int(size_holder.find("span", class_="statsValue").text.replace(",", ""))
                price_differential = 0
                difference_holder = soup.select_one("span[data-rf-test-name='avmDiffValue']")
                if difference_holder:
                    price_number = int(difference_holder.text.replace(",", ""))
                    color = difference_holder.get("class")
                    if color == "diffValue red":
                        price_differential = -price_number
                    else:
                        price_differential = price_number
                property_pipeline = DataPipeline(f"{row['name'].replace(' ', '-')}.csv")
                property_data = PropertyData(
                    name=row["name"],
                    bedrooms=bedrooms,
                    bathrooms=bathrooms,
                    square_feet=square_feet,
                    price_differential=price_differential
                )
                property_pipeline.add_data(property_data)
                property_pipeline.close_pipeline()
                success = True

            else:
                logger.warning(f"Failed Response: {response.status_code}")
                raise Exception(f"Failed Request, status code: {response.status_code}")
        except Exception as e:
            logger.error(f"Exception thrown: {e}")
            logger.warning(f"Failed to process page: {row['url']}, Retries left: {retries-tries}")
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
    PAGES = 3
    LOCATION = "us"

    logger.info(f"Crawl starting...")

    ## INPUT ---> List of keywords to scrape
    location_list = [{"id_number": 12572, "state": "SC", "locality": "Myrtle Beach"}]
    aggregate_files = []

    ## Job Processes
    for search_area in location_list:
        filename = search_area["locality"].replace(" ", "-")

        crawl_pipeline = DataPipeline(csv_filename=f"{filename}.csv")
        start_scrape(search_area, PAGES, LOCATION, data_pipeline=crawl_pipeline, max_threads=MAX_THREADS, retries=MAX_RETRIES)
        crawl_pipeline.close_pipeline()
        aggregate_files.append(f"{filename}.csv")
    logger.info(f"Crawl complete.")

    for file in aggregate_files:
        process_results(file, LOCATION, max_threads=MAX_THREADS, retries=MAX_RETRIES)