import requests
import datetime
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
print("🤖 Morning Report Generator")
print("="*40)
print("Gathering Your Daily Report...")
print("="*40)
now = datetime.datetime.now()
date = f"{now.day}/{now.month}/{now.year}"
time = f"{now.hour}:{now.minute}:{now.second}"
print(f"📅 Date: {date}")
print(f"⏰ Time: {time}")
print("="*40)
print("🌤️ Getting weather...")
try:
    weather_url = "https://wttr.in/Bahawalpur?format=j1"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    temp = weather_data['current_condition'][0]['temp_C']
    feels_like = weather_data['current_condition'][0]['FeelsLikeC']
    description = weather_data['current_condition'][0]['weatherDesc'][0]['value']
    humidity = weather_data['current_condition'][0]['humidity']
    print(f"🌡️  Temperature: {temp}°C")
    print(f"🌡️  Feels Like: {feels_like}°C")
    print(f"☁️  Weather: {description}")
    print(f"💧 Humidity: {humidity}%")
    print("="*40)
except:
    print("❌ Could not get weather!")
    print("="*40)
print("😄 Getting joke...")
try:
    joke_url = "https://official-joke-api.appspot.com/random_joke"
    joke_response = requests.get(joke_url)
    joke_data = joke_response.json()

    setup = joke_data['setup']
    punchline = joke_data['punchline']

    print(f"😀 Joke: {setup}")
    print(f"😂 Answer: {punchline}")
    print("="*40)
except:
    print("❌ Could not get joke!")
    print("="*40)
print(f"🎮 Getting Game Giveaway...")
try:
    game_url = "https://www.mmobomb.com/api1/giveaways"
    game_response = requests.get(game_url)
    game_data = game_response.json()
    
    title = game_data[0]['title']
    keys_left = game_data[0]['keys_left']
    short_description = game_data[0]['short_description']
    giveaway_url = game_data[0]['giveaway_url']
    
    print(f"🎮 Game: {title}")
    print(f"🔑 Keys Left: {keys_left}")
    print(f"📝 info: {short_description}")
    print(f"🔗 Link: {giveaway_url}")
    print("="*40)
except:
    print("❌ could not get giveaway!")
    print("="*40)
# Save report to text file
print("💾 Saving your report...")
try:
    # Create reports folder
    os.makedirs("reports", exist_ok=True)
    
    # Create filename with today's date
    filename = f"reports/report_{now.day}_{now.month}_{now.year}.txt"
    
    # Write everything to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("🤖 MORNING REPORT\n")
        f.write("="*40 + "\n")
        f.write(f"📅 Date: {date}\n")
        f.write(f"⏰ Time: {time}\n")
        f.write("="*40 + "\n")
        f.write("🌤️ WEATHER\n")
        f.write(f"🌡️ Temperature: {temp}°C\n")
        f.write(f"🌡️ Feels Like: {feels_like}°C\n")
        f.write(f"☁️ Weather: {description}\n")
        f.write(f"💧 Humidity: {humidity}%\n")
        f.write("="*40 + "\n")
        f.write("😄 JOKE OF THE DAY\n")
        f.write(f"😄 {setup}\n")
        f.write(f"😂 {punchline}\n")
        f.write("="*40 + "\n")
        f.write("🎮 GAME GIVEAWAY\n")
        f.write(f"🎮 Game: {title}\n")
        f.write(f"🔑 Keys Left: {keys_left}\n")
        f.write(f"🔗 Link: {giveaway_url}\n")
        f.write("="*40 + "\n")

    print(f"✅ Report saved as: {filename}")
    print("="*40)
    print("🎉 Morning Report Complete!")

except:
    print("❌ Could not save report!")
