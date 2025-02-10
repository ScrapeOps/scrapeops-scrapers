# Target Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [Target](https://www.target.com/) search results.

It is designed for **educational purposes** and demonstrates how to scrape data from Target while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape Target With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-target/)

---

## Features  

This scraper extracts the following data from Walmart:


✅ Search Data - Data extracted from the Target Search Results:


| **Item**        | **Description**                                                        |
|-----------------|------------------------------------------------------------------------|
| **name**        | Product name, extracted from the product page                          |
| **url**         | URL of the product page                                                |
| **price**       | Price of the product                                                   |
| **rating**      | Product rating, extracted from the product page                        |
| **review_count**| Number of reviews the product has received                              |
| **details**     | Detailed product description, gathered from the product detail section|




✅ Review Data - Data extracted from the the individual Target Product Pages:

| **Item**        | **Description**                                                        |
|-----------------|------------------------------------------------------------------------|
| **reviewer_name**| Name of the reviewer                                                   |
| **review_text** | Text content of the review provided by the reviewer                     |
| **verified**    | Boolean indicating if the review is from a verified purchase            |


---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following Target's terms of service.

- You can view Target's terms [here](https://www.target.com/c/terms-conditions/-/N-4sr7l). 
- Their robots.txt is available [here](https://www.target.com/robots.txt).

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

Each keyword corresponds to a separate search query on the Target website.


You can customize the keywords you want to scrape in the `keyword_list` section of the script.  

For example:

```python
keyword_list = ["laptop"]
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Determines the maximum number of retries the script will attempt if a request fails (e.g., due to a network issue or a non-200 status code).
- `MAX_THREADS`: Defines the number of concurrent threads used during the scraping and processing tasks.
- `PAGES`: Specifies the number of pages to scrape for each keyword. Each page typically contains a set of search results.
- `LOCATION`: Sets the location/country code for the scraping requests. It is passed to the proxy URL to simulate requests coming from a specific region.


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `target_scraper.py`, and run it using:


```bash
python target_scraper.py
```

---

## Output Format
After the script finishes running, it will generate CSV files for each keyword, containing:

- **Search result data** (e.g., laptop.csv)
- **Product reviews data** (e.g., laptop-reviews.csv)
