import discord
import os
import requests
from dotenv import load_dotenv
import sys
sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'🤖 CodeHafiz Bot is running!')
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    # Ignore bot's own messages
    if message.author == client.user:
        return

    # Hello command
    if message.content == '!hello':
        await message.channel.send(
            "👋 Assalam O Alaikum!\n"
            "🤖 I am CodeHafiz Bot!\n\n"
            "Commands:\n"
            "!hello → Greeting\n"
            "!weather → Get weather\n"
            "!news → Get tech news\n"
            "!game → Get free game!"
        )

    # Weather command
    elif message.content == '!weather':
        try:
            response = requests.get("https://wttr.in/Bahawalpur?format=j1")
            data = response.json()
            temp = data['current_condition'][0]['temp_C']
            feels = data['current_condition'][0]['FeelsLikeC']
            desc = data['current_condition'][0]['weatherDesc'][0]['value']
            await message.channel.send(
                f"🌤️ Weather in Bahawalpur:\n"
                f"🌡️ Temp: {temp}°C\n"
                f"🌡️ Feels Like: {feels}°C\n"
                f"☁️ {desc}"
            )
        except:
            await message.channel.send("❌ Could not get weather!")

    # Game command
    elif message.content == '!news':
        try:
            API_KEY = os.getenv("NEWS_API_KEY")
            url = f"https://newsapi.org/v2/top-headlines?category=technology&language=en&apiKey={API_KEY}"
            response = requests.get(url)
            data = response.json()

            if data['status'] == 'ok':
                articles = data['articles']
                news_text = "📰 Latest Tech News:\n"
                news_text += "="*30 + "\n"
                
                count = 0
                for article in articles:
                    # Skip if title is None!
                    if article['title'] is None:
                        continue
                    if count >= 3:
                        break
                        
                    news_text += f"\n📌 {article['title']}\n"
                    news_text += f"🔗 {article['url']}\n"
                    news_text += "-"*20 + "\n"
                    count += 1
                
                await message.channel.send(news_text)
            else:
                await message.channel.send("❌ Could not get news!")
        except Exception as e:
            await message.channel.send(f"❌ Error: {e}")
    # News command

client.run(TOKEN)
