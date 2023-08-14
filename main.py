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


@client.command()
async def catbomb(ctx, num_images: int = 5):
    if num_images > 10:  # Limit the number of images to a reasonable value
        num_images = 10

    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.thecatapi.com/v1/images/search?limit={num_images}') as r:
            if r.status == 200:
                data = await r.json()
                cat_urls = [entry['url'] for entry in data]
                for cat_url in cat_urls:
                    await ctx.send(cat_url)
            else:
                await ctx.send('Failed to fetch cat images from the API.')


@client.command()
async def nuts(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://meme-api.com/gimme/nutscapes') as r:
            if r.status == 200:
                data = await r.json()
                meme_url = data['url']
                await ctx.send(meme_url)
            else:
                await ctx.send('Failed to fetch meme from the API.')

@client.command()
async def joeysgf(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://meme-api.com/gimme/hentai') as r:
            if r.status == 200:
                data = await r.json()
                meme_url = data['url']
                await ctx.send(meme_url)
            else:
                await ctx.send('Failed to fetch meme from the API.')

@client.command()
async def vroom(ctx):
  async with aiohttp.ClientSession() as session:
    async with session.get('https://meme-api.com/gimme/carporn') as r:
      if r.status == 200:
        data = await r.json()
        meme_url = data['url']
        await ctx.send(meme_url)
      else:
        await ctx.send('Failed to fetch meme from the API.') 

@client.command()
async def ow(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://meme-api.com/gimme/overwatch_memes') as r:
            if r.status == 200:
                data = await r.json()
                meme_url = data['url']
                await ctx.send(meme_url)
            else:
                await ctx.send('Failed to fetch meme from the API.')

@client.command()
async def ow34(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://meme-api.com/gimme/overwatch_porn') as r:
            if r.status == 200:
                data = await r.json()
                meme_url = data['url']
                await ctx.send(meme_url)
            else:
                await ctx.send('Failed to fetch meme from the API.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('jordan'):
        await message.channel.send('I\'m 5\'11\\" but that pic makes me look short')


@client.event
async def on_message(message):
    author_emojis = {
        305383856364584960: '🏳️‍🌈', # jordan
        207334685741678598: '💅', # maddie
        444595872190300161: '🏳️‍⚧️', # hunter
        349715601364746251: '♿', #joey
    
        # Add more user IDs and emojis here
    }

    author_id = message.author.id
    if author_id in author_emojis:
        emoji = author_emojis[author_id]
        await message.add_reaction(emoji)

    await client.process_commands(message)
# working?


client.run(bot_token)
