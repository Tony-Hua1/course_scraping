##selenium.__version__

from selenium import webdriver # ver 4.4.3
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

##s = Service('/home/tony/Downloads/chromedriver') # ver ChromeDriver 104.0.5112.79
##driver = webdriver.Chrome(service=s)

service = Service('/home/tony/Downloads/chromedriver') # ver ChromeDriver 104.0.5112.79
service.start()
driver = webdriver.Remote(service.service_url)

url = "https://www.deanza.edu/schedule/"
driver.get(url)

##driver.find_element(By.NAME,"tbSearch").send_keys("Data Abstraction and Structures")
search_box = driver.find_element(By.ID,"tbSearch")
search_box.send_keys("Data Abstraction and Structures")
search_button = driver.find_element(By.CSS_SELECTOR,"button.btn.dark.full")
search_button.click()
print(driver.title)
time.sleep(5) # seconds
##driver.close() # close tab
driver.quit() # close browser

##time.sleep(10)
##driver.refresh()
##driver.close()
