# Bing.com Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [Bing](bing.com) search results.

It is designed for **educational purposes** and demonstrates how to scrape search engine results while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape Bing With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-bing/)

---

## Features  

This scraper extracts the following data from Bing search result pages:

✅ Search Result Listings - Data extracted from the search result pages.


| **Item**            | **Description**                                                                 |
|---------------------|---------------------------------------------------------------------------------|
| **Search Results**   | Scrapes search result headers (e.g., titles) from Bing search results pages.    |
| **URLs**             | Scrapes URLs from the search results to gather links to further scrape.         |
| **Meta Data**        | Scrapes the `title` and `description` meta tags from the pages linked in results. |
| **Headers**          | Scrapes the `<h2>` headers from the search results for relevant titles.         |
| **Base URL**         | Extracts the base URL (e.g., `https://example.com`) from each scraped link.     |
| **Page Rank**        | Records the rank of each result in the search result list.                      |




---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following Bing’s terms of service.

You can view their terms of service [here](https://www.microsoft.com/en-us/servicesagreement). Since Bing is a Microsoft product, it is subject to their terms. You can view their robots.txt [here](https://www.bing.com/robots.txt).

ScrapeOps take no responsibility for misuse of this code. Ensure you comply with all legal requirements before scraping Bing.

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
2. You need to create a `config.json` file that contains your API key for the proxy service. Here's how your config.json should look:

```json
{
  "api_key": "YOUR_API_KEY"
}
```

3. Replace "Replace "YOUR_API_KEY" with your actual ScrapeOps API key.




### 3. Configure Product Search Parameters
In the `main` section of the script, you define the search queries. The queries list can be modified to include any keywords you want to scrape results for. For example:

For example:

```python
keyword_list = ["learn rust"]
```

You can also adjust the following parameters:

- `PAGES`: The number of pages to scrape for each query.
- `MAX_RETRIES`: The number of retry attempts if a page fails to load.
- `MAX_THREADS`:  The number of threads to use for concurrent scraping.
- `LOCATION`: The location/country for search results (e.g., "us" for the United States).


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `bing_scraper.py`, and run it using:


```bash
python bing_scraper.py
```

---

## Output Format
After running the script, you should see logs printed in your console with information about each page being scraped. The results will be saved in **CSV files** named after the keywords, for example: `query-name.csv` (e.g., learn-rust.csv).


Each CSV file will contain:
- name: The title of the search result.
- base_url: The base URL extracted from the result link.
- url: The full URL of the search result.
- page: The page number of the search result.
- result_number: The rank of the result on that page.
