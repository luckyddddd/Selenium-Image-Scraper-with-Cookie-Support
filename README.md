# Selenium-Image-Scraper-with-Cookie-Support
This Python script uses Selenium to load cookies from a file, and continuously scrape image links from a specified URL. The script saves the scraped image links to a JSON file, ensuring that duplicate images are not stored.

## Features

- **Cookie Loading**: Loads cookies from a JSON file to bypass login or other restrictions.
- **Age Verification**: Automatically clicks the "I am over 18" (or "Yes") button if present.
- **Infinite Scrolling**: Continuously scrolls the page to load new content.
- **Duplicate Avoidance**: Stores image links in a JSON file and avoids saving duplicates.
- **Random Pauses**: Implements random wait times to mimic human browsing behavior.


### Disclaimer
This script is provided for educational purposes only. Please ensure you have the necessary permissions to scrape the target website and that your activities comply with its terms of service.

## Prerequisites

- Python 3.x
- [Selenium](https://www.selenium.dev/)
- Google Chrome
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (Ensure that your ChromeDriver version matches your installed version of Google Chrome)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/luckyddddd/Selenium-Image-Scraper-with-Cookie-Support.git
2. Navigate to the repository directory:
cd selenium-image-scraper

3. Install the required Python packages:
pip install selenium


## Configuration
ChromeDriver Path:
Update the following line in the script with the correct path to your ChromeDriver:
driver_service = Service('/root/chromedriver-linux64/chromedriver')

URL to Scrape:
Set the variable in the script to the URL you wish to scrape.url_to_scrape

Cookies File:
When prompted, enter the path to your cookies JSON file. The cookies file should be in a valid JSON format.

Output File:
The scraped image links are saved to in the script’s directory.mixx.json

Usage
Run the script using Python:
python scraper.py
When prompted, enter the path to your cookies file. The script will then load the cookies, and begin continuously scraping images while updating the file.mixx.json

Troubleshooting
Cookie Loading Issues:
Ensure your cookies file is properly formatted in JSON.

Element Not Found:
The script waits for the "I am over 18" button for 10 seconds. If the button is not found, the script will continue without clicking it.

ChromeDriver Issues:
Verify that your ChromeDriver version is compatible with your version of Google Chrome.

