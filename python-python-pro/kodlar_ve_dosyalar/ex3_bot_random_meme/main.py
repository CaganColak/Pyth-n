import discord
from discord.ext import commands
import os, random

from kodlar_ve_dosyalar.token import TOKEN

resimler = "./kodlar_ve_dosyalar/resimler"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def mem(ctx):
    resim = random.choice(os.listdir(resimler))
    with open(f'{resimler}/{resim}', 'rb') as file:
        picture = discord.File(file)
 
    await ctx.send(file=picture)

bot.run(TOKEN)