import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions

ser = Service('C://Program Files//Google//Chrome//Application//geckodriver.exe')

option = FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=option)


driver.get("https://www.google.com/")

time.sleep(15)
driver.maximize_window()
print(driver.page_source)


print(driver.current_url)

