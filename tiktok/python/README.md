# TikTok Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [TikTok](https://www.tiktok.com/).

It is designed for **educational purposes** and demonstrates how to scrape data from TikTok while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape TikTok With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-tiktok/)

---

## Features  

This scraper extracts the following data from TikTok:


✅ Profile Data - Data extracted from the TikTok Profiles of each TikTok channel: 

| **Field Name**      | **Description**                                                   |
|-----------------|------------------------------------------------------------|
| name            | The unique ID of the TikTok channel.                       |
| follower_count  | The total number of followers the channel has.            |
| likes           | The total number of likes the channel's videos have received. |
| video_count     | The total number of videos uploaded by the channel.       |
| nickname        | The nickname used by the user on TikTok.                   |
| verified        | Boolean indicating whether the channel is verified.       |
| signature       | The signature or description text used by the user.       |





✅ Video Data - Data extracted from the each TikTok video linked on the channel's page:

| **Field Name**      | **Description**                                                   |
|-------------|----------------------------------------------------|
| name        | The name/ID of the video (extracted from the video URL). |
| url         | The direct URL to the video on TikTok.             |
| views       | The number of views the video has received.       |



---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following TikTok's terms of service.

We also need to pay attention to both their Terms and Conditions and their robots.txt. Immobilienscout24 explicitly prohibits scraping. We did violate their policies in this scrape for educational purposes.

- You may view TikTok's terms [here](https://www.immoscout24.ch/c/en/about-us/gtc). 
- Their robots.txt is available [here](https://www.immobilienscout24.de/robots.txt).

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
The script will scrape TikTok based on a list of channels. In the `main` section of the script, you define the channels you want to scrape. 

The `channel_list` contains the TikTok handles of the users, which are used to construct the URLs from which profile and video data will be fetched. 

If you want to scrape other channels, you can modify `channel_list` accordingly inside the script:


For example:

```python
channel_list = [
    "user123",       # Example TikTok username 1
    "john_doe",      # Example TikTok username 2
    "cool_tokker",   # Example TikTok username 3
]
```

You can also adjust the following parameters:

- `MAX_RETRIES`: Specifies the number of times the scraper will retry fetching a page if it encounters an error.
- `MAX_THREADS`: Defines the maximum number of threads to be used for concurrent scraping.
- `PAGES`: Specifies the number of pages to scrape for each keyword.
- `LOCATION`: Defines the geographic location from which the scraping requests appear to originate.


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `tiktok_scraper.py`, and run it using:


```bash
python tiktok_scraper.py
```

---

## Output Format
After the script completes, you will have several CSV files containing the extracted data for each keyword.
 
- **Profile Data:** This file contains the profile information of the channels. (Eg. channels.csv)
- **Video View Data:** For each channel, a separate CSV file will be created with the videos' information (name, URL, views) of that channel.

