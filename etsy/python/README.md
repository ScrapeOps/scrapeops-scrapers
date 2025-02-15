# Etsy Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [Etsy](https://etsy.com/) search results.

It is designed for **educational purposes** and demonstrates how to scrape data from Etsy while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape Etsy With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-etsy/)

---

## Features  

This scraper extracts the following data from Etsy:


✅ Product Data - Data extracted from the Etsy Search Results:


| Field Name        | Description                                               |
|-------------------|-----------------------------------------------------------|
| `name`            | The name of the product.                                  |
| `stars`           | The average rating (stars) of the product.                |
| `url`             | The URL of the product listing.                           |
| `price_currency`  | The currency symbol used for the product price.           |
| `listing_id`      | The unique ID for the product listing.                    |
| `current_price`   | The current price of the product.                         |
| `original_price`  | The original price of the product (if discounted).        |






✅ Review Data - Data extracted from the the individual Etsy Product Pages:

| Field Name        | Description                                               |
|-------------------|-----------------------------------------------------------|
| `name`            | The name of the reviewer.                                 |
| `date`            | The date the review was posted.                           |
| `review`          | The content of the review.                                |
| `stars`           | The rating (stars) given by the reviewer.                 |




---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following Etsy's terms of service.

While scraping Etsy data might be legal, Etsy does explicitly prohibit scraping. You need to be aware of both their Terms of Use and their robots.txt. 

Violating these policies can lead to suspension and even a permanent ban from the site.

- You can view Etsy's terms [here](https://www.etsy.com/legal/terms-of-use). 
- Their robots.txt is available [here](https://www.etsy.com/robots.txt).

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

Each keyword corresponds to a separate search query on the Etsy website.

You can customize the keywords you want to scrape in the `keyword_list` section of the script.  

For example:

```python
keyword_list = ["coffee mug"]
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Specifies the number of times the scraper will retry fetching a page if it encounters an error.
- `MAX_THREADS`: Defines the maximum number of threads to be used for concurrent scraping.
- `PAGES`:Specifies the number of pages to scrape for each keyword.
- `LOCATION`:Defines the geographic location from which the scraping requests appear to originate.

**WARNING:** This code uses the bypass setting of `generic_level_4`. It costs **85 API credits per call**. This configuration costs significantly more than standard requests to the ScrapeOps API.

---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `etsy_scraper.py`, and run it using:


```bash
python etsy_scraper.py
```

---

## Output Format
After the script completes, you will have several CSV files containing the extracted data for each keyword.

- **Search Data:** For each product found in the search results, the script will save the data (e.g., name, stars, price, etc.) to CSV files named after each keyword.

- **Review Data:** After collecting search results, the script will attempt to scrape reviews for each product and save the review data (e.g., name, date, review, stars) to individual CSV files for each product.
