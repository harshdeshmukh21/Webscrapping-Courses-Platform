from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from pymongo import MongoClient
import random
import config
import datetime

def scrape_trending_topics():
    proxy_ip = random.choice(config.ips)
    path = "/Users/harshdeshmukh/Downloads/chromedriver-mac-arm64/chromedriver"
    service = Service(path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get('https://talentedge.com/golden-gate-university/doctor-of-business-administration')
    wait = WebDriverWait(driver, 30)

    title_element = driver.find_element(By.XPATH, '//h1[@class="pl-title"]')
    title_text = title_element.text
    print("Title: " + title_text)

    desc = driver.find_element(By.XPATH, '//div[@class="desc_less"]')
    desc_text = desc.text
    print("Description: " + desc_text)

    now = datetime.datetime.now()

    driver.quit()

scraped_data = scrape_trending_topics()