import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')

response = requests.get("https://www.mmobomb.com/api1/giveaways")
data = response.json()

print("🎮 LIVE GAME GIVEAWAYS!")
print("="*40)

for game in data[:5]:
    print(f"🎯 Title:       {game['title']}")
    print(f"🔑 Keys Left:   {game['keys_left']}")
    print(f"📝 Description: {game['short_description']}")
    print(f"🔗 Link:        {game['giveaway_url']}")
    print("-"*40)