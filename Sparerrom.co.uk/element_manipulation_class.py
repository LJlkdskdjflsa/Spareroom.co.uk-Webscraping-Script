
# Class that finds elements and sends keys when necessary

class find_element_:

    def __init__():
        pass

    def set_postcode():

        wait = WebDriverWait(driver, timeout=2)
        wait.until(lambda d : driver.find_element(By.XPATH,'//*[@id="search_by_location_field"]').is_displayed())
        driver.find_element(By.XPATH,'//*[@id="search_by_location_field"]').send_keys(postcode)
