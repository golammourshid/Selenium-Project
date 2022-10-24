import pandas as pd
import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
#import requests
import datetime
from selenium.webdriver.chrome.options import Options
from collections import OrderedDict

## parameters ############################
# profile = webdriver.FirefoxProfile()
# profile.set_preference("permissions.default.image", 2) # 2 - Block all images



start_year = 2000
end_year = 2020

#set the list of things you wanted to query to source_dict
source_dict = OrderedDict([
('Joplin Globe, The (MO)', [ ' ', "iraq's", "city's", 'park', 'district', 'building', 'street', 'schools', 'fire', 'community', 'officers', 'board', 'students', 'church', 'officer', 'neighborhood', 'hospital', 'union', 'residents', 'project', 'judge', 'son', 'prosecutors', 'business', 'company', 'airport', 'charges', 'workers', 'lot', 'line', 'crime', 'traffic', 'life', 'parents', 'housing', 'teachers', 'transportation', 'budget', 'services', 'death', 'water', 'contract', 'hours', 'attorney', 'meeting', 'cost', 'education', 'call', 'trial', 'station', 'bush', 'iraq', 'war', 'voters',  'administration', 'troops', 'attacks', 'democrats', 'hussein', 'edwards', 'country', 'soldiers', 'campaign', 'washington', 'world', 'weapons', 'forces', 'army', 'congress', 'baghdad', 'intelligence', 'saddam', 'bill', 'jobs', 'issues', 'policy', 'defense', 'force', 'economy', 'terrorism', 'attack', 'convention', 'tax', 'america', 'nations', 'secretary', 'leaders', 'dean', 'air', 'qaeda', 'coalition', 'party', 'terrorist', 'candidate', 'vote', 'race', 'republicans', 'issue',  'leader',  'power', 'candidates', 'election', 'korea', 'action', 'debate',  'iraqis', 'threat', 'decision', 'change', 'york', 'justice', 'speech', 'agency', 'vice', 'regime', 'pentagon', 'resolution', 'oil', 'rights', 'control', 'polls', 'countries', 'george', 'cheney', 'research', 'inspectors', 'supporters', 'photo', 'security', 'house', 'officials', 'percent', 'government', 'week', 'department', 'support', 'law', 'illustration', 'report', 'city', 'court', 'health', 'plan', 'council', 'program', 'children', 'center', 'information', 'school', 'director', 'committee', 'police', 'office', 'family', 'university', 'job', 'system', 'chief', 'care', 'spokesman', 'plans', 'service'  ]),
('Tribune-Star, The (Terre Haute, IN)', [ ' ', "iraq's", "city's", 'park', 'district', 'building', 'street', 'schools', 'fire', 'community', 'officers', 'board', 'students', 'church', 'officer', 'neighborhood', 'hospital', 'union', 'residents', 'project', 'judge', 'son', 'prosecutors', 'business', 'company', 'airport', 'charges', 'workers', 'lot', 'line', 'crime', 'traffic', 'life', 'parents', 'housing', 'teachers', 'transportation', 'budget', 'services', 'death', 'water', 'contract', 'hours', 'attorney', 'meeting', 'cost', 'education', 'call', 'trial', 'station', 'bush', 'iraq', 'war', 'voters',  'administration', 'troops', 'attacks', 'democrats', 'hussein', 'edwards', 'country', 'soldiers', 'campaign', 'washington', 'world', 'weapons', 'forces', 'army', 'congress', 'baghdad', 'intelligence', 'saddam', 'bill', 'jobs', 'issues', 'policy', 'defense', 'force', 'economy', 'terrorism', 'attack', 'convention', 'tax', 'america', 'nations', 'secretary', 'leaders', 'dean', 'air', 'qaeda', 'coalition', 'party', 'terrorist', 'candidate', 'vote', 'race', 'republicans', 'issue',  'leader',  'power', 'candidates', 'election', 'korea', 'action', 'debate',  'iraqis', 'threat', 'decision', 'change', 'york', 'justice', 'speech', 'agency', 'vice', 'regime', 'pentagon', 'resolution', 'oil', 'rights', 'control', 'polls', 'countries', 'george', 'cheney', 'research', 'inspectors', 'supporters', 'photo', 'security', 'house', 'officials', 'percent', 'government', 'week', 'department', 'support', 'law', 'illustration', 'report', 'city', 'court', 'health', 'plan', 'council', 'program', 'children', 'center', 'information', 'school', 'director', 'committee', 'police', 'office', 'family', 'university', 'job', 'system', 'chief', 'care', 'spokesman', 'plans', 'service'  ]),
('Herald Bulletin, The (Anderson, IN)', [ ' ', "iraq's", "city's", 'park', 'district', 'building', 'street', 'schools', 'fire', 'community', 'officers', 'board', 'students', 'church', 'officer', 'neighborhood', 'hospital', 'union', 'residents', 'project', 'judge', 'son', 'prosecutors', 'business', 'company', 'airport', 'charges', 'workers', 'lot', 'line', 'crime', 'traffic', 'life', 'parents', 'housing', 'teachers', 'transportation', 'budget', 'services', 'death', 'water', 'contract', 'hours', 'attorney', 'meeting', 'cost', 'education', 'call', 'trial', 'station', 'bush', 'iraq', 'war', 'voters',  'administration', 'troops', 'attacks', 'democrats', 'hussein', 'edwards', 'country', 'soldiers', 'campaign', 'washington', 'world', 'weapons', 'forces', 'army', 'congress', 'baghdad', 'intelligence', 'saddam', 'bill', 'jobs', 'issues', 'policy', 'defense', 'force', 'economy', 'terrorism', 'attack', 'convention', 'tax', 'america', 'nations', 'secretary', 'leaders', 'dean', 'air', 'qaeda', 'coalition', 'party', 'terrorist', 'candidate', 'vote', 'race', 'republicans', 'issue',  'leader',  'power', 'candidates', 'election', 'korea', 'action', 'debate',  'iraqis', 'threat', 'decision', 'change', 'york', 'justice', 'speech', 'agency', 'vice', 'regime', 'pentagon', 'resolution', 'oil', 'rights', 'control', 'polls', 'countries', 'george', 'cheney', 'research', 'inspectors', 'supporters', 'photo', 'security', 'house', 'officials', 'percent', 'government', 'week', 'department', 'support', 'law', 'illustration', 'report', 'city', 'court', 'health', 'plan', 'council', 'program', 'children', 'center', 'information', 'school', 'director', 'committee', 'police', 'office', 'family', 'university', 'job', 'system', 'chief', 'care', 'spokesman', 'plans', 'service'  ]),
('Traverse City Record-Eagle (MI)', [ ' ', "iraq's", "city's", 'park', 'district', 'building', 'street', 'schools', 'fire', 'community', 'officers', 'board', 'students', 'church', 'officer', 'neighborhood', 'hospital', 'union', 'residents', 'project', 'judge', 'son', 'prosecutors', 'business', 'company', 'airport', 'charges', 'workers', 'lot', 'line', 'crime', 'traffic', 'life', 'parents', 'housing', 'teachers', 'transportation', 'budget', 'services', 'death', 'water', 'contract', 'hours', 'attorney', 'meeting', 'cost', 'education', 'call', 'trial', 'station', 'bush', 'iraq', 'war', 'voters',  'administration', 'troops', 'attacks', 'democrats', 'hussein', 'edwards', 'country', 'soldiers', 'campaign', 'washington', 'world', 'weapons', 'forces', 'army', 'congress', 'baghdad', 'intelligence', 'saddam', 'bill', 'jobs', 'issues', 'policy', 'defense', 'force', 'economy', 'terrorism', 'attack', 'convention', 'tax', 'america', 'nations', 'secretary', 'leaders', 'dean', 'air', 'qaeda', 'coalition', 'party', 'terrorist', 'candidate', 'vote', 'race', 'republicans', 'issue',  'leader',  'power', 'candidates', 'election', 'korea', 'action', 'debate',  'iraqis', 'threat', 'decision', 'change', 'york', 'justice', 'speech', 'agency', 'vice', 'regime', 'pentagon', 'resolution', 'oil', 'rights', 'control', 'polls', 'countries', 'george', 'cheney', 'research', 'inspectors', 'supporters', 'photo', 'security', 'house', 'officials', 'percent', 'government', 'week', 'department', 'support', 'law', 'illustration', 'report', 'city', 'court', 'health', 'plan', 'council', 'program', 'children', 'center', 'information', 'school', 'director', 'committee', 'police', 'office', 'family', 'university', 'job', 'system', 'chief', 'care', 'spokesman', 'plans', 'service'  ]),
('Hour, The (Norwalk, CT)', [ ' ', "iraq's", "city's", 'park', 'district', 'building', 'street', 'schools', 'fire', 'community', 'officers', 'board', 'students', 'church', 'officer', 'neighborhood', 'hospital', 'union', 'residents', 'project', 'judge', 'son', 'prosecutors', 'business', 'company', 'airport', 'charges', 'workers', 'lot', 'line', 'crime', 'traffic', 'life', 'parents', 'housing', 'teachers', 'transportation', 'budget', 'services', 'death', 'water', 'contract', 'hours', 'attorney', 'meeting', 'cost', 'education', 'call', 'trial', 'station', 'bush', 'iraq', 'war', 'voters',  'administration', 'troops', 'attacks', 'democrats', 'hussein', 'edwards', 'country', 'soldiers', 'campaign', 'washington', 'world', 'weapons', 'forces', 'army', 'congress', 'baghdad', 'intelligence', 'saddam', 'bill', 'jobs', 'issues', 'policy', 'defense', 'force', 'economy', 'terrorism', 'attack', 'convention', 'tax', 'america', 'nations', 'secretary', 'leaders', 'dean', 'air', 'qaeda', 'coalition', 'party', 'terrorist', 'candidate', 'vote', 'race', 'republicans', 'issue',  'leader',  'power', 'candidates', 'election', 'korea', 'action', 'debate',  'iraqis', 'threat', 'decision', 'change', 'york', 'justice', 'speech', 'agency', 'vice', 'regime', 'pentagon', 'resolution', 'oil', 'rights', 'control', 'polls', 'countries', 'george', 'cheney', 'research', 'inspectors', 'supporters', 'photo', 'security', 'house', 'officials', 'percent', 'government', 'week', 'department', 'support', 'law', 'illustration', 'report', 'city', 'court', 'health', 'plan', 'council', 'program', 'children', 'center', 'information', 'school', 'director', 'committee', 'police', 'office', 'family', 'university', 'job', 'system', 'chief', 'care', 'spokesman', 'plans', 'service'  ]),
('Daily Record, The (Wooster, OH)', [ ' ', "iraq's", "city's", 'park', 'district', 'building', 'street', 'schools', 'fire', 'community', 'officers', 'board', 'students', 'church', 'officer', 'neighborhood', 'hospital', 'union', 'residents', 'project', 'judge', 'son', 'prosecutors', 'business', 'company', 'airport', 'charges', 'workers', 'lot', 'line', 'crime', 'traffic', 'life', 'parents', 'housing', 'teachers', 'transportation', 'budget', 'services', 'death', 'water', 'contract', 'hours', 'attorney', 'meeting', 'cost', 'education', 'call', 'trial', 'station', 'bush', 'iraq', 'war', 'voters',  'administration', 'troops', 'attacks', 'democrats', 'hussein', 'edwards', 'country', 'soldiers', 'campaign', 'washington', 'world', 'weapons', 'forces', 'army', 'congress', 'baghdad', 'intelligence', 'saddam', 'bill', 'jobs', 'issues', 'policy', 'defense', 'force', 'economy', 'terrorism', 'attack', 'convention', 'tax', 'america', 'nations', 'secretary', 'leaders', 'dean', 'air', 'qaeda', 'coalition', 'party', 'terrorist', 'candidate', 'vote', 'race', 'republicans', 'issue',  'leader',  'power', 'candidates', 'election', 'korea', 'action', 'debate',  'iraqis', 'threat', 'decision', 'change', 'york', 'justice', 'speech', 'agency', 'vice', 'regime', 'pentagon', 'resolution', 'oil', 'rights', 'control', 'polls', 'countries', 'george', 'cheney', 'research', 'inspectors', 'supporters', 'photo', 'security', 'house', 'officials', 'percent', 'government', 'week', 'department', 'support', 'law', 'illustration', 'report', 'city', 'court', 'health', 'plan', 'council', 'program', 'children', 'center', 'information', 'school', 'director', 'committee', 'police', 'office', 'family', 'university', 'job', 'system', 'chief', 'care', 'spokesman', 'plans', 'service'  ])
])
## this code needs to be adapted to scrape all 840 newspapers

    ####start running the scraping script here####

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C://Program Files//Google//Chrome//Application//chromedriver.exe')

driver.set_window_position(0, 0)
driver.set_window_size(1024, 768)
first_key_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/form[1]/table/tbody/tr[2]/td[2]/input"
second_key_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/form[1]/table/tbody/tr[3]/td[2]/input"
third_key_path = "html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/form[1]/table/tbody/tr[4]/td[2]/input"
fourth_key_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/form[1]/table/tbody/tr[5]/td[2]/input[1]"
first_searchwhere_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/form[1]/table/tbody/tr[2]/td[3]/select"
second_searchwhere_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table[1]/tbody/tr/td/form/table[1]/tbody/tr[3]/td[3]/select"
third_searchwhere_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table[1]/tbody/tr/td/form/table[1]/tbody/tr[4]/td[3]/select"
section_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/form[1]/table/tbody/tr[3]/td[3]/select"
button_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/form[1]/table/tbody/tr[5]/td[3]/input"
output_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[1]/span"
new_button_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table[1]/tbody/tr/td/form/table[1]/tbody/tr[3]/td[3]/a"
second_or_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/form[1]/table/tbody/tr[3]/td[1]/select"
third_or_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/form[1]/table/tbody/tr[4]/td[1]/select"
page1_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/div"
page2_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[2]/a"
page3_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[3]/a"
page4_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[4]/a"
page5_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[5]/a"
page6_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[6]/a"
page7_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[7]/a"
page8_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[8]/a"
page9_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[9]/a"
page10_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[10]/a"
page11_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[11]/a"
page12_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[12]/a"
page13_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[13]/a"
page14_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[14]/a"
page15_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[15]/a"
page16_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[16]/a"
page17_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[17]/a"
page18_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[18]/a"
page19_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[19]/a"
page20_path = "/html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[20]/a"

output_frame = pd.DataFrame()

####### run the driver #######################################
driver.get(
    "http://nl.newsbank.com/nl-search/we/Archives?p_product=NewsLibrary&p_action=keyword&p_theme=newslibrary2&p_queryname=4000&s_home=home&s_sources=location&p_clear_search=&s_search_type=keyword&s_place=&d_refprod=NewsLibrary")
driver.find_element("xpath", new_button_path).click()

monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

iii = 0
for src in source_dict:
    iii = iii + 1
print(src)

# start_year = start_year

try:  # j=0: all, j=1: the, j=2:localcheck, j=3: nationalcheck, j=4: wired, j=5: cityname, j=6: statename, j=7: startyear
    j = -1
    for keyword in source_dict[src]:
        start = time.time()
        j = j + 1

        if (j == 0):
            continue;
        if (j == 0):
            boxloc = 'in Lead/First Paragraph'
        else:
            boxloc = 'in All Text'

        # for month in monthList:
        for month in monthList:
            # for year in range(start_year, end_year):
            for year in range(start_year, end_year):

                # dynamic search parameter
                # date_range = "Jan 01 " +  str(year) + " to Jan 01 " + str(year + 1)
                if month == "Jan":
                    date_range = "Jan 01 " + str(year) + " to Feb 01 " + str(year)
                elif month == "Feb":
                    date_range = "Feb 01 " + str(year) + " to Mar 01 " + str(year)
                elif month == "Mar":
                    date_range = "Mar 01 " + str(year) + " to Apr 01 " + str(year)
                elif month == "Apr":
                    date_range = "Apr 01 " + str(year) + " to May 01 " + str(year)
                elif month == "May":
                    date_range = "May 01 " + str(year) + " to Jun 01 " + str(year)
                elif month == "Jun":
                    date_range = "Jun 01 " + str(year) + " to Jul 01 " + str(year)
                elif month == "Jul":
                    date_range = "Jul 01 " + str(year) + " to Aug 01 " + str(year)
                elif month == "Aug":
                    date_range = "Aug 01 " + str(year) + " to Sep 01 " + str(year)
                elif month == "Sep":
                    date_range = "Sep 01 " + str(year) + " to Oct 01 " + str(year)
                elif month == "Oct":
                    date_range = "Oct 01 " + str(year) + " to Nov 01 " + str(year)
                elif month == "Nov":
                    date_range = "Nov 01 " + str(year) + " to Dec 01 " + str(year)
                else:
                    date_range = "Dec 01 " + str(year) + " to Jan 01 " + str(year + 1)

            # add row of data
            output_frame.loc[len(output_frame), 'Paper'] = src
            output_frame.loc[len(output_frame) - 1, 'Year'] = year
            if j == 5:
                output_frame.loc[len(output_frame) - 1, 'Keyword'] = "cityname"
            elif j == 6:
                output_frame.loc[len(output_frame) - 1, 'Keyword'] = "statename"
            elif j == 0:
                output_frame.loc[len(output_frame) - 1, 'Keyword'] = "all"
            elif j == 1:
                output_frame.loc[len(output_frame) - 1, 'Keyword'] = "custom"
            elif j == 2:
                output_frame.loc[len(output_frame) - 1, 'Keyword'] = "local"
            elif j == 3:
                output_frame.loc[len(output_frame) - 1, 'Keyword'] = "national"
            elif j == 4:

                output_frame.loc[len(output_frame) - 1, 'Keyword'] = "wired"
            else:
                output_frame.loc[len(output_frame) - 1, 'Keyword'] = keyword

            output_frame.loc[len(output_frame) - 1, 'Keyword'] = keyword
            # wait until next page loads, 10 is max wait time
            WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xpath", first_key_path))

            # plug in search info
            # driver.find_element("xpath",first_key_path).send_keys("\"" + src + "\"")
            driver.find_element("xpath", first_key_path).send_keys(src)

            driver.find_element("xpath", second_searchwhere_path).send_keys(boxloc)
            driver.find_element("xpath", second_key_path).send_keys(keyword)

            # if j ==5 or j ==6:
            # driver.find_element("xpath",third_or_path).send_keys("NOT")
            # driver.find_element("xpath",third_key_path).send_keys('"local"')
            # driver.find_element("xpath",third_searchwhere_path).send_keys('in Section')
            driver.find_element("xpath", fourth_key_path).send_keys(date_range)
            driver.find_element("xpath", first_searchwhere_path).send_keys("in Source")
            # driver.find_element("xpath",section_path).send_keys("in All Text")
            # time.sleep(6)
            # click the button
            driver.find_element("xpath", button_path).click()

            # wait until next page loads, 10 is max wait time
            # WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xpath",output_path))

            # collect results count. if no results, give it a 0

            # print("testing1111111111111111111")

            try:
                # wait for the result to load
                WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xpath", fourth_key_path))
                WebDriverWait(driver, 1).until(lambda driver: driver.find_element("xpath", output_path))
                output = driver.find_element("xpath", output_path)
                result_count = output.text
                output_frame.loc[len(output_frame) - 1, 'Result_Count'] = result_count
                # print("testing2222222222222")
            except:
                result_count = "Results: 0"
                output_frame.loc[len(output_frame) - 1, 'Result_Count'] = "Results: 0"

            try:
                WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xpath", fourth_key_path))
                WebDriverWait(driver, 1).until(lambda driver: driver.find_element("xpath", page1_path))
                page1 = driver.find_element("xpath", page1_path)
                page1_count = page1.text
                output_frame.loc[len(output_frame) - 1, 'Page1_Count'] = page1_count
            except:
                page1_count = "NA"
                output_frame.loc[len(output_frame) - 1, 'Page1_Count'] = "0"

            try:
                WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xpath", fourth_key_path))
                WebDriverWait(driver, 1).until(lambda driver: driver.find_element("xpath", page2_path))
                page2 = driver.find_element("xpath", page2_path)
                page2_count = page2.text
                output_frame.loc[len(output_frame) - 1, 'Page2_Count'] = page2_count
            except:
                page2_count = "NA"
                output_frame.loc[len(output_frame) - 1, 'Page2_Count'] = "0"

            try:
                WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xpath", fourth_key_path))
                WebDriverWait(driver, 1).until(lambda driver: driver.find_element("xpath", page3_path))
                page3 = driver.find_element("xpath", page3_path)
                page3_count = page3.text
                output_frame.loc[len(output_frame) - 1, 'Page3_Count'] = page3_count
            except:
                page3_count = "NA"
                output_frame.loc[len(output_frame) - 1, 'Page3_Count'] = "0"

            try:
                WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xpath", fourth_key_path))
                WebDriverWait(driver, 1).until(lambda driver: driver.find_element("xpath", page4_path))
                page4 = driver.find_element("xpath", page4_path)
                page4_count = page4.text
                output_frame.loc[len(output_frame) - 1, 'Page4_Count'] = page4_count
            except:
                page4_count = "NA"
                output_frame.loc[len(output_frame) - 1, 'Page4_Count'] = "0"

            try:
                WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xpath", fourth_key_path))
                WebDriverWait(driver, 1).until(lambda driver: driver.find_element("xpath", page5_path))
                page5 = driver.find_element("xpath", page5_path)
                page5_count = page5.text
                output_frame.loc[len(output_frame) - 1, 'Page5_Count'] = page5_count
            except:
                page5_count = "NA"
                output_frame.loc[len(output_frame) - 1, 'Page5_Count'] = "0"

            try:
                WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xpath", fourth_key_path))
                WebDriverWait(driver, 1).until(lambda driver: driver.find_element("xpath", page6_path))
                page6 = driver.find_element("xpath", page6_path)
                page6_count = page6.text
                output_frame.loc[len(output_frame) - 1, 'Page6_Count'] = page6_count
            except:
                page6_count = "NA"
                output_frame.loc[len(output_frame) - 1, 'Page6_Count'] = "0"

            try:
                WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xpath", fourth_key_path))
                WebDriverWait(driver, 1).until(lambda driver: driver.find_element("xpath", page7_path))
                page7 = driver.find_element("xpath", page7_path)
                page7_count = page7.text
                output_frame.loc[len(output_frame) - 1, 'Page7_Count'] = page7_count
            except:
                page7_count = "NA"
                output_frame.loc[len(output_frame) - 1, 'Page7_Count'] = "0"

            try:
                WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xpath", fourth_key_path))
                WebDriverWait(driver, 1).until(lambda driver: driver.find_element("xpath", page8_path))
                page8 = driver.find_element("xpath", page8_path)
                page8_count = page8.text
                output_frame.loc[len(output_frame) - 1, 'Page8_Count'] = page8_count
            except:
                page8_count = "NA"
                output_frame.loc[len(output_frame) - 1, 'Page8_Count'] = "0"

            try:
                WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xpath", fourth_key_path))
                WebDriverWait(driver, 1).until(lambda driver: driver.find_element("xpath", page9_path))
                page9 = driver.find_element("xpath", page9_path)
                page9_count = page9.text
                output_frame.loc[len(output_frame) - 1, 'Page9_Count'] = page9_count
            except:
                page9_count = "NA"
                output_frame.loc[len(output_frame) - 1, 'Page9_Count'] = "0"

            try:
                WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xpath", fourth_key_path))
                WebDriverWait(driver, 1).until(lambda driver: driver.find_element("xpath", page10_path))
                page10 = driver.find_element("xpath", page10_path)
                page10_count = page10.text
                output_frame.loc[len(output_frame) - 1, 'Page10_Count'] = page10_count
            except:
                page10_count = "NA"
                output_frame.loc[len(output_frame) - 1, 'Page10_Count'] = "0"

            try:
                WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xpath", fourth_key_path))
                WebDriverWait(driver, 1).until(lambda driver: driver.find_element("xpath", page11_path))
                page11 = driver.find_element("xpath", page11_path)
                page11_count = page11.text
                output_frame.loc[len(output_frame) - 1, 'Page11_Count'] = page11_count
            except:
                page11_count = "NA"
                output_frame.loc[len(output_frame) - 1, 'Page11_Count'] = "0"

            try:
                WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xpath", fourth_key_path))
                WebDriverWait(driver, 1).until(lambda driver: driver.find_element("xpath", page12_path))
                page12 = driver.find_element("xpath", page12_path)
                page12_count = page12.text
                output_frame.loc[len(output_frame) - 1, 'Page12_Count'] = page12_count
            except:
                page12_count = "NA"
                output_frame.loc[len(output_frame) - 1, 'Page12_Count'] = "0"

            try:
                WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xpath", fourth_key_path))
                WebDriverWait(driver, 1).until(lambda driver: driver.find_element("xpath", page13_path))
                page13 = driver.find_element("xpath", page13_path)
                page13_count = page13.text
                output_frame.loc[len(output_frame) - 1, 'Page13_Count'] = page13_count
            except:
                page13_count = "NA"
                output_frame.loc[len(output_frame) - 1, 'Page13_Count'] = "0"

            try:
                WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xpath", fourth_key_path))
                WebDriverWait(driver, 1).until(lambda driver: driver.find_element("xpath", page14_path))
                page14 = driver.find_element("xpath", page14_path)
                page14_count = page14.text
                output_frame.loc[len(output_frame) - 1, 'Page14_Count'] = page14_count
            except:
                page14_count = "NA"
                output_frame.loc[len(output_frame) - 1, 'Page14_Count'] = "0"

            try:
                WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xpath", fourth_key_path))
                WebDriverWait(driver, 1).until(lambda driver: driver.find_element("xpath", page15_path))
                page15 = driver.find_element("xpath", page15_path)
                page15_count = page15.text
                output_frame.loc[len(output_frame) - 1, 'Page15_Count'] = page15_count
            except:
                page15_count = "NA"
                output_frame.loc[len(output_frame) - 1, 'Page15_Count'] = "0"

            try:
                WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xpath", fourth_key_path))
                WebDriverWait(driver, 1).until(lambda driver: driver.find_element("xpath", page16_path))
                page16 = driver.find_element("xpath", page16_path)
                page16_count = page16.text
                output_frame.loc[len(output_frame) - 1, 'Page16_Count'] = page16_count
            except:
                page16_count = "NA"
                output_frame.loc[len(output_frame) - 1, 'Page16_Count'] = "0"

            try:
                WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xpath", fourth_key_path))
                WebDriverWait(driver, 1).until(lambda driver: driver.find_element("xpath", page17_path))
                page17 = driver.find_element("xpath", page17_path)
                page17_count = page17.text
                output_frame.loc[len(output_frame) - 1, 'Page17_Count'] = page17_count
            except:
                page17_count = "NA"
                output_frame.loc[len(output_frame) - 1, 'Page17_Count'] = "0"

            try:
                WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xpath", fourth_key_path))
                WebDriverWait(driver, 1).until(lambda driver: driver.find_element("xpath", page18_path))
                page18 = driver.find_element("xpath", page18_path)
                page18_count = page18.text
                output_frame.loc[len(output_frame) - 1, 'Page18_Count'] = page18_count
            except:
                page18_count = "NA"
                output_frame.loc[len(output_frame) - 1, 'Page18_Count'] = "0"

            try:
                WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xpath", fourth_key_path))
                WebDriverWait(driver, 1).until(lambda driver: driver.find_element("xpath", page19_path))
                page19 = driver.find_element("xpath", page19_path)
                page19_count = page19.text
                output_frame.loc[len(output_frame) - 1, 'Page19_Count'] = page19_count
            except:
                page19_count = "NA"
                output_frame.loc[len(output_frame) - 1, 'Page19_Count'] = "0"

            try:
                WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xpath", fourth_key_path))
                WebDriverWait(driver, 1).until(lambda driver: driver.find_element("xpath", page20_path))
                page20 = driver.find_element("xpath", page20_path)
                page20_count = page20.text
                output_frame.loc[len(output_frame) - 1, 'Page20_Count'] = page20_count
            except:
                page20_count = "NA"
                output_frame.loc[len(output_frame) - 1, 'Page20_Count'] = "0"

                # print("testing333333333333")

            # print("testing44444444444444")

            print(str(src) + "; " + str(year) + "; " + str(month) + "; " + str(keyword) + "; " + str(
                result_count) + "; " + str(page1_count) + "; " + str(page2_count) + "; " + str(
                page3_count) + "; " + str(page4_count) + "; " + str(page5_count) + "; " + str(page6_count) + "; " + str(
                page7_count) + "; " + str(page8_count) + "; " + str(page9_count) + "; " + str(
                page10_count) + "; " + str(page11_count) + "; " + str(page12_count) + "; " + str(
                page13_count) + "; " + str(page14_count) + "; " + str(page15_count) + "; " + str(
                page16_count) + "; " + str(page17_count) + "; " + str(page18_count) + "; " + str(
                page19_count) + "; " + str(page20_count))
            # clear input fields
            driver.find_element("xpath", first_key_path).clear()
            driver.find_element("xpath", second_key_path).clear()
            driver.find_element("xpath", third_key_path).clear()
            driver.find_element("xpath", fourth_key_path).clear()

            time.sleep(1)
        end = time.time()
        print(end - start)
except:
    driver.get(
        "http://nl.newsbank.com/nl-search/we/Archives?p_product=NewsLibrary&p_action=keyword&p_theme=newslibrary2&p_queryname=4000&s_home=home&s_sources=location&p_clear_search=&s_search_type=keyword&s_place=&d_refprod=NewsLibrary")
    driver.find_element("xpath", new_button_path).click()
    print("no articles found")
    # pass

if (iii % 1 == 0):
    output_frame_temp = output_frame
    output_frame_temp['Result_Count'] = output_frame_temp['Result_Count'].str.split(" ")
    output_frame_temp['Result_Count'] = output_frame_temp['Result_Count'].apply(lambda x: x[len(x) - 1])
    output_frame_temp.to_csv(r'C:\Users\kh3852\Documents/export_output_frame_temp_test.csv', index=False, header=True)
    print("exported " + str(iii) + "th newspaper")

    # time.sleep(1)

    ## first and/or
    # /html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/form[1]/table/tbody/tr[3]/td[1]/select
    # second and/or
    # /html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/form[1]/table/tbody/tr[4]/td[1]/select
    # second "in all text"
    # /html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/form[1]/table/tbody/tr[3]/td[3]/select
    # third of those
    # /html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/form[1]/table/tbody/tr[4]/td[3]/select
    # search button
    # /html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/form[1]/table/tbody/tr[5]/td[3]/input
    # desired output
    # /html/body/div[1]/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[1]/span

driver.quit()

output_frame['Result_Count'] = output_frame['Result_Count'].str.split(" ")
output_frame['Result_Count'] = output_frame['Result_Count'].apply(lambda x: x[len(x) - 1])
# output_frame.loc[output_frame['Keyword'] =="", 'Keyword'] = "allarticles"

output_panel = output_frame.pivot_table(
    values='Result_Count',
    index=['Paper', 'Year'],
    columns='Keyword',
    aggfunc=np.sum)


#do some processing on the output dataframe

output_frame['Result_Count'] = output_frame['Result_Count'].str.split(" ")
output_frame['Result_Count'] = output_frame['Result_Count'].apply(lambda x: x[len(x)-1])
#output_frame.loc[output_frame['Keyword'] =="", 'Keyword'] = "allarticles"
output_panel = output_frame.pivot_table(
        values='Result_Count',
        index=['Paper', 'Year'],
        columns='Keyword',
        aggfunc=np.sum)

#show the output dataframe to check that the scraping is done correctly
output_frame


#export the output dataframe here
output_frame['Result_Count'] = output_frame['Result_Count'].apply(lambda x: x[len(x)-1])
output_frame
output_frame.to_csv (r'C:\Users\kh3852\Documents/export_output_frame.csv', index = False, header=True)


#Alternatively, export the data  in the wide format instead of the long format
output_panel
output_panel.to_csv (r'C:\Users\kh3852\Documents/export_output_panel.csv', index = False, header=True)