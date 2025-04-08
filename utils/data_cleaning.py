import pandas as pd
import re

def clean_amazon_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Drop duplicates
    df.drop_duplicates(subset="Title", inplace=True)

    # Clean and convert Price
    df['Price'] = df['Price'].replace('[₹,]', '', regex=True).str.replace(',', '')
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

    # Clean and convert Rating
    if df['Rating'].dtype == 'object':
        df['Rating'] = df['Rating'].str.extract(r'([\d.]+)').astype(float)


    # Clean and convert Reviews
    df['Reviews'] = df['Reviews'].replace(',', '', regex=True)
    df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')

    # Clean Brand
    df['Brand'] = df['Title'].apply(lambda x: x.split()[0] if pd.notnull(x) else None)

    # Handle missing values (you can tweak this)
    df.fillna({'Price': 0, 'Rating': 0, 'Reviews': 0, 'Brand': 'Unknown'}, inplace=True)

    return df
