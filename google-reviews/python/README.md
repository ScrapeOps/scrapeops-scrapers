# Google Reviews Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [Google Reviews](https://business.google.com/reviews).

It is designed for **educational purposes** and demonstrates how to scrape data from Google Reviews while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape Google Reviews With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-google-reviews/)

---

## Features  

This scraper extracts the following data from Google Reviews:


✅ Search Data - Data extracted from the Google Maps search results page for each keyword: 

| **Field Name**      | **Description**                                                   |
|---------------|----------------------------------------------------|
| name          | The name of the business or location.             |
| stars         | The average rating (stars) of the business.       |
| url           | The URL of the business page on Google Maps.      |
| rating_count  | The total number of ratings or reviews received by the business. |




✅ Review Data - Data extracted from each individual business of Google Reviews listing:

| **Field Name**      | **Description**                                                   |
|-----------------|---------------------------------------------------------------|
| name            | The name of the reviewer (person who posted the review).      |
| stars           | The number of stars given by the reviewer.                    |
| time_left       | The time or date when the review was posted.                  |
| review_shortened| A shortened version or excerpt of the review text.            |




---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following Google's terms of service.

- You may view Google's terms [here](https://cloud.google.com/maps-platform/terms). 
- Their robots.txt is available [here](https://www.google.com/robots.txt).

Violating these terms could get your Google account suspended or even permanently deleted. Be careful about breaking rules online.

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
The script will scrape Google Reviews based on a list of keywords (e.g., "restaurant"). In the `main` section of the script, you define the search keywords you want to scrape. 

In the `keyword_list` variable, add the keywords you want to scrape data for. This is set as `["restaurant"]` in the script by default, but you can replace it with any keywords you want to target.

For example:

```python
keyword_list = ["restaurant"]
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Specifies the number of times the scraper will retry fetching a page if it encounters an error.
- `MAX_THREADS`: Defines the maximum number of threads to be used for concurrent scraping.
- `LOCALITIES`: The areas of the map you'd like to scrape. They need to be added in as latitude and longitude pairs.
- `LOCATION`: Defines the geographic location from which the scraping requests appear to originate.


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `google_reviews_scraper.py`, and run it using:


```bash
python google_reviews_scraper.py
```

---

## Output Format
After the script completes, you will have several CSV files containing the extracted data based on search results from Google Maps.
 
- **Search Data:** For each keyword, a CSV file will be created with data for the businesses found. The CSV files will be named after the keyword, replacing spaces with dashes, e.g., restaurant.csv.
- **Review Data:** The script scrapes the business pages to collect detailed information like hours of operation and addresses.

