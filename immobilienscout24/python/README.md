# Immobilienscout24 Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [Immobilienscout24](https://www.immobilienscout24.de/).

It is designed for **educational purposes** and demonstrates how to scrape data from Redfin while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape Immobilienscout24 With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-immobilienscout24/)

---

## Features  

This scraper extracts the following data from Immobilienscout24:


✅ Search Data - Data extracted from the Immobilienscout24 Search results: 

| **Field Name**      | **Description**                                                   |
|-------------------|--------------------------------------------------------------------------|
| name              | The name of the listing (e.g., address or title).                        |
| price             | The price of the property (cold rent).                                   |
| size              | The size of the property in square meters.                               |
| date_available    | The date when the property is available for rent.                        |
| url               | The URL of the listing for further details.                              |




✅ Cost Data - Data extracted from the individual property pages:

| **Field Name**      | **Description**                                                   |
|-------------------|--------------------------------------------------------------------------|
| name              | The name of the listing (e.g., address or title).                        |
| cold_rent         | The cold rent for the property (base rent).                              |
| price_per_m2      | The price per square meter for the property.                             |
| additional_costs  | The additional costs associated with the property (e.g., utilities).    |
| total_cost        | The total cost of the property (cold rent + additional costs).           |


---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following Immobilienscout24's terms of service.

We also need to pay attention to both their Terms and Conditions and their robots.txt. Immobilienscout24 explicitly prohibits scraping. We did violate their policies in this scrape for educational purposes.

- You may view Immobilienscout24's terms [here](https://www.immoscout24.ch/c/en/about-us/gtc). 
- Their robots.txt is available [here](https://www.immobilienscout24.de/robots.txt).

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
The script will scrape Immobilienscout24 based on a list of locations. In the `main` section of the script, you define the location you want to scrape. 

The `keyword_list` variable is hardcoded to scrape listings for **"Bavaria" (state)** and **"Munich" (city)**. If you want to scrape other areas, you can modify `keyword_list` accordingly.

Modify the `keyword_list` variable inside the script:


For example:

```python
keyword_list = [{"state": "bayern", "city": "muenchen"}]
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Specifies the number of times the scraper will retry fetching a page if it encounters an error.
- `MAX_THREADS`: Defines the maximum number of threads to be used for concurrent scraping.
- `PAGES`: Specifies the number of pages to scrape for each keyword.
- `LOCATION`: Defines the geographic location from which the scraping requests appear to originate.


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `immo_scraper.py`, and run it using:


```bash
python immo_scraper.py
```

---

## Output Format
After the script completes, you will have several CSV files containing the extracted data for each keyword.
 
- **Search Data:** This file contains general information about the listings found during the search based on the provided location (e.g., "Bavaria - Munich").
- **Property Specific Data:** This file provides detailed cost information about each individual property. It includes values such as rent, additional costs, and total costs for the listing.

