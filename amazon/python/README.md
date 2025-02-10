# Amazon.com Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** to extract product listing data from [Amazon](amazon.com).  

It is designed for **educational purposes** and demonstrates how to scrape large e-commerce websites while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape Amazon With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-amazon/)

---

## Features  

This scraper extracts the following Amazon data:  

✅ **Product Listings** – Data extracted from Amazon search results (multiple products on a search page).


| Data Point       | Description |
|-----------------|-------------|
| `name` | ASIN (Amazon Standard Identification Number) of the product. |
| `title` | Product title as displayed in search results. |
| `url` | Product URL on Amazon. |
| `is_ad` | Boolean indicating if the product is a sponsored (ad) listing. |
| `pricing_unit` | Currency symbol of the product price (e.g., `$`, `£`). |
| `price` | Current product price extracted from the listing. |
| `real_price` | Original price before discount, if applicable. |
| `rating` | Product rating as shown in search results. |

✅ **Product Details** – Data extracted from individual product pages.

| Data Point       | Description |
|-----------------|-------------|
| `name` | ASIN of the product. |
| `title` | Product title from the product page. |
| `url` | Full product page URL. |
| `pricing_unit` | Currency symbol. |
| `price` | Final price extracted from the product page. |
| `feature_1` | First key feature from the product description. |
| `feature_2` | Second key feature from the product description. |
| `feature_3` | Third key feature from the product description. |
| `feature_4` | Fourth key feature from the product description. |
| `images_1` | First product image URL. |
| `images_2` | Second product image URL. |
| `images_3` | Third product image URL. |
| `images_4` | Fourth product image URL. |


---

## Fair Use Disclaimer
This scraper is for educational purposes only. Web scraping should be done ethically and legally, following Amazon’s terms of service.

For Amazon you can check the links below.
- [Terms of Service](https://www.amazon.com/gp/help/customer/display.html?nodeId=202140280)
- [robots.txt](https://www.amazon.com/robots.txt)

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
In the `main` section of the script, you define the list of products you want to search for. 

The `PRODUCTS` list can be modified to include any product names you want to scrape data for. For example:

```python
PRODUCTS = ["phone", "laptop", "headphones"]
```

You can also adjust the following parameters:

- `PAGES`: The number of pages to scrape for each product.
- `MAX_RETRIES`: The number of retry attempts if a page fails to load.
- `MAX_THREADS`: The number of threads used for concurrent scraping.
- `LOCATION`: The location parameter (e.g., "us" for the USA).


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `amazon_scraper.py`, and run it using:


```bash
python amazon_scraper.py
```

---

## Output Format
The scraped data is saved into **a CSV file** for each product in the format `product_name.csv` (e.g., phone.csv).

Each CSV file will contain:
 -Product Name
- Title
- Price
- Rating
- URL
- And other product features
