import time
import xlutils
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import csv
from selenium.webdriver.common.by import By

file_path = Service('C://Program Files//Google//Chrome//Application//chromedriver.exe')
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=file_path, options=op)

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


# Ownership Transfer
driver.find_element(By.PARTIAL_LINK_TEXT, "Ownership Transfer").click()
time.sleep(2)
driver.implicitly_wait(2)
apply = driver.find_elements(By.XPATH, "//*[@id='apply-again']/div")
if len(apply) > 0:
    apply[0].click()
    driver.find_element(By.ID, "alertify-ok").click()
time.sleep(2)


# Ownership Transfer Information
driver.find_element(By.NAME, 'transferDateDay').send_keys(rows[0][6])
driver.find_element(By.NAME, 'transferDateMonth').send_keys(rows[0][7])
driver.find_element(By.NAME, 'transferDateYear').send_keys(rows[0][8])

driver.implicitly_wait(5)
owner_type_individual = driver.find_element(By.CSS_SELECTOR, "label[for='owner-type-individual']")
owner_type_organization = driver.find_element(By.CSS_SELECTOR, "label[for='owner-type-organization']")
click = 0


def individual_click():
    owner_type_individual.click()
    global click
    click = 1


def organization_click():
    owner_type_organization.click()
    global click
    click = 2


# Click for Individual or Organization

# individual_click()
organization_click()

if click == 1:
    firstName = driver.find_element(By.NAME, 'firstName')
    firstName.clear()
    firstName.send_keys(rows[0][28])

    lastName = driver.find_element(By.NAME, 'lastName')
    lastName.clear()
    lastName.send_keys(rows[0][29])

    driver.find_element(By.NAME, 'citizenshipIssuingDateDay').send_keys(rows[0][31])
    driver.find_element(By.NAME, 'citizenshipIssuingDateMonth').send_keys(rows[0][32])
    driver.find_element(By.NAME, 'citizenshipIssuingDateYear').send_keys(rows[0][33])

    Select(driver.find_element(By.NAME, "citizenshipIssuingDistrict")).select_by_visible_text(rows[0][34])

    citizenshipNumber = driver.find_element(By.NAME, 'citizenshipNumber')
    citizenshipNumber.clear()
    citizenshipNumber.send_keys(rows[0][35])

    address = driver.find_element(By.NAME, 'address')
    address.clear()
    address.send_keys(rows[0][37])

elif click == 2:
    representativeFirstName = driver.find_element(By.NAME, 'representativeFirstName')
    representativeFirstName.clear()
    representativeFirstName.send_keys(rows[0][39])

    representativeLastName = driver.find_element(By.NAME, 'representativeLastName')
    representativeLastName.clear()
    representativeLastName.send_keys(rows[0][40])

    driver.find_element(By.NAME, 'representativeCitizenshipIssuingDateDay').send_keys(rows[0][42])
    driver.find_element(By.NAME, 'representativeCitizenshipIssuingDateMonth').send_keys(rows[0][43])
    driver.find_element(By.NAME, 'representativeCitizenshipIssuingDateYear').send_keys(rows[0][44])

    Select(driver.find_element(By.NAME, "representativeCitizenshipIssuingDistrict")).select_by_visible_text(rows[0][45])

    nameOfOrganization = driver.find_element(By.NAME, 'nameOfOrganization')
    nameOfOrganization.clear()
    nameOfOrganization.send_keys(rows[0][48])

    representativeAddress = driver.find_element(By.NAME, 'representativeAddress')
    representativeAddress.clear()
    representativeAddress.send_keys(rows[0][50])


time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="next-document"]/div').click()


# Document Upload
doc = [driver.find_element(By.XPATH, "//*[@id='doc-type']/option[1]").text,
       driver.find_element(By.XPATH, "//*[@id='doc-type']/option[2]").text,
       driver.find_element(By.XPATH, "//*[@id='doc-type']/option[3]").text,
       driver.find_element(By.XPATH, "//*[@id='doc-type']/option[4]").text]
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

doc_tr = driver.find_elements(By.XPATH, "//*[@id='doc-tr']/tr[4]/td[1]")
if len(doc_tr) > 0:
    already_has_doc.append(doc_tr[0].text)

for i in range(1, 5):
    Select(driver.find_element(By.ID, "doc-type")).select_by_visible_text(doc[i - 1])
    if doc[i - 1] not in already_has_doc:
        time.sleep(1)
        file_path = "D://Antor//Everest//image//Ownerhip Transfer//doc" + str(i) + ".jpg"
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
