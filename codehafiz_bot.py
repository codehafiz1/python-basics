import discord
import os
import requests
import random
from dotenv import load_dotenv
from groq import Groq
import sys
sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

GROQ_KEY = os.getenv("GROQ_API_KEY")
grok_client = Groq(api_key=GROQ_KEY)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#AI Function
def ask_ai(question):
    try:
        chat = grok_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role":"system",
                    "content":"You are CodeHafiz Bot! A helpful and friendly assistant. Keep answers short and simple!"
                },
                {
                    "role":"user",
                    "content":question
                }
            ]
        )
        return chat.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {e}"

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
            "!game → Get free game!\n"
            "!ask → Ask AI anything!\n"
            "!joke → Get AI joke!\n"
            "!advice → Get AI advice!\n"
            "!translate → Translate text!\n"
            "!calculate → Solve math!\n"
            "!quiz → Python quiz!"
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
    elif message.content == '!game':
        try:
            response = requests.get("https://www.mmobomb.com/api1/giveaways")
            data = response.json()
            title = data[0]['title']
            keys = data[0]['keys_left']
            link = data[0]['giveaway_url']
            description = data[0]['short_description']
            await message.channel.send(
                f"🎮 Free Game Giveaway!\n"
                f"🎯 {title}\n"
                f"📝 {description}\n"
                f"🔑 Keys Left: {keys}\n"
                f"🔗 {link}"
            )
        except:
            await message.channel.send("❌ Could not get giveaway!")

    # News command
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
    elif message.content.startswith('!ask'):
        question = message.content[5:]
        if question:
            await message.channel.send("🤔 Thinking...")
            response = ask_ai(question)
            await message.channel.send(f"🤖 {response}")
        else:
            await message.channel.send(
                "❌ Please ask something!\n"
                "Example: !ask What is Python?"
            )
    
    elif message.content == '!joke':
        # Get joke from API first
        try:
            response = requests.get(
                "https://official-joke-api.appspot.com/random_joke"
            )
            data = response.json()
            setup = data['setup']
            punchline = data['punchline']
            await message.channel.send(
                f"😂 {setup}\n"
                f"🎯 {punchline}"
            )
        except:
            # If API fails use AI
            joke = ask_ai("Tell me a very funny unique joke!")
            await message.channel.send(f"😂 {joke}")

    elif message.content == '!advice':
        try:
            response = requests.get(
                "https://zenquotes.io/api/random"
            )
            data = response.json()
            quote = data[0]['q']
            author = data[0]['a']
            await message.channel.send(
                f"💡 Motivational Quote:\n\n"
                f"✨ {quote}\n\n"
                f"👤 - {author}"
            )
        except:
            # AI backup
            advice = ask_ai(
                "Give me one powerful motivational quote for a student!"
            )
            await message.channel.send(f"💡 {advice}")

    #Translation command
    elif message.content.startswith('!translate'):
        text = message.content[11:]
        if text:
            await message.channel.send("🌍 Translating...")
            translation = ask_ai(
                f"Translate this text:\n'{text}'\n\n"
                f"Rules:\n"
                f"1. Do NOT repeat original text!\n"
                f"2. Only show translations!\n"
                f"3. Follow this format exactly:\n\n"
                f"🇵🇰 Urdu: (urdu translation only)\n"
                f"🇬🇧 English: (english translation only)"
            )
            await message.channel.send(f"🌍 Translation:\n{translation}")
        else:
            await message.channel.send(
                "❌ Please provide text!\n"
                "Example: !translate Hello how are you"
            )

    # Calculate command
    elif message.content.startswith('!calculate'):
        problem = message.content[11:]
        if problem:
            await message.channel.send("🧮 Calculating...")
            result = ask_ai(
                f"Solve this math problem:\n{problem}\n\n"
                f"Rules:\n"
                f"1. Show solution step by step!\n"
                f"2. Show final answer clearly!\n"
                f"3. Keep it simple and short!"
            )
            await message.channel.send(f"🧮 Solution:\n{result}")
        else:
            await message.channel.send(
                "❌ Please provide a problem!\n"
                "Example: !calculate 5 + 3 * 2\n"
                "Example: !calculate area of circle radius 5"
            )

    # Quiz command
    elif message.content == '!quiz':
        try:
            # Free Python Quiz API!
            response = requests.get(
                "https://opentdb.com/api.php?amount=1&category=18&type=multiple"
            )
            data = response.json()
            question = data['results'][0]
            
            q_text = question['question']
            correct = question['correct_answer']
            incorrect = question['incorrect_answers']
            
            # Mix all options randomly
            options = incorrect + [correct]
            random.shuffle(options)
            
            # Find correct option letter
            labels = ['A', 'B', 'C', 'D']
            correct_label = labels[options.index(correct)]
            
            # Build quiz message
            quiz_text = f"❓ Question:\n{q_text}\n\n"
            for i, option in enumerate(options):
                quiz_text += f"{labels[i]}) {option}\n"
            quiz_text += f"\n✅ Answer: {correct_label}) {correct}"
            
            await message.channel.send(
                f"🎯 Quiz Time!\n\n{quiz_text}"
            )
        except:
            # AI backup
            topic = random.choice(["variables", "loops", 
                                   "functions", "lists"])
            number = random.randint(1, 1000)
            quiz = ask_ai(
                f"Give me unique quiz {number} about {topic}!"
            )
            await message.channel.send(f"🎯 Quiz!\n\n{quiz}")

client.run(TOKEN)
