import os
from dotenv import load_dotenv
import discord
import aiohttp
# i neeed to define intents better and add the discord import for commands
API_URL = "https://meme-api.com/gimme"

# Load environment variables from .env file
load_dotenv()

# Initialize the bot
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)


async with aiohttp.ClientSession() as session:
    async with session.get('https://meme-api.com/gimme') as r:
        if r.status == 200:
            js = await r.json()


# Event: on_ready
@client.event
async def on_ready():
    print(f"fired up and ready {client.user}")


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
                    
                    # Create an embed to send the meme
                    embed = discord.Embed(title="Here's a meme for you!", color=0x00ff00)
                    embed.set_image(url=meme_url)
                    await message.channel.send(embed=embed)
        except Exception as e:
            await message.channel.send("Sorry, couldn't fetch a meme at the moment.")


# Get the bot token from the environment variable
bot_token = os.getenv("BOT_TOKEN")

# Run the bot
client.run(bot_token)

#in the discord.py docs there is a frequently asked question on how to use
# aihttp