import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, urlencode
import csv
import concurrent
from concurrent.futures import ThreadPoolExecutor
import os
import logging
import time
from dataclasses import dataclass, field, fields, asdict
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.3'}
proxy_url = "https://proxy.scrapeops.io/v1/"
API_KEY = "99363770-bd32-4a3c-9a11-16dbf3d7167d"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class SearchData:
    name: str
    base_url: str
    link: str
    page: int
    result_number: int

    def __post_init__(self):
        self.check_string_fields()
    def check_string_fields(self):
        for field in fields(self):
            if isinstance(getattr(self, field.name), str):
                if getattr(self, field.name) == "":
                    setattr(self, field.name, f"No {field.name}")
                    continue
                value = getattr(self, field.name)
                setattr(self, field.name, value.strip())


class DataPipeline:
    def __init__(self, csv_filename="", storage_queue_limit=50):
        self.names_seen = []
        self.storage_queue = []
        self.storage_queue_limit = storage_queue_limit
        self.csv_filename = csv_filename
        self.csv_open = False
    def save_to_csv(self):
        self.csv_open = True
        data_to_save = []
        data_to_save.extend(self.storage_queue)
        self.storage_queue.clear()
        if not data_to_save:
            return
        
        keys = [field.name for field in fields(data_to_save[0])]

        file_exists = os.path.isfile(self.csv_filename) and os.path.getsize(self.csv_filename)

        with open(self.csv_filename, mode="a", encoding="UTF-8") as output_file:
            writer = csv.DictWriter(output_file, fieldnames=keys)
            if not file_exists:
                writer.writeheader()
            for item in data_to_save:
                writer.writerow(asdict(item))
        self.csv_open = False

    def is_duplicate(self, input_data):
        if input_data.name in self.names_seen:
            logger.warning(f"Duplicate Item Found: {input_data.name}. Item dropped")
            return True
        self.names_seen.append(input_data.name)
        return False

    def add_data(self, scraped_data):
        if self.is_duplicate(scraped_data) == False:
            self.storage_queue.append(scraped_data)
        if len(self.storage_queue) >= self.storage_queue_limit and self.csv_open == False:
            self.save_to_csv()

    def close_pipeline(self):
        if self.csv_open:
            time.sleep(3)
        if len(self.storage_queue) > 0:
            self.save_to_csv()

def get_scrapeops_url(url):
    payload = {'api_key': API_KEY, 'url': url, 'country': 'us'}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url

def search_page(query, page, location="United States", headers=headers, pipeline=None, num=100, retries=3):
    url = f"https://www.google.com/search?q={query}&start={page * num}&num={num}"
    payload = {
        "api_key": API_KEY,
        "url": url,
    }
    tries = 0
    success = False
    while tries <= retries and not success:
        try:
            response = requests.get(get_scrapeops_url(url))
            soup = BeautifulSoup(response.text, 'html.parser')
            divs = soup.find_all("div")
            index = 0
            last_link = ""
            for div in divs:
                h3s = div.find_all("h3")
                if len(h3s) > 0:
                    link = div.find("a", href=True)
                    parsed_url = urlparse(link["href"])
                    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
                    site_info = {'title': h3s[0].text, "base_url": base_url, 'link': link["href"], "page": page, "result_number": index}
                    search_data = SearchData(
                        name = site_info["title"],
                        base_url = site_info["base_url"],
                        link = site_info["link"],
                        page = site_info["page"],
                        result_number = site_info["result_number"]
                    )            
                    if site_info["link"] != last_link:
                        index += 1
                        last_link = site_info["link"]
                        if pipeline:
                            pipeline.add_data(search_data)
                            success = True

        except:
            print(f"Failed to scrape page {page}")
            print(f"Retries left: {retries-tries}")
            tries += 1
    if not success:
        print(f"Failed to scrape page {page}, no retries left")
        raise Exception(f"Max retries exceeded: {retries}")
    else:
        print(f"Scraped page {page} with {retries-tries} retries left")

def full_search(query, pages=3, location="us", MAX_THREADS=5, MAX_RETRIES=3, num=10):
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        pipeline = DataPipeline(csv_filename=f"{query.replace(' ', '-')}.csv")
        tasks = [executor.submit(search_page, query, page, location, None, pipeline, num, MAX_RETRIES) for page in range(pages)]
        for future in tasks:
            future.result()
        pipeline.close_pipeline()

if __name__ == "__main__":
    MAX_THREADS = 5
    MAX_RETRIES = 5
    queries = ["cool stuff"]


    logger.info("Starting full search...")
    for query in queries:
        full_search(query, pages=3, num=10)
    logger.info("Search complete.")

