# Walmart Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [Walmart](https://www.walmart.com/) search results.

It is designed for **educational purposes** and demonstrates how to scrape data from Walmart while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape Walmart With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-walmart/)

---

## Features  

This scraper extracts the following data from Walmart:


✅ Product Data - Data extracted from the Walmart Search Results:


| **Item**         | **Description**                                                    |
|------------------|--------------------------------------------------------------------|
| Product Name     | Name of the product listed on Walmart.                             |
| Product URL      | Direct link to the product's page on Walmart (e.g., for reviews).  |
| Product Rating   | Average rating of the product (e.g., 4.5 stars).                  |
| Sponsored Flag   | Indicates if the product is sponsored.                             |
| Price            | Price of the product.                                              |
| Product ID       | Unique identifier for the product.                                 |


✅ Review Data - Data extracted from the the Walmart Product Pages:

| **Item**         | **Description**                                                    |
|------------------|--------------------------------------------------------------------|
| Review Name      | User's nickname or the name they use to write the review.          |
| Author ID        | Unique identifier for the review author.                           |
| Rating           | Rating provided by the reviewer (e.g., 1-5 stars).                |
| Review Date      | Date when the review was submitted.                                |
| Review Text      | Content of the review left by the user.                            |


---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following Walmart's terms of service.

Scraping data from Walmart is generally considered legal (depending on the country you reside in and their individual laws). Public data is almost always considered fair game.

However, when we scrape Walmart, we are subject to both their Terms of Service and their robots.txt. Violating their policies can lead to suspension and even deletion of your account.

- You can view their terms [here](https://www.walmart.com/help/article/walmart-com-terms-of-use/3b75080af40340d6bbd596f116fae5a0?gclsrc=aw.ds&adid=22222222254421687455&wmlspartner=wmtlabs&wl0=&wl1=g&wl2=c&wl3=314095497094&wl4=dsa-574015752130&wl5=9016897&wl6=&wl7=&wl8=&veh=sem&gad_source=1&gclid=Cj0KCQjwzva1BhD3ARIsADQuPnWM1IH4Fp2q1mbcg5hKi-uyOgm9teGz_bL4o449E1D568KME8qMPEYaAsLrEALw_wcB).
- Walmart's robots.txt is available [here](https://corporate.walmart.com/robots.txt).

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
keyword_list = ["laptop", "smartphone"]
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Defines the maximum number of times the script will retry fetching a webpage if a request fails due to issues such as network timeouts or non-200 HTTP responses.
- `MAX_THREADS`: Sets the maximum number of threads that will be used concurrently while scraping.
- `PAGES`: The number of search result pages to scrape for each keyword.
- `LOCATION`: The location or country code where the products or reviews will be scraped from.


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `walmart_scraper.py`, and run it using:


```bash
python walmart_scraper.py
```

---

## Output Format
After the script has finished running, you should see the CSV files with the following structure:

- **For search results**: A CSV file containing product data like product name, URL, rating, price, etc.
- **For reviews**: Separate CSV files for each product containing review details like reviewer name, rating, review text, etc.
