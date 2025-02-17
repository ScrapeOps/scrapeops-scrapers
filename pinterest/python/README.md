# Pinterest Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [Pinterest](https://play.google.com/store/).

It is designed for **educational purposes** and demonstrates how to scrape data from Pinterest while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape Pinterest With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-pinterest/)

---

## Features  

This scraper extracts the following data from Pinterest:


✅ **Search Data** - Data extracted from the Pinterest search results page for each keyword: 

| Field Name | Description |
|------------|-------------|
| name  | Title of the Pinterest pin. |
| url   | Direct URL to the Pinterest pin. |
| image | URL of the pin's image. |


✅ **Pin Data** - Data extracted from each individual Pinterest listing that contains detailed information about a specific Pinterest pin:

| Field Name        | Description |
|------------------|-------------|
| name          | Account name of the Pinterest creator. |
| website       | Website associated with the pin, if available. |
| stars         | Number of rating stars for the pin. |
| follower_count| Number of followers of the creator. |
| image         | URL of the main image in the pin. |




---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following Pinterest's terms of service.

When you access Pinterest, you are subject to their terms of service. On top of that, when you access their site with a bot (in this case a scraper), you are subject to their robots.txt.

- You may view Pinterest's terms [here](https://policy.pinterest.com/en/terms-of-service). 
- Their robots.txt is available [here](https://www.pinterest.com/robots.txt).

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
The script will scrape Pinterest based on a list of keywords (e.g., "grilling"). In the `main` section of the script, you define the search keywords you want to scrape. 

The `keyword_list` contains the keywords you want to search for on the Pinterest. Modify the `keyword_list` in the script with your desired search locations.

For example:

```python
keyword_list = ["grilling"]
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Specifies the number of times the scraper will retry fetching a page if it encounters an error.
- `MAX_THREADS`: Defines the maximum number of threads to be used for concurrent scraping.
- `LOCATION`: Defines the geographic location from which the scraping requests appear to originate.

---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `pinterest_scraper.py`, and run it using:


```bash
python pinterest_scraper.py
```

---

## Output Format
After the script completes, you will have several CSV files containing the extracted data based on search results from Pinterest.

- **Search Data:** For each keyword, a CSV file will be created and stores basic information about Pinterest search results for a given keyword.
- **Review Data:** This file will stores detailed information about each Pinterest post.
