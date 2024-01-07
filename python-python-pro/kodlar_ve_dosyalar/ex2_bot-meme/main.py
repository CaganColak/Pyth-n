import discord
from discord.ext import commands

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
    with open(f'{resimler}/m1.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run(TOKEN)