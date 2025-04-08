

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def brand_performance_analysis(df: pd.DataFrame):
    # Drop rows with missing brand or rating
    df = df.dropna(subset=['Brand', 'Rating'])

    # Brand frequency
    brand_counts = df['Brand'].value_counts().head(5)

    # Average rating by brand
    avg_ratings = df.groupby('Brand')['Rating'].mean().sort_values(ascending=False).head(5)

    # Plot Top 5 Brands by Frequency
    plt.figure(figsize=(8, 5))
    sns.barplot(x=brand_counts.values, y=brand_counts.index, palette="Blues_d")
    plt.title("Top 5 Brands by Frequency")
    plt.xlabel("Count")
    plt.ylabel("Brand")
    plt.tight_layout()
    plt.savefig("data/top_brands_frequency.png")
    plt.close()

    # Pie chart of top brands
    plt.figure(figsize=(6, 6))
    brand_counts.plot.pie(autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title("Top Brands Share (Pie Chart)")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("data/top_brands_pie.png")
    plt.close()
    
    print(df['Brand'].value_counts())
    print(df[['Brand', 'Rating']].dropna().groupby('Brand').mean().sort_values(by='Rating', ascending=False))

    # Plot Top 5 Brands by Average Rating
    plt.figure(figsize=(8, 5))
    sns.barplot(x=avg_ratings.values, y=avg_ratings.index, palette="Greens_d")
    plt.title("Top 5 Brands by Average Rating")
    plt.xlabel("Average Rating")
    plt.ylabel("Brand")
    plt.tight_layout()
    plt.savefig("data/top_brands_avg_rating.png")
    plt.close()
