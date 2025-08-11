import requests

API_KEY = "66be079f72757f394b2fd9237e5ca310"

CATEGORIES = {
    "Technology": "technology",
    "Science": "science",
    "World": "world",
    "Business": "business",
    "Entertainment": "entertainment",
    "Health": "health",
    "Sports": "sports"
}

def get_top_news(category):
    print(f"🛰️ Fetching {category} news from GNews API...")
    url = f"https://gnews.io/api/v4/top-headlines?category={CATEGORIES[category]}&lang=en&country=in&max=5&token={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        print("🔍 Raw API response:", data)

        articles = data.get("articles", [])
        if not articles:
            raise ValueError("No articles found.")

        headlines = [
            {
                "title": article["title"],
                "url": article["url"],
                "content": article.get("content", "")  # ✅ include content
            }
            for article in articles
        ]

        print("✅ Fetched live news successfully!\n")
        return headlines

    except Exception as e:
        print(f"❌ Failed to fetch from GNews. Reason: {e}\n")
        return [
            {"title": "Fallback news 1", "url": "https://example.com/news1", "content": ""},
            {"title": "Fallback news 2", "url": "https://example.com/news2", "content": ""},
            {"title": "Fallback news 3", "url": "https://example.com/news3", "content": ""},
            {"title": "Fallback news 4", "url": "https://example.com/news4", "content": ""},
            {"title": "Fallback news 5", "url": "https://example.com/news5", "content": ""},
        ]
