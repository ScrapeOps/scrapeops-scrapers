# Quora Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [Quora](https://www.quora.com/).

It is designed for **educational purposes** and demonstrates how to scrape data from Quora while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape Quora With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-quora/)

---

## Features  

This scraper extracts the following data from Quora:


✅ Search Data - Data extracted from the Quora search results page for each keyword: 

| **Field Name**      | **Description**                                                   |
|-------------|---------------------------------------------------------------|
| `name`      | The name or title of the search result (usually the title of a Quora thread). |
| `url`       | The URL of the search result (typically a link to a Quora post). |
| `rank`      | The rank/position of the result on the search results page.    |






✅ Reply Data - Data extracted from each Quora post, specifically the replies to a question:

| **Field Name**      | **Description**                                                   |
|-------------|---------------------------------------------------------------|
| `name`      | The name of the user who posted the reply.                      |
| `reply`     | The content of the reply posted by the user.                    |



---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following Quora's terms of service.

- You may view Quora's terms [here](https://www.quora.com/about/tos). 
- Their robots.txt is available [here](https://www.quora.com/robots.txt).

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
  "api_key": "YOUR-SUPER-SECRET-API-KEY"
}
```

3. Replace "Replace "YOUR-SUPER-SECRET-API-KEY" with your actual ScrapeOps API key.




### 3. Configure Product Search Parameters
The script will scrape Quora based on keywords. In the `main` section of the script, you define the search keywords you want to scrape. 

In the `keyword_list` variable, add the keywords you want to scrape data for. This is set as `["learn rust"]` in the script by default, but you can replace it with any keywords you want to target.

For example:

```python
keyword_list = ["learn rust"]
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Specifies the number of times the scraper will retry fetching a page if it encounters an error.
- `MAX_THREADS`: Defines the maximum number of threads to be used for concurrent scraping.
- `PAGES`: Specifies the number of pages to scrape for each keyword.
- `LOCATION`: Defines the geographic location from which the scraping requests appear to originate.


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `quora_scraper.py`, and run it using:


```bash
python quora_scraper.py
```

---

## Output Format
After the script completes, you will have several CSV files containing the extracted data based on search results from Google and replies from Quora pages.
 
- **Search Data:** The search results from Google are parsed, and the details of each search result are saved in a CSV file. Each keyword you input will generate a separate CSV file for search results, named after the keyword (e.g., learn-rust.csv).
- **Reply Data:** The replies data for each Quora URL processed will be saved in its own CSV file, named after the title or name of the question.

