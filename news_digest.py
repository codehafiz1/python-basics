import requests
import json
import datetime
import os
import sys
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

# Get current date
now = datetime.datetime.now()
date = f"{now.day}/{now.month}/{now.year}"

print("📰 TECH NEWS DIGEST!")
print("="*40)
print(f"📅 Date: {date}")
print("="*40)
print("Fetching latest tech news...")

try:
    # News API URL
    url = f"https://newsapi.org/v2/top-headlines?category=technology&language=en&apiKey={API_KEY}"
    
    response = requests.get(url)
    data = response.json()

    # Check if successful
    if data['status'] == 'ok':
        articles = data['articles']
        
        print(f"✅ Found {len(articles)} articles!")
        print("="*40)

        # Show first 5 news
        for i, article in enumerate(articles[:5]):
            print(f"📰 News {i+1}:")
            print(f"📌 Title: {article['title']}")
            print(f"📝 Description: {article['description']}")
            print(f"🔗 Link: {article['url']}")
            print("-"*40)

        # Save to file
        os.makedirs("news_reports", exist_ok=True)
        filename = f"news_reports/tech_news_{now.day}_{now.month}_{now.year}.txt"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write("📰 TECH NEWS DIGEST\n")
            f.write("="*40 + "\n")
            f.write(f"📅 Date: {date}\n")
            f.write("="*40 + "\n")

            for i, article in enumerate(articles[:5]):
                f.write(f"📰 News {i+1}:\n")
                f.write(f"📌 {article['title']}\n")
                f.write(f"📝 {article['description']}\n")
                f.write(f"🔗 {article['url']}\n")
                f.write("-"*40 + "\n")

        print(f"✅ News saved to: {filename}")
        print("🎉 Tech News Digest Complete!")

    else:
        print(f"❌ Error: {data['message']}")

except Exception as e:
    print(f"❌ Error: {e}")