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
        "render_js": True,
        "bypass": "generic_level_3",
        "country": location,
        }
    proxy_url = "https://proxy.scrapeops.io/v1/?" + urlencode(payload)
    return proxy_url


## Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class SearchData:
    name: str = ""
    price: str = ""
    size: str = ""
    date_available: str = ""
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
class CostData:
    name: str = ""
    cold_rent: str = ""
    price_per_m2: str = ""
    additional_costs: str = ""
    total_cost: str = ""


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
    base_url = f"https://www.immobilienscout24.de/Suche/de/{search_info['state']}/{search_info['city']}/wohnung-mieten"
    url = ""
    if page_number != 0:
        url = f"{base_url}?pagenumber={page_number+1}"
    else:
        url = base_url
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
            
            div_cards = soup.find_all("div", class_="result-list-entry__data")
            if not div_cards:
                raise Exception("Listings failed to load!")

            for card in div_cards:
                name = card.find("div", class_="result-list-entry__address font-ellipsis").text
                href = card.find("a").get("href")
                link = ""
                prefix =  "https://www.immobilienscout24.de"
                if prefix in href:
                    continue
                else:
                    link = f"{prefix}{href}"
                attributes_card = card.select_one("div[data-is24-qa='attributes']")
                attributes = attributes_card.find_all("dl")

                price = attributes[0].text.replace("Kaltmiete", "")
                size = attributes[1].text.replace("Wohnfläche", "")
                date_available = "n/a"
                date_text = attributes[2].find("dd").text
                if "Zi" not in date_text:
                    date_available = date_text

                search_data = SearchData(
                    name=name,
                    price=price,
                    size=size,
                    date_available=date_available,
                    url=link
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

                costs_pipeline = DataPipeline(csv_filename=f"COST-{row['name']}.csv")
                
                cold_rent = soup.find("dd", class_="is24qa-kaltmiete grid-item three-fifths").text.strip()
                price_per_m2 = soup.find("dd", class_="is24qa-preism² grid-item three-fifths").text\
                    .replace("Kalkuliert von ImmoScout24", "").strip()
                additional_costs = soup.find("dd", class_="is24qa-nebenkosten grid-item three-fifths").text.strip()
                heating_costs = soup.find("dd", class_="is24qa-heizkosten grid-item three-fifths").text.strip()
                total_cost = soup.find("dd", class_="is24qa-gesamtmiete grid-item three-fifths font-bold").text.strip()

                cost_data = CostData(
                    name=row["name"],
                    cold_rent=cold_rent,
                    price_per_m2=price_per_m2,
                    additional_costs=additional_costs,
                    total_cost=total_cost
                )
                costs_pipeline.add_data(cost_data)
                costs_pipeline.close_pipeline()
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
    LOCATION = "de"

    logger.info(f"Crawl starting...")

    ## INPUT ---> List of keywords to scrape
    keyword_list = [{"state": "bayern", "city": "muenchen"}]
    aggregate_files = []

    ## Job Processes
    for keyword in keyword_list:
        filename = f"{keyword['state']}-{keyword['city']}"

        crawl_pipeline = DataPipeline(csv_filename=f"{filename}.csv")
        start_scrape(keyword, PAGES, LOCATION, data_pipeline=crawl_pipeline, max_threads=MAX_THREADS, retries=MAX_RETRIES)
        crawl_pipeline.close_pipeline()
        aggregate_files.append(f"{filename}.csv")
    logger.info(f"Crawl complete.")

    for file in aggregate_files:
        process_results(file, LOCATION, max_threads=MAX_THREADS, retries=MAX_RETRIES)