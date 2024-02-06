import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import youtube_dl
from key import token

intents = discord.Intents.default()
intents.messages = True  # Mesajları dinlemek için intents'i etkinleştir
# Bot oluştur
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected to Discord!')

@bot.command(name="dinle")
async def dinle(ctx):
    channel = ctx.author.voice.channel
    voice_channel = await channel.connect()

    def check(m):
        return m.author == ctx.author and m.content.startswith('!stop')

    # YouTube videosunu çalmak için kullanılan özel bir fonksiyon
    def play_youtube(url):
        ydl_opts = {'format': 'bestaudio'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            voice_channel.play(FFmpegPCMAudio(url2), after=lambda e: print('done', e))
    
    await ctx.send("Dinlemeye başlandı. !stop yazarak dinlemeyi durdurabilirsiniz.")

    while True:
        try:
            message = await bot.wait_for('message', check=check, timeout=10.0)
            if message.content == "!stop":
                await ctx.send("Dinleme durduruldu.")
                break
        except:
            pass

    await voice_channel.disconnect()

# Ana kod
if __name__ == "__main__":
    # Botu çalıştır
    bot.run(token)
