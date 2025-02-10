# eBay Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [eBay](https://www.ebay.com/) search results.

It is designed for **educational purposes** and demonstrates how to scrape data from eBay while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape eBay With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-ebay/)

---

## Features  

This scraper extracts the following data from Walmart:


✅ Search Data - Data extracted from the eBay Search Results:


| **Item**        | **Description**                                                        |
|-----------------|------------------------------------------------------------------------|
| **name**        | Product name                                                          |
| **url**         | Product URL                                                           |
| **price**       | Product price                                                         |
| **buy_it_now**  | Whether it's listed as a "Buy It Now" option                           |
| **is_auction**  | Whether it's an auction                                                |
| **auction_end** | Auction end time if applicable                                         |



✅ Review Data - Data extracted from the the individual eBay Product Pages:

| **Item**   | **Description**                                      |
|------------|------------------------------------------------------|
| **name**   | The username of the person who left the review.      |
| **comment**| The actual review/comment left by the user.         |
| **verified**| A boolean indicating whether the review was made by a verified purchase. |


---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following eBay's terms of service.

- You can view eBay's terms in full [here](https://www.ebay.com/help/policies/member-behaviour-policies/user-agreement?id=4259).
- You may view their robots.txt [here](https://www.ebay.com/robots.txt).

ScrapeOps take no responsibility for misuse of this code. Ensure you comply with all legal requirements before scraping Walmart.

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

You can customize the keywords you want to scrape in the `keyword_list` section of the script. For example:


For example:

```python
keyword_list = ["gpu", "laptop"]
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Defines the maximum number of times the script will retry fetching a webpage if a request fails due to issues such as network timeouts or non-200 HTTP responses.
- `MAX_THREADS`: Sets the maximum number of threads that will be used concurrently while scraping.
- `PAGES`: The number of search result pages to scrape for each keyword.
- `LOCATION`: The location or country code where the products or reviews will be scraped from.


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `ebay_scraper.py`, and run it using:


```bash
python ebay_scraper.py
```

---

## Output Format
After the script has finished running, you should see the CSV files with the following structure:

- **For search results:** A CSV file containing product data such as product name, description, price, "Buy It Now" status, auction status, and auction end time (if applicable).
- **For reviews:** Separate CSV files for each product containing review details such as reviewer name, review comment, and verified purchase status.