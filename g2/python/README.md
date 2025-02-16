# G2 Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [G2](https://www.g2.com/).

It is designed for **educational purposes** and demonstrates how to scrape data from G2 while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape G2 With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-g2/)

---

## Features  

This scraper extracts the following data from G2:


✅ Search Data - Data extracted from the G2 Search results: 

| Field Name  | Description |
|-------------|------------|
| `name`      | Name of the product or service found in the G2 search results. |
| `stars`     | Average star rating of the product on G2. |
| `g2_url`    | URL of the product's G2 page. |
| `description` | Short description of the product from G2. |





✅ Review Data - Data extracted from the individual business review pages:

| Field Name    | Description |
|--------------|------------|
| `name`       | Name of the reviewer (or "anonymous" if not provided). |
| `date`       | Date when the review was posted. |
| `job_title`  | Job title of the reviewer. |
| `rating`     | Star rating given by the reviewer (converted from G2’s visual representation). |
| `full_review` | The full text of the review. |
| `review_source` | Source of the review (if mentioned). |
| `validated`  | Boolean flag indicating if the reviewer is verified. |
| `incentivized` | Boolean flag indicating if the reviewer was incentivized to leave a review. |




---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following G2's terms of service.

- You may view G2's terms [here](https://legal.g2.com/terms-of-use). 
- Their robots.txt is available [here](https://www.g2.com/robots.txt).

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
The script will scrape G2 based on a list of keywords. In the `main` section of the script, you define the search query you want to scrape. 

Modify the `keyword_list` variable inside the script:


For example:

```python
keyword_list = ["online bank"]
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Specifies the number of times the scraper will retry fetching a page if it encounters an error.
- `MAX_THREADS`: Defines the maximum number of threads to be used for concurrent scraping.
- `PAGES`: Specifies the number of pages to scrape for each keyword.
- `LOCATION`: Defines the geographic location from which the scraping requests appear to originate.


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `g2_scraper.py`, and run it using:


```bash
python g2_scraper.py
```

---

## Output Format
After the script completes, you will have several CSV files containing the extracted data for each keyword.
 
- **Search Data:** This file stores details of businesses that appear in G2 search results based on the given keyword. (e.g. `keyword.csv`)
- **Business Specific Data:** For each business in the search results, the script fetches its reviews and saves them in a separate CSV file named `business_name.csv`.
