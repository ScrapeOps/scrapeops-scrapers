# SimilarWeb Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [SimilarWeb](https://www.similarweb.com/).

It is designed for **educational purposes** and demonstrates how to scrape data from SimilarWeb while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape SimilarWeb With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-similarweb/)

---

## Features  

This scraper extracts the following data from SimilarWeb:


✅ Search Data - Data extracted from the SimilarWeb Search results: 

| Field Name        | Description                                                   |
|-------------------|---------------------------------------------------------------|
| `name`            | The name of the website                                       |
| `url`             | The URL of the website                                        |
| `rank`            | The rank of the website in its category                       |
| `rank_change`     | The change in the website's rank (positive or negative)       |
| `average_visit`   | The average duration of visits to the website                 |
| `pages_per_visit` | The number of pages visited per session                       |
| `bounce_rate`     | The bounce rate of the website                                |





✅ Competitor Data - Data extracted about the competitor websites scraped from search results:

| Field Name        | Description                                                   |
|-------------------|---------------------------------------------------------------|
| `name`            | The name of a competitor website                              |
| `url`             | The URL of the competitor website                             |
| `affinity`        | The level of affinity the competitor has with the audience    |
| `monthly_visits`  | The estimated monthly visits to the competitor website        |
| `category`        | The category under which the competitor falls                 |
| `category_rank`   | The rank of the competitor within its category                |





---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following SimilarWeb's terms of service.

- You may view SimilarWeb's terms [here](https://www.similarweb.com/corp/legal/terms/). 
- Their robots.txt is available [here](https://www.similarweb.com/robots.txt).

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
The script will scrape SimilarWeb based on a list of keywords. 

These keywords should have **a category** and **subcategory** (e.g., `{"category": "arts-and-entertainment", "subcategory": "humor"}`).

In the `main` section of the script, there is a predefined list of keywords (`keyword_list`). You can modify this list to add or change keywords based on the websites you want to scrape.

For example:

```python
keyword_list = [{"category": "arts-and-entertainment", "subcategory": "humor"}, {"category": "arts-and-entertainment", "subcategory": "animation-and-comics"}]
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Specifies the number of times the scraper will retry fetching a page if it encounters an error.
- `MAX_THREADS`: Defines the maximum number of threads to be used for concurrent scraping.
- `PAGES`: Specifies the number of pages to scrape for each keyword.
- `LOCATION`: Defines the geographic location from which the scraping requests appear to originate.


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `similarweb_scraper.py`, and run it using:


```bash
python similarweb_scraper.py
```

---

## Output Format
After the script completes, you will have several CSV files containing the extracted data for each keyword.
 
- **Search Data:** Information about the search traffic of websites within a specific category. These files are named after the categories you're scraping, such as `arts-and-entertainment.csv`, and each file contains the data for that specific category or subcategory.
- **Competitor Data:** Information about competitor websites within the same category. 