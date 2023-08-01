import os
from dotenv import load_dotenv
import discord
import aiohttp

API_URL = "https://meme-api.herokuapp.com/gimme"

# Load environment variables from .env file
load_dotenv()

# Initialize the bot
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)


# Create an aiohttp session to reuse connections
async def create_session():
    return aiohttp.ClientSession()


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
        # Fetch meme from the API using aiohttp
        try:
            async with create_session() as session:
                async with session.get(API_URL) as response:
                    data = await response.json()
                    meme_url = data["url"]
                    await message.channel.send(meme_url)
        except Exception as e:
            await message.channel.send("Sorry, couldn't fetch a meme at the moment.")


# Get the bot token from the environment variable
bot_token = os.environ.get("BOT_TOKEN")

# Run the bot
client.run(bot_token)
