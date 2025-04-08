import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def brand_performance_analysis(df: pd.DataFrame):
    df = df.dropna(subset=['Brand', 'Rating'])
    brand_counts = df['Brand'].value_counts().head(5)
    avg_ratings = df.groupby('Brand')['Rating'].mean().sort_values(ascending=False).head(5)

    plt.figure(figsize=(8, 5))
    sns.barplot(x=brand_counts.values, y=brand_counts.index, palette="Blues_d")
    plt.title("Top 5 Brands by Frequency")
    plt.xlabel("Count")
    plt.ylabel("Brand")
    plt.tight_layout()
    plt.savefig("data/top_brands_frequency.png")
    plt.close()

    plt.figure(figsize=(6, 6))
    brand_counts.plot.pie(autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title("Top Brands Share (Pie Chart)")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("data/top_brands_pie.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.barplot(x=avg_ratings.values, y=avg_ratings.index, palette="Greens_d")
    plt.title("Top 5 Brands by Average Rating")
    plt.xlabel("Average Rating")
    plt.ylabel("Brand")
    plt.tight_layout()
    plt.savefig("data/top_brands_avg_rating.png")
    plt.close()

def price_vs_rating_analysis(df: pd.DataFrame):
    df = df.dropna(subset=['Price', 'Rating'])

    # Scatter plot: Price vs. Rating
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x='Rating', y='Price', hue='Brand', palette='tab10', alpha=0.7)
    plt.title("Price vs. Rating")
    plt.xlabel("Rating")
    plt.ylabel("Price (₹)")
    plt.tight_layout()
    plt.savefig("data/price_vs_rating_scatter.png")
    plt.close()

    # Bar chart: Average Price by Rating Range (e.g., 0–1, 1–2, ..., 4–5)
    df['Rating_Range'] = pd.cut(df['Rating'], bins=[0, 1, 2, 3, 4, 5])
    avg_price_by_rating = df.groupby('Rating_Range')['Price'].mean().reset_index()

    plt.figure(figsize=(8, 5))
    sns.barplot(data=avg_price_by_rating, x='Rating_Range', y='Price', palette='mako')
    plt.title("Average Price by Rating Range")
    plt.xlabel("Rating Range")
    plt.ylabel("Average Price (₹)")
    plt.tight_layout()
    plt.savefig("data/avg_price_by_rating_range.png")
    plt.close()

def review_and_rating_distribution(df: pd.DataFrame):
    df = df.dropna(subset=['Reviews', 'Rating', 'Title'])

    # Top 5 products by reviews
    top_reviews = df.sort_values(by='Reviews', ascending=False).head(5)
    plt.figure(figsize=(8, 5))
    sns.barplot(x=top_reviews['Reviews'], y=top_reviews['Title'], palette='viridis')
    plt.title("Top 5 Products by Number of Reviews")
    plt.xlabel("Reviews")
    plt.ylabel("Product Title")
    plt.tight_layout()
    plt.savefig("data/top_products_by_reviews.png")
    plt.close()

    # Top 5 products by rating
    top_rated = df[df['Reviews'] > 10].sort_values(by='Rating', ascending=False).head(5)  # Ignore low-review ones
    plt.figure(figsize=(8, 5))
    sns.barplot(x=top_rated['Rating'], y=top_rated['Title'], palette='coolwarm')
    plt.title("Top 5 Products by Rating")
    plt.xlabel("Rating")
    plt.ylabel("Product Title")
    plt.tight_layout()
    plt.savefig("data/top_products_by_rating.png")
    plt.close()
