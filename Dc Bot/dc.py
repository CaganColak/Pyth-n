import discord
from bot_logic import *
import requests


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

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
    elif message.content.startswith('Orkun Işıtmak'):
        await message.channel.send("https://tenor.com/view/orkun-%C4%B1%C5%9F%C4%B1tmak-orkun-isitmak-gif-8480279054209557082")
    elif message.content.startswith('Yok'):
        await message.channel.send("https://tenor.com/view/yok-ghost-rider-ghost-rider-meme-gif-26788994")
    elif message.content.startswith('!komut'):
        await message.channel.send("Komutlarım: Sa,Fati,Enes Batur,PP,toss,emoji,Orkun Iştmak,Yok")
    elif message.content.startswith('ÇALIŞIYOR'):
        await message.channel.send("Ne Sandın")
    elif message.content.startswith('mem'):
        with open('Dc Bot\images\mem1.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
            picture = discord.File(f)
        # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
        await message.channel.send(file=picture)
    elif message.content.startswith('duck'):
        '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
        image_url = get_duck_image_url()
        await message.channel.send(image_url)

    else:
        await message.channel.send("")

    
client.run("MTExMjA2OTUwMzE2MTk5OTQwMA.GQOIBT.6VvzSmm7MH4Ncp1aQNja1dqWw6qEVAgDvCo9jk")
