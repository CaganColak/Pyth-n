from ayarlar import ayarlar
import discord
from bot_logic import *

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# istemci (client) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
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
    else:
        await message.channel.send(message.content)

client.run(ayarlar["TOKEN"])