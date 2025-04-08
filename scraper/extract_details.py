
from selenium.webdriver.common.by import By


def extract_product_data(product):
    try:
        title = product.find_element(By.XPATH, ".//h2/span").text
        url = product.find_element(By.XPATH, ".//h2/ancestor::a").get_attribute("href")
        image_url = product.find_element(By.XPATH, ".//img").get_attribute("src")
    except:
        return None  # Essential data missing

    try:
        price = product.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
        price = price.replace(",", "").strip()
    except:
        price = None


    # ✅ Correct Rating Extraction (Final Fix)
    # ✅ Fallback Rating Extraction using aria-label
    try:
        rating_element = product.find_element(By.XPATH, ".//span[contains(@class,'a-icon-alt')]")
        rating_text = rating_element.get_attribute("innerHTML").strip()
        print(f"Rating raw text: {rating_text}")
        rating = float(rating_text.split()[0])
    except Exception as e:
        print(f"Rating not found or failed to parse: {e}")
        rating = None

    # ✅ Correct Reviews Extraction
    try:
        reviews_element = product.find_element(By.XPATH, ".//span[@class='a-size-base s-underline-text']")
        reviews_text = reviews_element.text.replace(",", "").strip()
        print(f"Reviews raw text: {reviews_text}")
        reviews = int(reviews_text)
    except Exception as e:
        print(f"Reviews not found or failed to parse: {e}")
        reviews = None

    try:
        badge = product.find_element(By.XPATH, ".//span[contains(@class,'a-badge-label-inner')]").text
    except:
        badge = None

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
