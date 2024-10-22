import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import undetected_chromedriver as uc

# Fetch proxies from ProxyScrape
def get_proxies():
    url = 'https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&country=ae,gb,us,ca&proxy_format=protocolipport&format=text&timeout=20000'
    response = requests.get(url)
    proxies = response.text.splitlines()
    return proxies

def create_driver(proxy):
    chrome_options = Options()
    chrome_options.add_argument(f'--proxy-server={proxy}')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-popup-blocking')
    service = Service("path/to/chromedriver")
    driver = uc.Chrome(service=service, options=chrome_options)
    return driver

# Fetch proxy list
proxies = get_proxies()

# Open 10 tabs with different proxies and clear cache/cookies
for i in range(10):
    proxy = proxies[i % len(proxies)]
    driver = create_driver(proxy)
    driver.get('chrome://settings/clearBrowserData')
    time.sleep(2)  # Wait for cache clearing
    driver.get('https://stylexe.shop')  # Replace with your website
    time.sleep(10)  # Wait for 10 seconds
    driver.quit()
    time.sleep(5)  # Short break to avoid rate limits

# Note: Adjust time.sleep durations and other parameters as necessary