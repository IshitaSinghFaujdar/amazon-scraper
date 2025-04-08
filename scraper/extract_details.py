# scraper/extract_details.py
from selenium.webdriver.common.by import By

def extract_product_data(product):
    try:
        title = product.find_element(By.XPATH, ".//h2/span").text
        url = product.find_element(By.XPATH, ".//h2/ancestor::a").get_attribute("href")
        image_url = product.find_element(By.XPATH, ".//img").get_attribute("src")
    except:
        return None  # Skip if essential data is missing

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

    return {
        "Title": title,
        "URL": url,
        "Image URL": image_url,
        "Price": price,
        "Rating": rating,
        "Reviews": reviews,
        "Badge": badge,
        "Sponsored": sponsored
    }
