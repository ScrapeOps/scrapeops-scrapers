# BestBuy Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [BestBuy](https://www.bestbuy.com/) search results.

It is designed for **educational purposes** and demonstrates how to scrape data from BestBuy while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape BestBuy With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-bestbuy/)

---

## Features  

This scraper extracts the following data from Walmart:


✅ Product Data - Data extracted from the BestBuy Search Results:


| Field        | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `name`       | The name of the product (e.g., "NVIDIA GeForce RTX 3080").                   |
| `url`        | The URL link to the product's page (e.g., "https://www.bestbuy.com/...").    |
| `price`      | The price of the product (e.g., "$699.99").                                 |
| `model_number` | The model number of the product (e.g., "RTX 3080").                         |
| `sku`        | The Stock Keeping Unit (SKU) identifier for the product (e.g., "1234567890"). |
| `rating`     | The rating given to the product, usually in decimal form (e.g., "4.7").      |
| `sponsored`  | A boolean value indicating whether the product is a sponsored listing (`True` means sponsored, `False` means not). |





✅ Review Data - Data extracted from the the individual BestBuy Product Pages:

| Field         | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `name`        | The name of the reviewer (e.g., "John Doe").                                |
| `rating`      | The rating given by the reviewer, typically in decimal form (e.g., "4.5").  |
| `incentivized`| A boolean value indicating whether the review is incentivized (`True` if incentivized, `False` if not). |
| `verified`    | A boolean value indicating whether the review was left by a verified purchaser (`True` for verified, `False` for unverified). |


---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following BestBuy's terms of service.

- You can view BestBuy's terms [here](https://www.bestbuy.com/site/help-topics/terms-and-conditions/pcmcat204400050067.c?id=pcmcat204400050067). 
- Their robots.txt is available [here](https://www.bestbuy.com/robots.txt).

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
  "api_key": "YOUR_API_KEY"
}
```

3. Replace "Replace "YOUR_API_KEY" with your actual ScrapeOps API key.




### 3. Configure Product Search Parameters
In the `main` section of the script, you define the search query you want to scrape. 

Each keyword corresponds to a separate search query on the BestBuy website.

You can customize the keywords you want to scrape in the `keyword_list` section of the script.  

For example:

```python
keyword_list = ["gpu"]
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Determines the maximum number of retries the script will attempt if a request fails (e.g., due to a network issue or a non-200 status code).
- `MAX_THREADS`: Defines the number of concurrent threads used during the scraping and processing tasks.
- `PAGES`: Specifies the number of pages to scrape for each keyword. Each page typically contains a set of search results.
- `LOCATION`: Sets the location/country code for the scraping requests. It is passed to the proxy URL to simulate requests coming from a specific region.


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `bestbuy_scraper.py`, and run it using:


```bash
python bestbuy_scraper.py
```

---

## Output Format
After the script finishes running, it will generate CSV files for each keyword, containing:

- **Product Search Result Data:** For each search query, a CSV file will be generated containing product data scraped from the search results. These files will contain information such as the product name, price, description, etc.

Example: laptop.csv

- **Product Review Data:** For each product, a separate CSV file will be created containing product review details such as ratings, review text, and reviewer information.

Example: laptop-reviews.csv