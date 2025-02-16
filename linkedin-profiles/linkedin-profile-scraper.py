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
        }
    proxy_url = "https://proxy.scrapeops.io/v1/?" + urlencode(payload)
    return proxy_url


## Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



@dataclass
class SearchData:
    name: str = ""
    display_name: str = ""
    url: str = ""
    location: str = ""
    companies: str = ""

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
class ProfileData:
    name: str = ""
    company: str = ""
    company_profile: str = ""
    job_title: str = ""
    followers: int = 0



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



def crawl_profiles(name, location, data_pipeline=None, retries=3):
    first_name = name.split()[0]
    last_name = name.split()[1]
    url = f"https://www.linkedin.com/pub/dir?firstName={first_name}&lastName={last_name}&trk=people-guest_people-search-bar_search-submit"
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
            profile_cards = soup.find_all("div", class_="base-search-card__info")
            for card in profile_cards:
                href = card.parent.get("href").split("?")[0]
                name = href.split("/")[-1].split("?")[0]
                display_name = card.find("h3", class_="base-search-card__title").text
                location = card.find("p", class_="people-search-card__location").text
                companies = "n/a"
                has_companies = card.find("span", class_="entity-list-meta__entities-list")
                if has_companies:
                    companies = has_companies.text

                search_data = SearchData(
                    name=name,
                    display_name=display_name,
                    url=href,
                    location=location,
                    companies=companies
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


def start_crawl(profile_list, location, data_pipeline=None, max_threads=5, retries=3):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(
            crawl_profiles,
            profile_list,
            [location] * len(profile_list),
            [data_pipeline] * len(profile_list),
            [retries] * len(profile_list)
        )


def scrape_profile(row, location, retries=3):
    url = row["url"]
    tries = 0
    success = False

    while tries <= retries and not success:
        response = requests.get(get_scrapeops_url(url, location=location))
        try:
            if response.status_code != 200:
                logger.warning(f"Failed Response: {response.status_code}")
                raise Exception(f"Failed Request, status code: {response.status_code}")

            logger.info(f"Status: {response.status_code}")
            soup = BeautifulSoup(response.text, "html.parser")
            head = soup.find("head")
            script = head.select_one("script[type='application/ld+json']")
            json_data_graph = json.loads(script.text)["@graph"]
            json_data = {}
            person_pipeline = DataPipeline(f"{row['name']}.csv")
            for element in json_data_graph:
                if element["@type"] == "Person":
                    json_data = element
                    break

            company = "n/a"
            company_profile = "n/a"
            job_title = "n/a"
            
            if "jobTitle" in json_data.keys() and type(json_data["jobTitle"] == list) and len(json_data["jobTitle"]) > 0:
                job_title = json_data["jobTitle"][0]
            
            has_company = "worksFor" in json_data.keys() and len(json_data["worksFor"]) > 0
            if has_company:
                company = json_data["worksFor"][0]["name"]
                has_company_url = "url" in json_data["worksFor"][0].keys()
                if has_company_url:
                    company_profile = json_data["worksFor"][0]["url"]
            
            has_interactions = "interactionStatistic" in json_data.keys()
            followers = 0
            if has_interactions:
                stats = json_data["interactionStatistic"]
                if stats["name"] == "Follows" and stats["@type"] == "InteractionCounter":
                    followers = stats["userInteractionCount"]
            
            profile_data = ProfileData (
                name=row["name"],
                company=company,
                company_profile=company_profile,
                job_title=job_title,
                followers=followers
            )
            person_pipeline.add_data(profile_data)       
            person_pipeline.close_pipeline()
            success = True
                
        except Exception as e:
            logger.error(f"Exception thrown: {e}")
            logger.warning(f"Failed to process page: {row['url']}, retries left: {retries-tries}")
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
                scrape_profile,
                reader,
                [location] * len(reader),
                [retries] * len(reader)
            )

if __name__ == "__main__":

    MAX_RETRIES = 3
    MAX_THREADS = 5
    
    LOCATION = "us"

    logger.info(f"Crawl starting...")

    ## INPUT ---> List of keywords to scrape
    keyword_list = ["bill gates", "elon musk"]

    ## Job Processes
    filename = "profile-crawl.csv"
    crawl_pipeline = DataPipeline(csv_filename=filename)
    start_crawl(keyword_list, LOCATION, data_pipeline=crawl_pipeline, max_threads=MAX_THREADS, retries=MAX_RETRIES)
    crawl_pipeline.close_pipeline()
    logger.info(f"Crawl complete.")

    process_results(filename, LOCATION, max_threads=MAX_THREADS, retries=MAX_RETRIES)