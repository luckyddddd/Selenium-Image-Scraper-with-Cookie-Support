from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import json
import time
import random

def load_cookies_and_scrape(url, cookies_path):
    """Loads cookies and continuously scrapes images."""
    # Selenium setup
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run without GUI
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
    
    driver_service = Service('/root/chromedriver-linux64/chromedriver')  # Specify your ChromeDriver path
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)
    driver.get(url)
    time.sleep(5)  # Wait for the page to load

    # Load cookies from file
    try:
        with open(cookies_path, "r") as f:
            cookies = json.load(f)
            for cookie in cookies:
                driver.add_cookie(cookie)

        driver.refresh()  # Refresh the page to apply cookies
        print("✅ Cookies loaded!")
    except Exception as e:
        print(f"❌ Error loading cookies: {e}")


    # File for saving image links
    output_file = "mixx.json"
    img_links = set()

    # Load already saved images to avoid duplicates
    try:
        with open(output_file, "r") as f:
            img_links.update(json.load(f))
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    print("📸 Starting continuous image scraping...")

    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    same_scroll_count = 0  # Number of consecutive scrolls with no change in height

    try:
        while True:
            # Scroll down
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(random.uniform(3, 6))  # Random pause

            # Force lazy images to load by dispatching a scroll event
            driver.execute_script("window.dispatchEvent(new Event('scroll'));")

            # Check for new content by comparing the scroll height
            new_height = driver.execute_script("return document.documentElement.scrollHeight")
            if new_height == last_height:
                same_scroll_count += 1
                if same_scroll_count >= 5:  # If height hasn't changed for 5 consecutive scrolls, refresh the page
                    print("🔄 Refreshing the page...")
                    driver.refresh()
                    time.sleep(5)
                    same_scroll_count = 0
                continue
            else:
                same_scroll_count = 0
                last_height = new_height

            # Collect images
            images = driver.execute_script("""
                return Array.from(document.querySelectorAll('.vertical-view__media, img'))
                    .map(img => img.src || img.getAttribute('srcset'))
                    .filter(src => src !== null);
            """)

            new_images = [img_url for img_url in images if img_url not in img_links]

            if new_images:
                img_links.update(new_images)
                print(f"📷 New images found: {len(new_images)}")

                with open(output_file, "w") as f:
                    json.dump(list(img_links), f, indent=4)

                print(f"✅ Total images saved: {len(img_links)}")

    except Exception as e:
        print(f"❌ Error during scraping: {e}")
    finally:
        driver.quit()

# 🔹 Example usage
url_to_scrape = ""
cookies_path = input("Enter the path to the cookies file: ")  # Allows the user to choose a file
load_cookies_and_scrape(url_to_scrape, cookies_path)
