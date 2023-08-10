import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import aiohttp

load_dotenv()

# Get the bot token from the environment variable
bot_token = os.getenv("BOT_TOKEN")

# Initialize the bot
intents = discord.Intents.all()
intents.messages = True
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f"coming online {client.user} !")

@client.command()
async def test(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get

client.run(bot_token)

#this is just some very basic code to see if the api is working 