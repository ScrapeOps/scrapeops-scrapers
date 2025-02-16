# Indeed Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [Indeed](https://www.indeed.com/) Jobs.

It is designed for **educational purposes** and demonstrates how to scrape data from LinkedIn Jobs while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape Indeed With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-indeed/)

---

## Features  

This scraper extracts the following data from LinkedIn:


✅ Search Data - Data extracted from the Indeed Job Listings:


| Field Name     | Description                                        |
|----------------|----------------------------------------------------|
| `name`         | The job title.                                    |
| `url`          | The URL link to the individual job post.          |
| `stars`        | The rating or stars associated with the company.  |
| `company_name` | The name of the company offering the job.         |
| `location`     | The job location.                                 |




✅ Job Post Data - Data extracted from the the individual Indeed Job Posts:

| Field Name     | Description                                         |
|----------------|-----------------------------------------------------|
| `name`         | The job title.                                     |
| `salary`       | The salary information for the job.                |
| `description`  | A detailed description of the job.                 |
| `benefits`     | The benefits offered with the job.                 |



---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following Indeed's terms of service.

- You may view Indeed's terms [here](https://ca.indeed.com/legal). 
- Their robots.txt is available [here](https://www.indeed.com/robots.txt).

If your data is gated behind a login, this is generally considered **private data**. When working with private data, you often need to get permission from the site you're scraping and you can be sued for accessing or disseminating private data.

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

The script scrapes Indeed job posts on a list of keywords (names).

You can customize the job posts you want to scrape in the `keyword_list` section of the script.  

For example:

```python
keyword_list = ["software engineer", "data scientist"]
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Defines the maximum number of retries the scraper will attempt if a request fails (e.g., due to a network error or a non-200 HTTP response).
- `MAX_THREADS`: Defines the maximum number of threads that will be used to run the scraper concurrently.
- `PAGES`: Determines the number of search result pages to scrape for each keyword.
- `LOCATION`: Sets the country or region code used in the scraping process.
- `LOCALITY`: Specifies the locality or city used in the search query, which can narrow down the search results to a specific geographical area.


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `indeed_scraper.py`, and run it using:


```bash
python indeed_scraper.py
```

---

## Output Format
After the script completes, you will have several CSV files containing the extracted data for each keyword.
 
- **Search Data:** For each search result (writer in this case), a CSV file is generated with the job search results. (e.g. writer.csv)
- **Job Specific Data:** For each individual job post, a separate CSV file is generated to store detailed information about that specific job. (e.g. JobTitle.csv)