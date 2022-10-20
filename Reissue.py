import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import csv
from selenium.webdriver.common.by import By

file_path = Service('C://Program Files//Google//Chrome//Application//chromedriver.exe')
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=file_path, options=op)

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

# Registration Number
driver.implicitly_wait(5)
Select(driver.find_element(By.NAME, "region")).select_by_visible_text(rows[0][1])
driver.find_element(By.NAME, 'tmo').send_keys(rows[0][2])
driver.find_element(By.NAME, 'less').send_keys(rows[0][3])
Select(driver.find_element(By.NAME, "alphabet")).select_by_visible_text(rows[0][4])
driver.find_element(By.NAME, 'more').send_keys(rows[0][5])
driver.find_element(By.NAME, 'password').send_keys(rows[0][9])
driver.find_element(By.NAME, 'captcha').send_keys(rows[0][9])
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "Login").click()

# Reissue
driver.find_element(By.PARTIAL_LINK_TEXT, "Reissue Number Plate").click()


driver.implicitly_wait(2)
apply = driver.find_elements(By.XPATH, "//*[@id='apply-again']/div")
if len(apply) > 0:
    driver.find_element(By.XPATH, "//*[@id='apply-again']/div").click()
    driver.find_element(By.ID, "alertify-ok").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='next-document']/div").click()


# Document Upload
doc = [driver.find_element(By.XPATH, "//*[@id='doc-type']/option[1]").text,
       driver.find_element(By.XPATH, "//*[@id='doc-type']/option[2]").text,
       driver.find_element(By.XPATH, "//*[@id='doc-type']/option[3]").text]
already_has_doc = []
doc_tr = driver.find_elements(By.XPATH, "//*[@id='doc-tr']/tr[1]/td[1]")
if len(doc_tr) > 0:
    already_has_doc.append(doc_tr[0].text)

doc_tr = driver.find_elements(By.XPATH, "//*[@id='doc-tr']/tr[2]/td[1]")
if len(doc_tr) > 0:
    already_has_doc.append(doc_tr[0].text)

doc_tr = driver.find_elements(By.XPATH, "//*[@id='doc-tr']/tr[3]/td[1]")
if len(doc_tr) > 0:
    already_has_doc.append(doc_tr[0].text)

for i in range(1, 4):
    Select(driver.find_element(By.ID, "doc-type")).select_by_visible_text(doc[i - 1])
    if doc[i - 1] not in already_has_doc:
        time.sleep(1)
        file_path = "D://Antor//Everest//image//Reissue image//doc" + str(i) + ".jpg"
        driver.find_element(By.ID, "doc-upload").send_keys(file_path)
driver.find_element(By.XPATH, "//*[@id='next-appointment']/div").click()


# Submission Appointment
driver.find_element(By.XPATH, "//*[@id='submissionAppCalendar']/div/div/table/tbody/tr[6]/td[5]/div").click()
time.sleep(2)
driver.find_element(By.ID, "alertify-ok").click()
driver.find_element(By.XPATH, '//*[@id="next-confirm"]/div').click()


# Submit
driver.find_element(By.XPATH, '//*[@id="update"]/div').click()

# Download
driver.find_element(By.XPATH, '//*[@id="download"]/div').click()
