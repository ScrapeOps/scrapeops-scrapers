# LinkedIn Jobs Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [LinkedIn](https://www.linkedin.com/) Jobs.

It is designed for **educational purposes** and demonstrates how to scrape data from LinkedIn Jobs while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape LinkedIn Jobs With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-linkedin-jobs/)

---

## Features  

This scraper extracts the following data from LinkedIn:


✅ Search Data - Data extracted from the LinkedIn Job Listings:


| Field Name  | Description                              |
|------------|----------------------------------|
| name       | Name of the company posting the job  |
| job_title  | Title of the job position       |
| url        | Direct link to the job posting  |
| location   | Location of the job listing     |



✅ Job Post Data - Data extracted from the the individual LinkedIn Job Posts:

| Field Name      | Description                                              |
|----------------|----------------------------------------------------------|
| name           | Name of the company posting the job                      |
| seniority      | Seniority level required for the job (e.g., Entry-level, Mid-senior level, etc.) |
| position_type  | Employment type (e.g., Full-time, Part-time, Contract, etc.) |
| job_function   | Job category or primary role (e.g., Engineering, Marketing, Sales, etc.) |
| industry       | Industry in which the job belongs (e.g., Technology, Healthcare, Finance, etc.) |



---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following LinkedIn's terms of service.

Although our scraping job here was completely legal, we definitely violated LinkedIn's terms of service and robots.txt.

- You can view LinkedIn's terms [here](https://www.linkedin.com/legal/user-agreement). 
- Their robots.txt is available [here](https://www.linkedin.com/robots.txt).

It's important to note that LinkedIn has strict terms of service regarding data scraping, and scraping LinkedIn profiles without permission can lead to legal issues, including being banned from the platform.

Always ensure compliance with LinkedIn's policies and consider using official APIs or getting explicit permission for large-scale data extraction.

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

The script scrapes LinkedIn job posts on a list of keywords (names).

You can customize the job posts you want to scrape in the `keyword_list` section of the script.  

For example:

```python
keyword_list = ["software engineer", "data scientist"]
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Defines the maximum number of times the script will attempt to retrieve a webpage if the initial request fails (e.g., due to network issues or rate limiting).
- `MAX_THREADS`: Sets the maximum number of threads that the script will use concurrently during scraping.
- `PAGES`: The number of pages of job listings to scrape for each keyword.
- `LOCATION`: The country code or identifier for the region from which job listings should be scraped (e.g., "us" for the United States).
- `LOCALITY`: The textual representation of the location where the jobs are being scraped (e.g., "United States").


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `linkedin_jobs_scraper.py`, and run it using:


```bash
python linkedin_jobs_scraper.py
```

---

## Output Format
After the script completes, you will have several CSV files containing the extracted data for each keyword.
 
- **Search Data:** For each job title in keyword_list, the script creates a CSV file named: `job-title.csv`
- **Job Specific Data:** After collecting search results, the script will attempt to scrape data about each job posting. 
