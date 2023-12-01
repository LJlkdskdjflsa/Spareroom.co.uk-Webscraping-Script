# IMPORT LIBRARIES
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException, ElementNotInteractableException
import os
from collections import defaultdict
from parameter_dict import Parameters

#====== OPEN WEBBROWSER ==========
driver = webdriver.Chrome()
# open Spare Room 
url = 'https://www.spareroom.co.uk'
driver.get(url)

# Accept Cookies
wait = WebDriverWait(driver, timeout=2)
wait.until(lambda d : driver.find_element(By.ID,'onetrust-accept-btn-handler').is_displayed())
driver.find_element(By.ID,'onetrust-accept-btn-handler').click()

def build_param_dct():
# Define and build parametre dictionary
    parameter_dct = defaultdict(str)

    with open('./parameters.txt','r') as params:
        for line in params:
            line = line.split('=')
            line = [word.strip() for word in line]
            line = [word.replace("'","") for word in line]
            parameter_dct[line[0]] = line[1]
    return parameter_dct



parameter_dct = build_param_dct('parameters.txt').postcode()
postcode = parameter_dct()
min_price = parameter_dct['min_price']
max_price = parameter_dct['max_price']


# driver.find_element(By.XPATH,'//*[@id="search_by_location_submit_button"]').click()

driver.find_element(By.XPATH,'//*[@id="search_by_location_field"]').send_keys('SW2 5NB')
driver.find_element(By.XPATH,'//*[@id="search_by_location_submit_button"]').click()

try:
    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda d : driver.find_element(By.XPATH,'//*[@id="reg_close"]').is_displayed())
    driver.find_element(By.XPATH,'//*[@id="reg_close"]').click()
    driver.find_element(By.XPATH,'//*[@id="reg_close"]').click()
except:
    pass


# ===== SEARCH THROUGH LISTINGS AND ADD TO ARRAY ============
arr = []

c=0
while True:
    print('page ',c)
    listings = driver.find_elements(By.CLASS_NAME,'listing-result')
    c1=0
    for element in listings:
        # href = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
        data_listing_id = element.get_attribute('data-listing-id')
        arr.append(tuple([data_listing_id]))
        c1+=1
    try:
        next_page_element = driver.find_element(By.ID,'paginationNextPageLink')
    except:
        break
    next_page_element.click()
    c+=1

arr.sort()


#========== IF THE FILE ISNT FOUND (FIRST ITTREATION), ADD ALL LISTING IDS TO A FILE
# IF A FILE IS THERE (SECOND ITTERATION) LOAD OLD LISTINGS INTO A SECONDAY ARRAY, THEN 
# CROSS CHECK WITH ARR1 FOR NEW LISTINGS ==============
if not os.path.isfile('test.txt'):
    with open('test.txt','w') as testfile:
        for listing in arr:
            testfile.write(str(listing)+',')
else:
    print('HERE')
    array2 = []
    with open('test.txt','r') as file_:
        for line in file_:
            print(line)
            array2.append(line)

    


print(array2)
# Log in
# driver.find_element(By.ID,'loginButtonNav').click()
# driver.find_element(By.XPATH,'//*[@id="loginemail"]').send_keys('tomtfranklin@gmail.com')
# driver.find_element(By.XPATH,'//*[@id="loginpass"]').send_keys('Spareroom123!')
# driver.find_element(By.XPATH,'//*[@id="sign-in-button"]').click()


