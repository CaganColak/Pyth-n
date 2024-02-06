import discord
from discord.ext import commands
from key import token

intents = discord.Intents.default()
intents.messages = True  # Mesajları dinlemek için intents'i etkinleştir

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Botun kendi mesajlarını işleme alma

    if message.channel.name == "Genel":  # Arama kanalının adını uygun şekilde değiştirin
        # Burada metne çevirme işlemini yapabilirsin, örnek olarak aynı mesajı tekrar gönderiyorum
        await message.channel.send(f"{message.author.display_name}: {message.content}")

    await bot.process_commands(message)

# Botunuzun token'ını buraya ekleyin
bot.run(token)