import discord

from eski.parola import *
from bot_mantik import *
# token
token = ""
token2 = ""
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == '$hi':
        await message.channel.send("Hello!😎")
    
    elif message.content == '$bye':
        await message.channel.send("see you🐱‍👤")
    
    elif message.content == '$pass':
        parola_uzunlugu = 10  # Set the desired password length
        generated_password = sifre_olusturucu(parola_uzunlugu)
        await message.channel.send(generated_password)
    elif message.content == '$emoji':
        emoji = emoji_olusturucu()
        await message.channel.send(emoji)
    elif message.content == '$yazıtura':
        tura = yazi_tura()
        await message.channel.send(tura)
    else:
        await message.channel.send(message.content)

client.run(token)