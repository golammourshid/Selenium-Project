import time
from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import csv
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait

file_path = Service('C://Program Files//Google//Chrome//Application//chromedriver.exe')
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=file_path, options=op)

# driver = webdriver.Firefox(executable_path="F:\Drivers Selenium\geckodriver-v0.30.0-win64\geckodriver.exe")

# driver = webdriver.Ie(executable_path="F:\Drivers Selenium\IEDriverServer_x64_4.0.0\IEDriverServer.exe")
# driver.get("https://www.prothomalo.com/")

driver.get("http://evrstmain/everest-pub/")

file = open('dat.csv', encoding='utf-8')
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
driver.find_element(By.XPATH, "//*[@id='container']/div[1]/div[4]/div/div/div[1]/a[1]").click()

# Registration  Number


driver.implicitly_wait(6)
element_region = driver.find_element(By.NAME, "region")
drp_down_region = Select(element_region)
drp_down_region.select_by_visible_text(rows[0][1])
driver.find_element(By.NAME, 'tmo').send_keys(rows[0][2])
driver.find_element(By.NAME, 'less').send_keys(rows[0][3])
element_alphabet = driver.find_element(By.NAME, "alphabet")
drp_down_alphabet = Select(element_alphabet)
drp_down_alphabet.select_by_visible_text(rows[0][4])
driver.find_element(By.NAME, 'more').send_keys(rows[0][5])
driver.find_element(By.NAME, 'day').send_keys(rows[0][6])
driver.find_element(By.NAME, 'month').send_keys(rows[0][7])
driver.find_element(By.NAME, 'year').send_keys(rows[0][8])

driver.find_element(By.NAME, 'captcha').send_keys(rows[0][9])

driver.find_element(By.XPATH, "//*[@id='start']").click()

# Mobile


driver.implicitly_wait(15)
driver.find_element(By.NAME, 'mobile').send_keys(rows[0][10])
driver.find_element(By.XPATH, "//*[@id='send-sms']").click()

# Verification //*[@id='skip-email']


driver.find_element(By.NAME, 'verificationCode').send_keys(rows[0][9])
driver.find_element(By.XPATH, "//*[@id='verify-mobile-code']").click()

# Email Skip
email = driver.find_elements(By.NAME, "email")
if len(email) > 0:
    driver.find_element(By.XPATH, "//*[@id='skip-email']").click()

''' Dynamic ID
#dynamic_id2 = driver.find_element(By.CSS_SELECTOR, '[id$="-results"]').get_attribute("id")
#print(dynamic_id2)'''

# Vehicle Information


driver.implicitly_wait(15)
driver.find_element(By.NAME, 'manufactureDateYear').send_keys(rows[0][12])

vehicleManufacturerName = driver.find_element(By.NAME, 'vehicleManufacturerName')
vehicleManufacturerName.clear()
vehicleManufacturerName.send_keys(rows[0][14])

vehicleModel = driver.find_element(By.NAME, 'vehicleModel')
vehicleModel.clear()
vehicleModel.send_keys(rows[0][15])

engineModel = driver.find_element(By.NAME, 'engineModel')
engineModel.clear()
engineModel.send_keys(rows[0][16])

engineNumber = driver.find_element(By.NAME, 'engineNumber')
engineNumber.clear()
engineNumber.send_keys(rows[0][17])

chassisNumber = driver.find_element(By.NAME, 'chassisNumber')
chassisNumber.clear()
chassisNumber.send_keys(rows[0][18])

engineDisplacement = driver.find_element(By.NAME, 'engineDisplacement')
engineDisplacement.clear()
engineDisplacement.send_keys(rows[0][21])

element_ownershipType = driver.find_element(By.NAME, "ownershipType")
drp_down_ownershipType = Select(element_ownershipType)
drp_down_ownershipType.select_by_visible_text(rows[0][22])

element_vehicleType = driver.find_element(By.NAME, "vehicleType")
drp_down_vehicleType = Select(element_vehicleType)
drp_down_vehicleType.select_by_visible_text(rows[0][23])

driver.find_element(By.XPATH, "//*[@id='form']/div[2]/a[2]").click()


# Owner Information
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
driver.find_element(By.XPATH, "//*[@id='next-document']/div").click()

# Document Page

# driver.implicitly_wait(15)


# For Remove
'''
while 1:
    driver.implicitly_wait(7)
    try:
        driver.find_element(By.XPATH, "//*[@id='doc-tr']/tr[1]/td[3]/div/div/span").click()
        driver.find_element(By.ID, "alertify-ok").click()
        driver.implicitly_wait(1)
        time.sleep(1)
    except NoSuchElementException:
        print("Have No Element to Remove.")
        break

'''

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

doc_tr = driver.find_elements(By.XPATH, "//*[@id='doc-tr']/tr[5]/td[1]")
if len(doc_tr) > 0:
    already_has_doc.append(doc_tr[0].text)

doc = [driver.find_element(By.XPATH, "//*[@id='doc-type']/option[1]").text,
       driver.find_element(By.XPATH, "//*[@id='doc-type']/option[2]").text,
       driver.find_element(By.XPATH, "//*[@id='doc-type']/option[3]").text,
       driver.find_element(By.XPATH, "//*[@id='doc-type']/option[4]").text,
       driver.find_element(By.XPATH, "//*[@id='doc-type']/option[5]").text]

for i in range(1, 6):
    Select(driver.find_element(By.ID, "doc-type")).select_by_visible_text(doc[i - 1])
    if doc[i - 1] not in already_has_doc:
        time.sleep(1)
        file_path = "D://Antor//Everest//image//pub image//doc" + str(i) + ".jpg"
        driver.find_element(By.ID, "doc-upload").send_keys(file_path)


time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='next-appointment']/div").click()


# Appointment

if click == 1:
    # Biometric Appointment
    driver.find_element(By.XPATH, "//*[@id='bioAppCalendar']/div/div/table/tbody/tr[6]/td[2]/div/div[1]").click()
    driver.find_element(By.ID, "alertify-ok").click()

# Delivery Appointment
driver.find_element(By.XPATH, "//*[@id='deliveryAppCalendar']/div/div/table/tbody/tr[6]/td[5]/div").click()
driver.find_element(By.ID, "alertify-ok").click()

time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='next-confirm']/div").click()

# Submit

driver.find_element(By.XPATH, "//*[@id='update']/div").click()

# Download

driver.find_element(By.XPATH, "//*[@id='download']/div").click()

# print(driver.page_source)
# driver.close()
