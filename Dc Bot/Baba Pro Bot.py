import discord
from discord.ext import commands
import random
from bot_logic import *

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('Sa'):
        await message.channel.send("As")
    elif message.content.startswith('Fati'):
        await message.channel.send("Buyrun Benim Bişey Mi Dedin")
    elif message.content.startswith('Enes Batur'):
        await message.channel.send("Efendim")
    elif message.content.startswith('PP'):
        await message.channel.send("https://cdn.discordapp.com/attachments/967828732201041950/1112011288822939668/20230527_163523.jpg")
    elif message.content.startswith('toss'):
        await message.channel.send(toss())
    elif message.content.startswith('emoji'):
        await message.channel.send(gen_emoji())
    elif message.content.startswith('Orkun Işıtmak'):
        await message.channel.send("https://tenor.com/view/orkun-%C4%B1%C5%9F%C4%B1tmak-orkun-isitmak-gif-8480279054209557082")
    elif message.content.startswith('Yok'):
        await message.channel.send("https://tenor.com/view/yok-ghost-rider-ghost-rider-meme-gif-26788994")
    elif message.content.startswith('!komut'):
        await message.channel.send("Komutlarım: Sa,Fati,Enes Batur,PP,toss,emoji,Orkun Iştmak,Yok")
    elif message.content.startswith('ÇALIŞIYOR'):
        await message.channel.send("Ne Sandın")
    else:
        await message.channel.send("")


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')
@cool.command(name='user')
async def _user(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the user is cool.')


bot.run('token girin')