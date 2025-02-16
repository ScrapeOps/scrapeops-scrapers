# Yelp Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [Yelp](https://www.yelp.com/).

It is designed for **educational purposes** and demonstrates how to scrape data from Yelp while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape Yelp With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-yelp/)

---

## Features  

This scraper extracts the following data from Yelp:


✅ Search Data - Data extracted from the Yelp Search results: 

| Field Name     | Description |
|---------------|-------------|
| name          | The name of the business or restaurant. |
| sponsored     | A boolean indicating whether the listing is a sponsored ad. |
| stars         | The star rating of the business. |
| rank          | The position of the business in the search results. |
| review_count  | The total number of reviews for the business. |
| url           | The Yelp URL of the business. |





✅ Review Data - Data extracted from the the individual business review pages:

| Field Name       | Description |
|-----------------|-------------|
| name           | The name of the reviewer. If the reviewer is anonymous, it will be marked as "Unknown User" with an index. |
| family_friendly | A boolean indicating whether the business is family-friendly. |
| date           | The date when the review was posted. |
| position       | The position of the review in the list of reviews. |






---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following Yelp's terms of service.

- You may view Yelp's terms [here](https://terms.yelp.com/tos/en_us/20240710_en_us/). 
- Their robots.txt is available [here](https://www.yelp.com/robots.txt).

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
  "api_key": "your_scrapeops_api_key_here"
}
```

3. Replace "Replace "your_scrapeops_api_key_here" with your actual ScrapeOps API key.




### 3. Configure Product Search Parameters
The script will scrape Yelp based on a list of keywords. In the `main` section of the script, you define the search query you want to scrape. 

Modify the `keyword_list` variable inside the script:


For example:

```python
keyword_list = ["coffee shops"]
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Specifies the number of times the scraper will retry fetching a page if it encounters an error.
- `MAX_THREADS`: Defines the maximum number of threads to be used for concurrent scraping.
- `PAGES`: Specifies the number of pages to scrape for each keyword.
- `LOCATION`: Defines the geographic location from which the scraping requests appear to originate.


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `yelp_scraper.py`, and run it using:


```bash
python yelp_scraper.py
```

---

## Output Format
After the script completes, you will have several CSV files containing the extracted data for each keyword.
 
- **Search Data:** This file stores details of businesses that appear in G2 search results based on the given keyword. (e.g. `keyword.csv`)
- **Business Specific Data:** For each business in the search results, the script fetches its reviews and saves them in a separate CSV file named `business_name.csv`.
