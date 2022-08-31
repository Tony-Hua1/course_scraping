##selenium.__version__

from selenium import webdriver # ver 4.4.3
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests
import re # regular expression

service = Service('/home/tony/Downloads/chromedriver') # ver ChromeDriver 104.0.5112.79
service.start()
driver = webdriver.Remote(service.service_url)

def list_courses(course_title):
    url = "https://www.deanza.edu/schedule/" # De Anza College
    driver.get(url)

    search_box = driver.find_element(By.ID,"tbSearch")
##    search_box.send_keys("Data Abstraction and Structures") # Search for all Data Abstraction and Structures courses
    search_box.send_keys(course_title)
    search_button = driver.find_element(By.CSS_SELECTOR,"button.btn.dark.full")
    search_button.click()
    time.sleep(5) # seconds

    page = driver.execute_script("return document.body.innerHTML;")
    doc = BeautifulSoup(page, "html.parser")
    tbody = doc.tbody
    trs = tbody.contents

    # Print info for each course section
    for tr in trs[1::2]:
        for td in tr.find_all("td"):
            print(td.text)

    ##driver.refresh()
    driver.close() # close tab
    driver.quit() # close browser

list_courses("Data Abstraction and Structures")
