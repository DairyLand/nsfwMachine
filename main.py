import os
from dotenv import load_dotenv
import discord
import requests
import asyncio
load_dotenv

API_URL = "https://meme-api.com/gimme"



# Initialize the bot
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)


# Event: on_ready
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


# Event: on_message
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!meme"):
        # Fetch meme from the API
        try:
            response = requests.get(API_URL)
            data = response.json()
            meme_url = data["url"]
            await message.channel.send(meme_url)
        except Exception as e:
            await message.channel.send("Sorry, couldn't fetch a meme at the moment.")


# Get the bot token from the environment variable
bot_token = os.environ.get("BOT_TOKEN")

# Run the bot
client.run(bot_token)
