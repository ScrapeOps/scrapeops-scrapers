# Google Play Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [Google Play](https://play.google.com/store/).

It is designed for **educational purposes** and demonstrates how to scrape data from Google Play while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape Google Play With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-google-play/)

---

## Features  

This scraper extracts the following data from Google Play:


✅ Search Data - Data extracted from the Google Play search results page for each keyword: 

| Field Name  | Description |
|--------------|-------------|
| **name**     | The name of the app or business found in the search results. |
| **stars**    | The rating of the app, represented as a float. |
| **url**      | The URL link to the app or business page on Google Play Store. |
| **publisher**| The name of the publisher or the developer of the app. |




✅ Review Data - Data extracted from each individual app of Google Play listing:

| Field Name  | Description |
|--------------|-------------|
| **name**     | The name of the reviewer. |
| **date**     | The date when the review was posted. |
| **stars**    | The rating given by the reviewer, represented as an integer (number of stars). |
| **description** | The text content of the review or the description given by the reviewer. |



---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following Google's terms of service.

- You may view Google's terms [here](https://cloud.google.com/maps-platform/terms). 
- Their robots.txt is available [here](https://www.google.com/robots.txt).

Violating these terms could get your Google account suspended or even permanently deleted. Be careful about breaking rules online.

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
The script will scrape Google Play based on a list of keywords (e.g., "crypto"). In the `main` section of the script, you define the search keywords you want to scrape. 

The `keyword_list` contains the keywords you want to search for on the Google Play Store. You can modify this list to include the apps or businesses you want to scrape. You can replace it with any keywords you want to target.



For example:

```python
keyword_list = ["crypto wallet", "web3 wallet"]
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Specifies the number of times the scraper will retry fetching a page if it encounters an error.
- `MAX_THREADS`: Defines the maximum number of threads to be used for concurrent scraping.
- `LOCATION`: Defines the geographic location from which the scraping requests appear to originate.


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `google_play_scraper.py`, and run it using:


```bash
python google_play_scraper.py
```

---

## Output Format
After the script completes, you will have several CSV files containing the extracted data based on search results from Google Play.
 
- **Search Data:** For each keyword, a CSV file will be created and contain details about the apps or businesses that match the keywords you provided. 
- **Review Data:** This file will contain details about the reviews for each app. 
