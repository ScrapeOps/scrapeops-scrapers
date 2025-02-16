# Redfin Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [Redfin](https://www.redfin.com/).

It is designed for **educational purposes** and demonstrates how to scrape data from Redfin while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape Redfin With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-redfin/)

---

## Features  

This scraper extracts the following data from Redfin:


✅ Search Data - Data extracted from the Redfin Search results: 

| **Field Name**     | **Description**                                                   |
|--------------------|-------------------------------------------------------------------|
| **name**           | Name of the property or product                                   |
| **price**          | Price of the property or product                                  |
| **price_currency** | Currency of the price (e.g., USD)                                 |
| **url**            | URL of the property or product listing                            |




✅ Property Data - Data extracted from the individual property pages:

| **Field Name**      | **Description**                                                   |
|---------------------|-------------------------------------------------------------------|
| **name**            | Name of the property                                              |
| **bedrooms**        | Number of bedrooms in the property                                |
| **bathrooms**       | Number of bathrooms in the property                               |
| **square_feet**     | Size of the property in square feet                               |
| **price_differential** | Difference in price (positive or negative) compared to market value |





---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following Redfin's terms of service.

- You may view Redfin's terms [here](https://www.redfin.com/about/terms-of-use). 
- Their robots.txt is available [here](https://www.redfin.com/robots.txt).

It's important to note that violation of these Terms could result in your account getting blocked or even permanently removed from the site.

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
The script will scrape Redfin based on a list of locations. In the `main` section of the script, you define the location you want to scrape. 

`location_list` is a list of dictionaries where each dictionary contains information about a specific search area, including the **city ID (id_number), state (state), and locality (locality)** on Redfin

Modify the `location_list` variable inside the script:


For example:

```python
location_list = [{"id_number": 12572, "state": "SC", "locality": "Myrtle Beach"}]
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Specifies the number of times the scraper will retry fetching a page if it encounters an error.
- `MAX_THREADS`: Defines the maximum number of threads to be used for concurrent scraping.
- `PAGES`: Specifies the number of pages to scrape for each keyword.
- `LOCATION`: Defines the geographic location from which the scraping requests appear to originate.


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `redfin_scraper.py`, and run it using:


```bash
python redfin_scraper.py
```

---

## Output Format
After the script completes, you will have several CSV files containing the extracted data for each keyword.
 
- **Search Data:** This file contains high-level data about the properties scraped from the Redfin search results based on the given keyword. (e.g. `location.csv`)
- **Property Specific Data:** For each property listed in the main CSV, the script scrapes detailed information from the individual property page on Redfin.

