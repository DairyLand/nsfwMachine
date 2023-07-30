import os
import discord
import requests

API_URL = "https://meme-api.herokuapp.com/gimme"

# Initialize the bot
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)


# Event: on_ready
def on_ready():
    print(f"We have logged in as {client.user}")


# Event: on_message
def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!meme"):
        # Fetch meme from the API
        try:
            response = requests.get(API_URL)
            data = response.json()
            meme_url = data["url"]
            client.loop.create_task(message.channel.send(meme_url))
        except Exception as e:
            client.loop.create_task(message.channel.send("Sorry, couldn't fetch a meme at the moment."))


# Register events
client.event(on_ready)
client.event(on_message)


# Get the bot token from the environment variable
bot_token = os.environ.get("BOT_TOKEN")

# Run the bot
client.run(bot_token)

