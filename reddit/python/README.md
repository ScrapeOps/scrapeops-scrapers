# Reddit Scraper  

This scraper uses [ScrapeOps.io](https://scrapeops.io/) and **Python** proxy service to extract data from [Reddit](reddit.com) search results.

It is designed for **educational purposes** and demonstrates how to scrape data from Reddit while handling **anti-bot protections** effectively.  

📖 **Full tutorial:** [How to Scrape Reddit With Python Requests](https://scrapeops.io/python-web-scraping-playbook/python-scrape-reddit/)

---

## Features  

This scraper extracts the following data from Bing search result pages:

✅ Reddit Post Data - Data extracted from the each Reddit post:


| Item         | Description                                   |
|---------------|-----------------------------------------------|
| `name`        | Title of the Reddit post                      |
| `author`      | Author of the Reddit post                     |
| `permalink`   | URL path to the Reddit post                   |
| `upvote_ratio`| Upvote-to-downvote ratio of the Reddit post   |

✅ Reddit Comment Data - Data extracted from the each comment in the Reddit post:

| Item     | Description                                    |
|-----------|------------------------------------------------|
| `name`    | Author of the comment                          |
| `body`    | The text of the comment                        |
| `upvotes` | The number of upvotes the comment received     |


---

## Fair Use Disclaimer
This scraper is for **educational purposes only**. Web scraping should be done ethically and legally, following Reddit’s terms of service.


You can view Reddit's Terms [here](https://redditinc.com/policies/user-agreement-february-15-2024). You can view their robots.txt [here](https://www.reddit.com/robots.txt). 

**Reddit reserves the right to block, ban, or delete your account if they believe you are responsible for malicious activity.**

ScrapeOps take no responsibility for misuse of this code. Ensure you comply with all legal requirements before scraping Reddit.

---

## Issues & Support
This repository is provided as is with no official support. If you encounter bugs, please open an issue in the Issues tab.

---

## Installation  

### 1. Install Dependencies  
Ensure you have Python installed, then install the required dependencies:  

```bash
pip install requests
```

### 2.  Install ScrapeOps Proxy Service
The script uses the ScrapeOps proxy service for web scraping. You need an API key from ScrapeOps to use the service:

1. Visit [ScrapeOps](https://scrapeops.io/) and sign up for an API key.
2. Replace YOUR-SUPER-SECRET-API-KEY in the script with your actual API key:

```bash
API_KEY = "YOUR-SUPER-SECRET-API-KEY"
```




### 3. Configure Product Search Parameters
In the `main` section of the script, you define the subreddit you want to scrape. 

The script is configured to scrape posts from the news subreddit by default. You can modify the list FEEDS to include other subreddits you'd like to scrape.

For example:

```python
FEEDS = ["news"]
```

You can also adjust the following parameters:

- `MAX_THREADS`:  The number of threads to use for concurrent scraping.
- `LOCATION`: The location/country for search results (e.g., "us" for the United States).
- `BATCH_SIZE`: If you want the top 100 posts instead of 10, change `BATCH_SIZE` to 100.


---

## How to Run the Scraper
Once the script is set up with your API key and product search terms, you can run the script directly from your command line.

Save the script to a file, for example, `reddit_scraper.py`, and run it using:


```bash
python reddit_scraper.py
```

---

## Output Format
After the script has finished running, you should see the following files:

- **Post Data CSV:** A CSV file for each subreddit containing the scraped post data (e.g., news.csv).
- **Comment Data CSV:** For each post, a CSV file containing the scraped comment data (e.g., post-title.csv).