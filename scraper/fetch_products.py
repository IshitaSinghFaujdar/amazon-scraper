# scraper/fetch_products.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def fetch_product_elements(driver, search_url):
    driver.get(search_url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@data-component-type, 's-search-result')]"))
    )
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    return driver.find_elements(By.XPATH, "//div[contains(@data-component-type, 's-search-result')]")
