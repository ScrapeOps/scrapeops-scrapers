# LinkedIn Profiles Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [LinkedIn](https://www.linkedin.com/) Profiles.

It is designed for **educational purposes** and demonstrates how to scrape data from LinkedIn Profiles while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape LinkedIn Profiles With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-linkedin-profiles/)

---

## Features  

This scraper extracts the following data from LinkedIn:


✅ Search Data - Data extracted from the LinkedIn Search Results:


| Field Name     | Description                                       |
|---------------|-------------------------------------------------|
| `name`        | The LinkedIn username extracted from the profile URL. |
| `display_name` | The full name of the person as shown in the search results. |
| `url`         | The LinkedIn profile URL.                          |
| `location`    | The location of the person (e.g., city, country).  |
| `companies`   | The company or companies associated with the person (if available). |




✅ Profile Data - Data extracted from the the individual LinkedIn Profiles:

| Field Name       | Description                                       |
|-----------------|-------------------------------------------------|
| `name`          | The full name of the person.                     |
| `company`       | The company where the person is currently working. |
| `company_profile` | The LinkedIn URL of the company.               |
| `job_title`     | The job title of the person.                     |
| `followers`     | The number of followers the person has on LinkedIn. |


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

The script scrapes LinkedIn profiles based on a list of keywords (names).

You can customize the profiles you want to scrape in the `keyword_list` section of the script.  

For example:

```python
keyword_list = ["bill gates", "elon musk"]
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Specifies the number of times the scraper will retry fetching a page if it encounters an error.
- `MAX_THREADS`: Defines the maximum number of threads to be used for concurrent scraping.
- `PAGES`:Specifies the number of pages to scrape for each keyword.
- `LOCATION`:Defines the geographic location from which the scraping requests appear to originate.


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `linkedin_profile_scraper.py`, and run it using:


```bash
python linkedin_profile_scraper.py
```

---

## Output Format
After the script completes, you will have several CSV files containing the extracted data for each keyword.

- **Search Data:** For each profile found in the search results, the script will save the data (e.g., name, profile_url, location, etc.) to CSV files named after each keyword.
- **Profile Data:** After collecting search results, the script will attempt to scrape data about each profile. (Eg. BillGates.csv)
