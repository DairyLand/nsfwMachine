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
    print(f"{client.user} has come online")

@client.command()
async def meme(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://meme-api.com/gimme') as r:
            if r.status == 200:
                data = await r.json()
                meme_url = data['url']
                await ctx.send(meme_url)
            else:
                await ctx.send('Failed to fetch meme from the API.')
                
@client.command()
async def cat(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.thecatapi.com/v1/images/search') as r:
            if r.status == 200:
                data = await r.json()
                cat_url = data[0]['url']
                await ctx.send(cat_url)
            else:
                await ctx.send('Failed to fetch cat from the API.')
                
                

       

client.run(bot_token)