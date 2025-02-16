# Trustpilot Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [Trustpilot](https://www.trustpilot.com/).

It is designed for **educational purposes** and demonstrates how to scrape data from Trustpilot while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape Trustpilot With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-trustpilot/)

---

## Features  

This scraper extracts the following data from Trustpilot:


✅ Search Data - Data extracted from the Trustpilot Search results: 

| Field Name       | Description |
|-----------------|-------------|
| `name`          | Business name on Trustpilot. |
| `stars`         | Star rating of the business (out of 5). |
| `rating`        | TrustScore rating assigned by Trustpilot. |
| `num_reviews`   | Number of reviews submitted for the business. |
| `website`       | Official website of the business. |
| `trustpilot_url`| Trustpilot review page URL for the business. |
| `location`      | Country where the business is based. |
| `category`      | Category of the business (e.g., Finance, Retail). |




✅ Review Data - Data extracted from the the individual business review pages:

| Field Name       | Description |
|-----------------|-------------|
| `name`          | Name of the reviewer. |
| `rating`        | Star rating given by the reviewer (1-5). |
| `text`          | Full text of the review. |
| `title`         | Title or summary of the review. |
| `date`          | Date when the review was published. |



---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following Trustpilot's terms of service.

- You may view Trustpilot's terms [here](https://legal.trustpilot.com/for-reviewers/terms-of-use-for-consumers). 
- Their robots.txt is available [here](https://www.trustpilot.com/robots.txt).

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

`keyword_list` is a list of keywords that the script uses to search businesses on Trustpilot. Each keyword represents a business category, industry, or specific term that users might search for on Trustpilot.

You can customize the keywords you want to scrape in the `keyword_list` section of the script.  

For example:

```python
keyword_list = ["online bank"]
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Defines the maximum number of retries the scraper will attempt if a request fails (e.g., due to a network error or a non-200 HTTP response).
- `MAX_THREADS`: Defines the maximum number of threads that will be used to run the scraper concurrently.
- `PAGES`: Determines the number of search result pages to scrape for each keyword.
- `LOCATION`: Sets the country or region code used in the scraping process.


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `trustpilot_scraper.py`, and run it using:


```bash
python trustpilot_scraper.py
```

---

## Output Format
After the script completes, you will have several CSV files containing the extracted data for each keyword.
 
- **Search Data:** This file stores details of businesses that appear in Trustpilot search results based on the given keyword. (e.g. `keyword.csv`)
- **Business Specific Data:** For each business in the search results, the script fetches its reviews and saves them in a separate CSV file named `business_name.csv`.
