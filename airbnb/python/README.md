# Airbnb Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [Airbnb](https://play.google.com/store/).

It is designed for **educational purposes** and demonstrates how to scrape data from Airbnb while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape Airbnb With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-airbnb/)

---

## Features  

This scraper extracts the following data from Airbnb:


✅ Search Data - Data extracted from the Airbnb search results page for each keyword: 

| Field Name   | Description                                   |
|-------------|-----------------------------------------------|
| `name`       | Name of the Airbnb listing.                 |
| `description` | Description of the Airbnb listing.          |
| `dates`      | Available dates or date-related details.    |
| `price`      | Price of the listing.                       |
| `url`        | Direct URL to the Airbnb listing.           |




✅ Review Data - Data extracted from each individual Airbnb listing:

| Field Name  | Description                               |
|------------|-------------------------------------------|
| `name`     | Name of the reviewer.                    |
| `stars`    | Number of stars given by the reviewer.   |
| `review`   | Text content of the review.              |



---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following Airbnb's terms of service.

When you access Airbnb, you are subject to their terms of service. On top of that, when you access their site with a bot (in this case a scraper), you are subject to their robots.txt.

- You may view Airbnb's terms [here](https://www.airbnb.com/help/article/2908). 
- Their robots.txt is available [here](https://www.airbnb.com/robots.txt).

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
  "api_key": "your-super-secret-api-key"
}
```

3. Replace "Replace "your-super-secret-api-key" with your actual ScrapeOps API key.




### 3. Configure Product Search Parameters
The script will scrape Airbnb based on a list of keywords (e.g., "South California"). In the `main` section of the script, you define the search keywords you want to scrape. 

The `keyword_list` contains the keywords you want to search for on the Airbnb. Modify the `keyword_list` in the script with your desired search locations.

For example:

```python
keyword_list = ["Myrtle Beach, South Carolina, United States"]
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Specifies the number of times the scraper will retry fetching a page if it encounters an error.
- `MAX_THREADS`: Defines the maximum number of threads to be used for concurrent scraping.
- `LOCATION`: Defines the geographic location from which the scraping requests appear to originate.
- `PAGES`: Determines how many pages of search results the scraper will attempt to process.


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `airbnb_scraper.py`, and run it using:


```bash
python airbnb_scraper.py
```

---

## Output Format
After the script completes, you will have several CSV files containing the extracted data based on search results from Airbnb.

- **Search Data:** For each keyword, a CSV file will be created and contain details that match the keywords you provided. The CSV file names are based on the search location.
- **Review Data:** This file will contain details about the reviews for each listing.