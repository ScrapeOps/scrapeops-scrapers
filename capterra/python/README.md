# Capterra Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [Capterra](https://www.capterra.com/).

It is designed for **educational purposes** and demonstrates how to scrape data from Capterra while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape Capterra With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-capterra/)

---

## Features  

This scraper extracts the following data from Capterra:


✅ Search Data - Data extracted from the Capterra Search results: 

| Field Name    | Description                          |
|--------------|--------------------------------------|
| `name`       | Product name from the search results. |
| `url`        | The URL of the product's page on Capterra. |
| `rating`     | The overall rating of the product. |
| `review_count` | The total number of reviews for the product. |





✅ Review Data - Data extracted from the individual business review pages:

| Field Name         | Description                          |
|-------------------|--------------------------------------|
| `name`           | Name of the reviewer.               |
| `overall`        | Overall rating given by the reviewer. |
| `ease_of_use`    | Rating for ease of use.            |
| `customer_service` | Rating for customer service.     |





---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following Capterra's terms of service.

- You may view Capterra's terms [here](https://www.capterra.com/legal/terms-of-use/). 
- Their robots.txt is available [here](https://www.capterra.com/robots.txt).

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
The script will scrape Capterra based on a list of keywords. In the `main` section of the script, you define the search query you want to scrape. 

Modify the `keyword_list` variable inside the script:


For example:

```python
keyword_list = ["cryptocurrency-exchange-software"]
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Specifies the number of times the scraper will retry fetching a page if it encounters an error.
- `MAX_THREADS`: Defines the maximum number of threads to be used for concurrent scraping.
- `PAGES`: Specifies the number of pages to scrape for each keyword.
- `LOCATION`: Defines the geographic location from which the scraping requests appear to originate.


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `capterra_scraper.py`, and run it using:


```bash
python capterra_scraper.py
```

---

## Output Format
After the script completes, you will have several CSV files containing the extracted data for each keyword.
 
- **Search Data:** This file stores details of businesses that appear in G2 search results based on the given keyword. (e.g. `keyword.csv`)
- **Business Specific Data:** For each business in the search results, the script fetches its reviews and saves them in a separate CSV file named `business_name.csv`.
