import time
from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import csv
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
ser = Service('C://Program Files//Google//Chrome//Application//chromedriver.exe')
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://www.linkedin.com/in/ACwAAAVzBa0Be71y51bFNGSRX5BuZRIbg-aI_24")
time.sleep(2)


# driver.find_element(By.XPATH, '//*[@id="main-content"]/div/a').click()
driver.find_element(By.XPATH, '//*[@id="main-content"]/div/form/p/button').click()

with open(r"C:\Users\user\Music\user.txt") as user:
    username = user.read().replace('\n', '')

driver.find_element(By.NAME, 'session_key').send_keys(username)

with open(r"C:\Users\user\Music\pass.txt") as passs:
    password = passs.read().replace('\n', '')
driver.find_element(By.NAME, 'session_password').send_keys(password)

# driver.find_element(By.ID, 'join-form-submit').click()
driver.find_element(By.XPATH, '//*[@id="main-content"]/div/div/div/form/button').click()

driver.maximize_window()
driver.get("https://www.linkedin.com/in/ACwAAAVzBa0Be71y51bFNGSRX5BuZRIbg-aI_24")
print(driver.current_url)

