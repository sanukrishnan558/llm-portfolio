import requests

API_KEY = "66be079f72757f394b2fd9237e5ca310"
API_URL = f"https://gnews.io/api/v4/top-headlines?lang=en&max=5&token={API_KEY}"

def get_top_news():
    """Fetches top news headlines from GNews API with fallback support."""
    print("🛰️ Fetching news from GNews API...")

    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Debug log
        print("🔍 Raw API response received.")

        articles = data.get("articles", [])
        if not articles:
            raise ValueError("No articles found in API response.")

        headlines = [{"title": article["title"], "url": article["url"]} for article in articles]
        print("✅ Fetched live news successfully!\n")
        return headlines

    except Exception as e:
        print(f"❌ Failed to fetch from GNews. Reason: {e}\n")
        return get_fallback_headlines()


def get_fallback_headlines():
    """Returns fallback headlines in case of API failure."""
    return [
        {"title": "Fallback news 1", "url": "https://example.com/news1"},
        {"title": "Fallback news 2", "url": "https://example.com/news2"},
        {"title": "Fallback news 3", "url": "https://example.com/news3"},
        {"title": "Fallback news 4", "url": "https://example.com/news4"},
        {"title": "Fallback news 5", "url": "https://example.com/news5"},
    ]


if __name__ == "__main__":
    headlines = get_top_news()
    print("📰 Top Headlines:")
    for idx, h in enumerate(headlines, start=1):
        print(f"{idx}. {h['title']} ({h['url']})")
