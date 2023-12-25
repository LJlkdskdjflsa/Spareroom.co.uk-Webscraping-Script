from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import os

# 設置郵編列表
postcodes = ["SW1A 1AA", "SW1A 2AA", "SW1A 0PW"]  # 示例郵編，請替換為您的郵編列表


# 檢查是否存在新房源
def check_new_listings(driver, postcode):
    try:
        driver.get("https://www.spareroom.co.uk/flatshare/?search_id=1263074378&")
        # 輸入郵編並搜索
        wait = WebDriverWait(driver, 10)
        search_field = wait.until(
            lambda d: d.find_element(By.XPATH, '//*[@id="search_by_location_field"]')
        )
        search_field.clear()
        search_field.send_keys(postcode)
        driver.find_element(
            By.XPATH, '//*[@id="search_by_location_submit_button"]'
        ).click()

        # 獲取列表結果
        wait.until(lambda d: d.find_element(By.CLASS_NAME, "listing-result"))
        listings = driver.find_elements(By.CLASS_NAME, "listing-result")
        return [
            (
                element.get_attribute("data-listing-id"),
                element.find_element(By.TAG_NAME, "a").get_attribute("href"),
            )
            for element in listings
        ]
    except (NoSuchElementException, TimeoutException):
        print(f"Error occurred while searching for listings in postcode {postcode}.")
        return []


# 初始化WebDriver
driver = webdriver.Chrome()
driver.get("https://www.spareroom.co.uk")

# 接受Cookies
try:
    wait = WebDriverWait(driver, 10)
    wait.until(lambda d: d.find_element(By.ID, "onetrust-accept-btn-handler")).click()
except TimeoutException:
    print("Timeout while waiting for the cookie acceptance button.")

# 用於存儲先前掃描的房源ID
previous_listings = {}

while True:
    for postcode in postcodes:
        new_listings = check_new_listings(driver, postcode)
        new_ids = set(id_ for id_, _ in new_listings)

        # 檢查是否有新的房源
        if postcode not in previous_listings:
            previous_listings[postcode] = new_ids
        else:
            new_houses = new_ids - previous_listings[postcode]
            if new_houses:
                print(f"New listings for postcode {postcode}:")
                for id_ in new_houses:
                    print([href for id__, href in new_listings if id__ == id_][0])
            previous_listings[postcode] = new_ids

    time.sleep(60)  # 每隔一分鐘掃描一次

driver.quit()
