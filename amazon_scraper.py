from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # NO manual path needed; WebDriverManager handles it
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def scrape_amazon_soft_toys():
    driver = setup_driver()

    search_url = "https://www.amazon.in/s?k=soft+toys"
    driver.get(search_url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@data-component-type, 's-search-result')]"))
    )
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    products = driver.find_elements(By.XPATH, "//div[contains(@data-component-type, 's-search-result')]")
    print(f"Found {len(products)} products.")

    all_data = []
    sponsored_data = []

    for product in products:
        try:
            title = product.find_element(By.XPATH, ".//h2/span").text
            url = product.find_element(By.XPATH, ".//h2/ancestor::a").get_attribute("href")
            image_url = product.find_element(By.XPATH, ".//img").get_attribute("src")
        except:
            continue  # Essential data missing

        # Optional data
        try: price = product.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
        except: price = None
        try: rating = product.find_element(By.XPATH, ".//span[@class='a-icon-alt']").text
        except: rating = None
        try: reviews = product.find_element(By.XPATH, ".//span[contains(@aria-label, 'ratings') or contains(text(), 'ratings')]").text
        except: reviews = None
        try: badge = product.find_element(By.XPATH, ".//span[contains(@class,'a-badge-label-inner')]").text
        except: badge = None
        try:
            product.find_element(By.XPATH, ".//span[.='Sponsored']")
            sponsored = True
        except:
            sponsored = False

        product_data = {
            "Title": title,
            "URL": url,
            "Image URL": image_url,
            "Price": price,
            "Rating": rating,
            "Reviews": reviews,
            "Badge": badge,
            "Sponsored": sponsored
        }

        all_data.append(product_data)
        if sponsored:
            sponsored_data.append(product_data)

    driver.quit()

    df_all = pd.DataFrame(all_data)
    df_sponsored = pd.DataFrame(sponsored_data)

    print(f"\n✅ Total products extracted: {len(df_all)}")
    print(f"⭐ Sponsored products: {len(df_sponsored)}")
    return df_all, df_sponsored


# Run
if __name__ == "__main__":
    df_all, df_sponsored = scrape_amazon_soft_toys()
    print(df_all.head())
