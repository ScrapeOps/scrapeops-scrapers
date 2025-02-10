# Leboncoin Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [Leboncoin](https://www.leboncoin.fr/) search results.

It is designed for **educational purposes** and demonstrates how to scrape data from Leboncoin while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape Leboncoin With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-leboncoin/)

---

## Features  

This scraper extracts the following data from Bing search result pages:

✅ Product Search Data - General information about the products found in search results:


| **Field Name** | **Description** |
|--------------|---------------|
| `name` | The name of the product (e.g., "Ford Mustang 2020"). |
| `url` | The direct link to the product listing on Leboncoin. |
| `price` | The price of the product, excluding the currency symbol. |
| `currency` | The currency in which the product is listed (e.g., "€", "$"). |


✅ Product Review Data - Detailed specifications of a specific product listing:

| **Field Name** | **Description** |
|--------------|---------------|
| `name` | The name of the vehicle (e.g., "Ford Mustang GT 2020"). |
| `description` | A text description of the vehicle provided by the seller. |
| `price` | The price of the vehicle, as extracted from the listing. |
| `currency` | The currency in which the vehicle is listed (e.g., "€", "$"). |
| `brand` | The brand or manufacturer of the vehicle (e.g., "Ford"). |
| `model` | The specific model of the vehicle (e.g., "Mustang GT"). |
| `year` | The year the vehicle was manufactured. |
| `mileage` | The total distance the vehicle has traveled (in kilometers/miles). |
| `transmission` | The type of transmission (e.g., "Automatic", "Manual"). |



---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following Leboncoin’s terms of service.

Leboncoin has their own Terms and Conditions and robots.txt that they expect people to follow. 

- You can view Leboncoin's Terms [here](https://www.leboncoin.fr/dc/cgv).
- You can view their robots.txt [here](https://www.leboncoin.fr/robots.txt). 

**Failure to respect these policies can even get you banned from the site.**

ScrapeOps take no responsibility for misuse of this code. Ensure you comply with all legal requirements before scraping Reddit.

---

## Issues & Support
This repository is provided as is with no official support. If you encounter bugs, please open an issue in the Issues tab.

---

## Installation  

### 1. Install Dependencies  
Ensure you have Python installed, then install the required dependencies:  

```bash
pip install requests
```

### 2.  Install ScrapeOps Proxy Service
The script uses the ScrapeOps proxy service for web scraping. You need an API key from ScrapeOps to use the service:

1. Visit [ScrapeOps](https://scrapeops.io/) and sign up for an API key.
2. Replace YOUR-SUPER-SECRET-API-KEY in the script with your actual API key:

```bash
API_KEY = "YOUR-SUPER-SECRET-API-KEY"
```


### 3. Configure Product Search Parameters
In the `main` section of the script, you define the search query you want to scrape. 

To scrape a different product, update the line below. For example:

```python
keyword_list = ["ford mustang"]  # Change this to any product you want
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Maximum number of retry attempts for failed HTTP requests.
- `MAX_THREADS`: Maximum number of threads that will run concurrently during the scraping process.
- `PAGES`: How many pages of search results to scrape for each keyword.
- `LOCATION`: The geographic location or country code for the scraping process.


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `leboncoin_scraper.py`, and run it using:


```bash
python leboncoin_scraper.py
```

---

## Output Format
The script generates CSV files containing the scraped data. There are two types of CSV files:

**1. Search Results Data (keyword.csv)**
- This file contains a list of vehicle listings found in the search results.
- The filename is based on the search keyword (e.g., ford-mustang.csv if the keyword is "Ford Mustang").

**2. Detailed Vehicle Data (vehicle_name.csv)**
- For each listing, the script extracts detailed data and saves it in a separate CSV file.
- The filename is based on the vehicle name extracted from the listing.