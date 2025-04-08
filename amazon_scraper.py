# amazon_scraper.py
from scraper.driver_setup import get_driver
from scraper.fetch_products import fetch_product_elements
from scraper.extract_details import extract_product_data
import pandas as pd

def scrape_amazon_soft_toys():
    driver = get_driver()
    search_url = "https://www.amazon.in/s?k=soft+toys"

    products = fetch_product_elements(driver, search_url)
    print(f"Found {len(products)} products.")

    all_data, sponsored_data = [], []

    for product in products:
        data = extract_product_data(product)
        if data:
            all_data.append(data)
            if data['Sponsored']:
                sponsored_data.append(data)

    driver.quit()
    df_all = pd.DataFrame(all_data)
    df_sponsored = pd.DataFrame(sponsored_data)

    print(f"\n✅ Total products extracted: {len(df_all)}")
    print(f"⭐ Sponsored products: {len(df_sponsored)}")

    return df_all, df_sponsored

if __name__ == "__main__":
    df_all, df_sponsored = scrape_amazon_soft_toys()
    print(df_all.head())
