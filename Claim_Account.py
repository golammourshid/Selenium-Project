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
# file_path = 'C://Program Files//Google//Chrome//Application//chromedriver.exe'
# driver = webdriver.Chrome(file_path)
# driver = webdriver.Firefox(executable_path="F:\Drivers Selenium\geckodriver-v0.30.0-win64\geckodriver.exe")

# driver = webdriver.Ie(executable_path="F:\Drivers Selenium\IEDriverServer_x64_4.0.0\IEDriverServer.exe")
# driver.get("https://www.prothomalo.com/")

driver.get("http://evrstmain/everest-pub/")

file = open('claim_data.csv', encoding='utf-8')
csvreader = csv.reader(file)
# header = []
# header = next(csvreader)
next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
# print(rows[0][0])
# print(driver.title)
# print(driver.current_url)
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "Claim Your Account").click()

# Claim Account
driver.implicitly_wait(5)
Select(driver.find_element(By.NAME, "region")).select_by_visible_text(rows[0][1])
driver.find_element(By.NAME, 'tmo').send_keys(rows[0][2])
driver.find_element(By.NAME, 'less').send_keys(rows[0][3])
Select(driver.find_element(By.NAME, "alphabet")).select_by_visible_text(rows[0][4])
driver.find_element(By.NAME, 'more').send_keys(rows[0][5])

driver.find_element(By.NAME, 'day').send_keys(rows[0][6])
driver.find_element(By.NAME, 'month').send_keys(rows[0][7])
driver.find_element(By.NAME, 'year').send_keys(rows[0][8])

driver.find_element(By.NAME, 'captcha').send_keys(rows[0][9])
time.sleep(2)
driver.find_element(By.ID, "validate").click()

# Send SMS
driver.implicitly_wait(10)
driver.find_element(By.ID, "send-sms").click()

# Verification Code
driver.implicitly_wait(10)
driver.find_element(By.NAME, 'verificationCode').send_keys(rows[0][9])
time.sleep(2)
driver.find_element(By.ID, "verify-code").click()

# Add Password Button
driver.find_element(By.ID, "add-password").click()

# Protect Account
driver.find_element(By.NAME, 'password').send_keys(rows[0][9])
driver.find_element(By.NAME, 'retypePassword').send_keys(rows[0][9])
driver.find_element(By.ID, "update-password").click()

# Email Skip
driver.find_element(By.ID, "skip").click()
time.sleep(10000)
