import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

ser = Service('C://Program Files//Google//Chrome//Application//chromedriver.exe')
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get("https://www.google.com")

time.sleep(2)
driver.maximize_window()
print(driver.page_source)


driver.find_element_by_xpath("//div[text()='Accept']").click() # Accept Cookies
driver.find_element_by_css_selector('input[class="gLFyf gsfi"]').click()
driver.find_element_by_css_selector('input[class="gLFyf gsfi"]').send_keys('some text')
driver.find_element_by_css_selector('input[class="gLFyf gsfi"]').send_keys(Keys.RETURN)

print(driver.current_url)

