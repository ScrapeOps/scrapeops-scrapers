# Zillow Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [Zillow](https://www.zillow.com/).

It is designed for **educational purposes** and demonstrates how to scrape data from Zillow while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape Zillow With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-zillow/)

---

## Features  

This scraper extracts the following data from Zillow:


✅ Search Data - Data extracted from the Zillow Search results: 

| **Field Name**    | **Description**                                                   |
|-------------------|-------------------------------------------------------------------|
| name              | Name of the property listing.                                     |
| property_type     | Type of the property (e.g., house, apartment).                   |
| street_address    | Street address of the property.                                   |
| locality          | Locality (city or town) where the property is located.            |
| region            | Region or state of the property.                                  |
| postal_code       | Postal code of the property.                                      |
| url               | URL of the property page.                                         |





✅ Property Data - Data extracted from the individual property pages:

| **Field Name**    | **Description**                                                   |
|-------------------|-------------------------------------------------------------------|
| name              | Name of the property.                                             |
| price             | Price of the property in numeric format.                          |
| time_on_zillow    | Time duration the property has been listed on Zillow.             |
| views             | Number of views the property has received.                        |
| saves             | Number of saves (favorites) the property has received.            |






---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following Zillow's terms of service.

- You may view Zillow's terms [here](https://www.zillowgroup.com/terms-of-use/). 
- Their robots.txt is available [here](https://www.zillow.com/robots.txt).

It's important to note that violation of these Terms could result in your account getting blocked or even permanently removed from the site.

ScrapeOps take no responsibility for misuse of this code. Ensure you comply with all legal requirements before scraping BestBuy.

---

## Issues & Support
This repository is provided as is with no official support. If you encounter bugs, please open an issue in the Issues tab.

---

## Installation  

### 1. Install Dependencies  
Ensure you have Python installed, then install the required dependencies:  

```bash
pip install requests beautifulsoup4
```

### 2.  Install ScrapeOps Proxy Service
The script uses the ScrapeOps proxy service for web scraping. You need an API key from ScrapeOps to use the service:

1. Visit [ScrapeOps](https://scrapeops.io/) and sign up for an API key.
2. You need to create a `config.json` file that contains your API key for the proxy service. Here's how your `config.json` should look:

```json
{
  "api_key": "your_api_key_here"
}
```

3. Replace "Replace "your_api_key_here" with your actual ScrapeOps API key.




### 3. Configure Product Search Parameters
The script will scrape Zillow based on a list of locations or keywords. In the `main` section of the script, you define the search query you want to scrape. 

`keyword_list` is a list of keywords representing different geographical areas or search terms on Zillow. Each keyword triggers a separate scraping job. ("pr" is Puerto Ricto, if you want to do Michigan, add "mi")

Modify the `keyword_list` variable inside the script:


For example:

```python
    keyword_list = ["pr"]
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Specifies the number of times the scraper will retry fetching a page if it encounters an error.
- `MAX_THREADS`: Defines the maximum number of threads to be used for concurrent scraping.
- `PAGES`: Specifies the number of pages to scrape for each keyword.
- `LOCATION`: Defines the geographic location from which the scraping requests appear to originate.


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `zillow_scraper.py`, and run it using:


```bash
python zillow_scraper.py
```

---

## Output Format
After the script completes, you will have several CSV files containing the extracted data for each keyword.
 
- **Search Data:** This file contains high-level data about the properties scraped from the Zillow search results based on the given keyword. (e.g. `keyword.csv`)
- **Property Specific Data:** For each property listed in the main CSV, the script scrapes detailed information (price, views, saves, etc.) from the individual property page on Zillow. These CSV files are named after each property’s name and contain detailed information about that property.


