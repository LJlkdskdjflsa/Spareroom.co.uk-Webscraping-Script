# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException, ElementNotInteractableException
import os
from collections import defaultdict

# %%

# 檢查'old_properties.txt'文件是否存在
def has_script_run():
    return os.path.exists('old_properties.txt')

# 根據文件是否存在，決定調用哪個函數
def set_file():
    if has_script_run():
        return run_firsttime()
    else:
        return keep_running(file_,params)



# %%
# 從文件中讀取參數，並儲存到字典中
parameter_dct = defaultdict(str)

with open('parameters.txt','r') as params:
    for line in params:
        line = line.split('=')
        line = [word.strip() for word in line]
        line = [word.replace("'","") for word in line]
        print(line[0],line[1])
        parameter_dct[line[0]] = line[1]
            

# %%
parameter_dct

# %%
# 函數用於設置郵編並提交搜索
def set_postcode():
    postcode = param_dct['postcode']
    print(postcode)
    try:
        driver.find_element(By.XPATH,'//*[@id="search_by_location_field"]').send_keys(postcode)
        driver.find_element(By.XPATH,'//*[@id="search_by_location_submit_button"]').click()
    except:
        print('Postcode element not found or postocde is incorrect')

# %%
# CHECK IF FILE IS CREATED

# IF NOT CREATED, CALL CREATE FILE

# 
# 函數用於第一次運行時初始化驅動器，搜索Spareroom的所有列表，
# 並按順序保存列表信息到文件，然後等待10分鐘
def run_firstime(url,params):

    # INITALISES DRIVER
    # SEARCHES SPAREROOM FOR ALL LISTINGS
    # SAVE LISTINGS IN ORDER AND SAVES TO FILE
    # THEN WAITED 10 MINS
    # RUNS keep_running SCRIPT


    driver = webdriver.Chrome()
    # open Spare Room 
    url = 'https://www.spareroom.co.uk'
    driver.get(url)
    # Newest Ads URL
    # https://www.spareroom.co.uk/flatshare/index.cgi?&search_id=1263074378&offset=0&sort_by=days_since_placed

    # Accept Cookies
    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda d : driver.find_element(By.ID,'onetrust-accept-btn-handler').is_displayed())
    driver.find_element(By.ID,'onetrust-accept-btn-handler').click()
    # p_code = params['postcode']
    # print('p_code set')

    postcode = parameter_dct['postcode']
    min_price = parameter_dct['min_price']
    max_price = parameter_dct['max_price']

    print('got here',min_price,postcode)


    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda d : driver.find_element(By.XPATH,'//*[@id="search_by_location_field"]').is_displayed())
    driver.find_element(By.XPATH,'//*[@id="search_by_location_field"]').send_keys(postcode)

    # driver.find_element(By.XPATH,'//*[@id="search_by_location_field"]')
    driver.find_element(By.XPATH,'//*[@id="search_by_location_submit_button"]').click()


    # Log in
    # driver.find_element(By.ID,'loginButtonNav').click()
    # driver.find_element(By.XPATH,'//*[@id="loginemail"]').send_keys('tomtfranklin@gmail.com')
    # driver.find_element(By.XPATH,'//*[@id="loginpass"]').send_keys('Spareroom123!')
    # driver.find_element(By.XPATH,'//*[@id="sign-in-button"]').click()

    # SET PARAMETERS

    


    # select = Select(driver.find_element(By.XPATH,'//*[@id="sort_by"]'))
    # select.select_by_value('days_since_placed')

    # listings = driver.find_elements(By.CLASS_NAME,'listing-result')
    # # element = listings[0]
    # arr = []

    # c=0
    # while True:
    #     # print('page ',c)
    #     listings = driver.find_elements(By.CLASS_NAME,'listing-result')
    #     # print('listings found')
    #     try:
    #         next_page_element = driver.find_element(By.ID,'paginationNextPageLink')
    #         # print('next page element found')
    #     except:
    #         # print('this is the break')
    #         break
    #     c1=0
    #     for element in listings:
    #         # print('element ',c1,' is found')
    #         href = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
    #         data_listing_id = element.get_attribute('data-listing-id')
    #         arr.append(tuple([data_listing_id,href]))
    #         c1+=1

    #     next_page_element.click()
    #     c+=1

    # arr.sort()

    
    # with open('old_properties.txt','w') as file_:
    #         for id_,href in arr:
    #             file_.write(id_+',')    
run_firstime('https://www.spareroom.co.uk',[])

# %%
# 檢查是否已經創建了文件
# 如果沒有創建，則調用創建文件的函數

# %%
# 接下來的代碼塊包含了一些使用Selenium進行網頁自動化操作的例子，
# 包括接受Cookies、設置最低和最高價格等

driver = webdriver.Chrome()
# open Spare Room 
url = 'https://www.spareroom.co.uk'
driver.get(url)
# Newest Ads URL
# https://www.spareroom.co.uk/flatshare/index.cgi?&search_id=1263074378&offset=0&sort_by=days_since_placed

# Accept Cookies
wait = WebDriverWait(driver, timeout=2)
wait.until(lambda d : driver.find_element(By.ID,'onetrust-accept-btn-handler').is_displayed())
driver.find_element(By.ID,'onetrust-accept-btn-handler').click()
# # p_code = params['postcode']
# # print('p_code set')

# postcode = parameter_dct['postcode']
# min_price = parameter_dct['min_price']
# max_price = parameter_dct['max_price']

# print('got here',min_price,postcode)


# wait = WebDriverWait(driver, timeout=2)
# wait.until(lambda d : driver.find_element(By.XPATH,'//*[@id="search_by_location_field"]').is_displayed())
# driver.find_element(By.XPATH,'//*[@id="search_by_location_field"]').send_keys(postcode)

# # driver.find_element(By.XPATH,'//*[@id="search_by_location_field"]')
# driver.find_element(By.XPATH,'//*[@id="search_by_location_submit_button"]').click()

# %%
#min price xpath = //*[@id="minRent"]
#max price xpath = //*[@id="maxRent"]
#Apply filters button = //*[@id="searchFilters"]/div/div/div/button

driver.find_element(By.XPATH,'//*[@id="minRent"]').send_keys(parameter_dct['min_price'])
driver.find_element(By.XPATH,'//*[@id="maxRent"]').send_keys(parameter_dct['max_price'])
driver.find_element(By.XPATH,'//*[@id="searchFilters"]/div/div/div/button').click()


# %%
driver.find_element(By)

# %%
# 此部分代碼是用於創建或檢查文件是否存在
# 如果文件不存在，則創建一個新文件並寫入id列表
file_ = 'old_properties.txt'

if os.path.exists(file_):
    return file_
else:
    with open('old_properties.txt','w'):
        for id_ in id_list:
            file.write(id_)

# %%
# 接下來的代碼塊演示了如何使用Selenium進行更複雜的操作，
# 包括登錄Spareroom，設置搜索參數，提取列表信息等
driver = webdriver.Chrome()
# open Spare Room 
driver.get('https://www.spareroom.co.uk/')
# Newest Ads URL
# https://www.spareroom.co.uk/flatshare/index.cgi?&search_id=1263074378&offset=0&sort_by=days_since_placed

# Accept Cookies
wait = WebDriverWait(driver, timeout=2)
wait.until(lambda d : driver.find_element(By.ID,'onetrust-accept-btn-handler').is_displayed())
driver.find_element(By.ID,'onetrust-accept-btn-handler').click()

# Log in
driver.find_element(By.ID,'loginButtonNav').click()
driver.find_element(By.XPATH,'//*[@id="loginemail"]').send_keys('tomtfranklin@gmail.com')
driver.find_element(By.XPATH,'//*[@id="loginpass"]').send_keys('Spareroom123!')
driver.find_element(By.XPATH,'//*[@id="sign-in-button"]').click()

driver.find_element(By.XPATH,'//*[@id="search_by_location_field"]').send_keys('SW25NB')
driver.find_element(By.XPATH,'//*[@id="submitButton"]').click()

select = Select(driver.find_element(By.XPATH,'//*[@id="sort_by"]'))
select.select_by_value('days_since_placed')

listings = driver.find_elements(By.CLASS_NAME,'listing-result')
# element = listings[0]
arr = []
for element in listings:
    href = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
    data_listing_id = element.get_attribute('data-listing-id')
    arr.append(tuple([data_listing_id,href]))



# %%
# 此部分代碼用於創建文件，並檢查文件是否存在
file_ = 'old_properties.txt'

if os.path.exists(file_):
    print(file_)
else:
    with open('old_properties.txt','w') as file_:
        for id_,href in arr:
            file_.write(id_)
            file_.write(',')



# element.find_element(By.CLASS_NAME,'desktop')
# element.get_attribute()
# # element.find_element(By.CLASS_NAME,'desktop')
# print(element.get_attribute('href'))


# %%
def create_file():
    return

def file_exists():
    file = with open('old_properties','w'):


    return 

# %%


# %%
# driver.find_element(By.ID, 'loginemail').send_keys('tomtfranklin@gmail.com')
# driver.find_element(By.ID, 'loginpass').send_keys('Spareroom123!')

driver.find_element(By.ID, 'sign-in-button').click()
# driver.find_element(By.ID, 'sort_by').send_keys('last_updated')
# driver.find_element(By.ID, 'sort_by').click()
//*[@id="maincontent"]/ul/li[1]/article/header[1]/a

# %%
# postcode_input = input('Enter Post Code: ')

# %%
# onetrust-accept-btn-handler
# driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
driver.find_element(By.ID, 'sort_by').click()


# %%
select = Select(driver.find_element(By.ID,'sort_by'))

# select by visible text
# select.select_by_visible_text('')

select.select_by_value('days_since_placed')



# %%
driver.find_element(By.CLASS_NAME, 'listing-result')

# %%
# 調用測試函數，使用Chrome WebDriver運行測試
# import pytest
import time
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_fails(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    driver.find_element(By.ID, "adder").click()

    with pytest.raises(NoSuchElementException):
        driver.find_element(By.ID, 'box0')


def test_sleep(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    driver.find_element(By.ID, "adder").click()

    time.sleep(2)
    added = driver.find_element(By.ID, "box0")

    assert added.get_dom_attribute('class') == "redbox"


def test_implicit(driver):
    driver.implicitly_wait(2)
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    driver.find_element(By.ID, "adder").click()

    added = driver.find_element(By.ID, "box0")

    assert added.get_dom_attribute('class') == "redbox"


def test_explicit(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    revealed = driver.find_element(By.ID, "revealed")
    driver.find_element(By.ID, "reveal").click()

    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda d : revealed.is_displayed())

    revealed.send_keys("Displayed")
    assert revealed.get_property("value") == "Displayed"


def test_explicit_options(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    revealed = driver.find_element(By.ID, "revealed")
    driver.find_element(By.ID, "reveal").click()

    errors = [NoSuchElementException, ElementNotInteractableException]
    wait = WebDriverWait(driver, timeout=2, poll_frequency=.2, ignored_exceptions=errors)
    wait.until(lambda d : revealed.send_keys("Displayed") or True)

    assert revealed.get_property("value") == "Displayed"

# %%
test_sleep(webdriver.Chrome())

# %%
test_explicit(webdriver.Chrome())

# %%



