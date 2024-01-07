from kodlar_ve_dosyalar.token import ayarlar
import discord
from discord.ext import commands

# import * - kütüphanedeki tüm dosyaları içe aktarmanın hızlı bir yoludur
from bot_mantik import *

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
ayricaliklar = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
ayricaliklar.message_content = True
# istemci (client) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
bot = commands.Bot(command_prefix='$', intents=ayricaliklar)


# Bot hazır olduğunda adını yazdıracak!
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')


# Bot bir mesaj aldığında, aynı kanalda mesaj gönderecek!
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def pasw(ctx):
    await ctx.send(sifre_olusturucu(10))
    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(ayarlar["TOKEN"])
