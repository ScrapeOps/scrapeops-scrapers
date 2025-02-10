# Google Search Results Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [Google](google.com) search results.

It is designed for **educational purposes** and demonstrates how to scrape search engine results while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape Google Search Results With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-google-search/)

---

## Features  

This scraper extracts the following data from Google search result pages:

✅ Search Result Listings - Data extracted from the search result pages.


| Data Point         | Description |
|--------------------|-------------|
| `name`             | Title of the search result. |
| `base_url`         | Base URL of the linked page (e.g., `https://www.example.com`). |
| `link`             | Full URL to the search result. |
| `page`             | The page number of the search results. |
| `result_number`    | The index of the result on the page (e.g., first, second). |



---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following Google’s terms of service.

You can look at Google's robots.txt [here](https://www.google.com/robots.txt). In addition, if you're unclear about whether or not you can scrape a site, check their Terms and Conditions.

You can view Google's Terms and Conditions [here](https://policies.google.com/terms). 

ScrapeOps take no responsibility for misuse of this code. Ensure you comply with all legal requirements before scraping Amazon.

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

### 2. Install ScrapeOps Proxy Service
The script uses the ScrapeOps proxy service for web scraping. You need an API key from ScrapeOps to use the service:

1. Visit [ScrapeOps](https://scrapeops.io/) and sign up for an API key.
2. Replace "YOUR-SUPER-SECRET-API-KEY" in the script with your actual ScrapeOps API key:


```bash
SCRAPEOPS_API_KEY=your_api_key_here
```

### 3. Configure Product Search Parameters
In the `main` section of the script, you define the search queries. The queries list can be modified to include any keywords you want to scrape results for. For example:

For example:

```python
queries = ["cool gadgets", "best laptops 2025"]
```

You can also adjust the following parameters:

- `PAGES`: The number of pages to scrape for each query.
- `MAX_RETRIES`: The number of retry attempts if a page fails to load.
- `MAX_THREADS`:  The number of threads to use for concurrent scraping.
- `NUM`: The number of search results per page.


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `google_search_scraper.py`, and run it using:


```bash
python google_search_scraper.py
```

---

## Output Format
The scraped data is saved into **a CSV file** for each product in the format `query-name.csv` (e.g., cool-gadgets.csv).

Each CSV file will contain:
- Name: The title of the search result.
- Base URL: The base URL of the linked page.
- Link: The full URL to the search result.
- Page: The page number of the search results.
- Result Number: The position of the result on the page.
