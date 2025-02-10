# Nordstrom Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [Nordstrom](https://www.nordstrom.com/) search results.

It is designed for **educational purposes** and demonstrates how to scrape data from Nordstrom while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape Nordstrom With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-nordstrom/)

---

## Features  

This scraper extracts the following data from Nordstrom:


✅ Product Data - Data extracted from the Nordstrom Search Results:


| Field Name    | Description                                                   |
|----------------|---------------------------------------------------------------|
| **Name**       | The name of the product (e.g., "Stylish Winter Boots").       |
| **Image URL**  | The URL of the product image (e.g., "https://example.com/images/boots.jpg"). |
| **URL**        | The URL of the product page (e.g., "https://example.com/product/boots"). |
| **Price**      | The price of the product (e.g., "$129.99").                  |






✅ Review Data - Data extracted from the the individual Nordstrom Product Pages:

| Field Name    | Description                                                   |
|----------------|---------------------------------------------------------------|
| **Name**       | The name of the reviewer (e.g., "John Doe").                  |
| **Incentivized** | Whether the review is incentivized (True/False).             |
| **Verified**   | Whether the review is verified (True/False).                  |
| **Rating**     | The rating given by the reviewer (e.g., 4.5).                 |
| **Date**       | The date the review was posted (e.g., "2025-02-10").          |



---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following Nordstrom's terms of service.

When you scrape Nordstom, you are subject to their terms of service. You can be temporarily or even permanently banned for accessing their site with a bot. Also, you are subject to their robots.txt. 


- You can view Nordstrom's terms [here](https://www.nordstrom.com/browse/customer-service/policy/terms-conditions). 
- Their robots.txt is available [here](https://www.nordstrom.com/robots.txt).

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

Each keyword corresponds to a separate search query on the Nordstrom website.

You can customize the keywords you want to scrape in the `keyword_list` section of the script.  

For example:

```python
keyword_list = ["boots"]
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Maximum number of retry attempts for failed HTTP requests.
- `MAX_THREADS`: Maximum number of threads that will run concurrently during the scraping process.
- `PAGES`: How many pages of search results to scrape for each keyword.
- `LOCATION`: The geographic location or country code for the scraping process.


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `nordstrom_scraper.py`, and run it using:


```bash
python nordstrom_scraper.py
```

---

## Output Format
After the script finishes running, you should find CSV files generated for each keyword:

- **Product search data (boots.csv):** The product search CSV will contain information like the product name, price, image URL, and product URL.
- **Product review data (boots-reviews.csv):** The product review CSV will contain review data like the reviewer name, rating, and review details.
