import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import youtube_dl
from key import token
from speech import speech_tr

# Google Cloud Speech-to-Text API'yi kullanmak için servis anahtarınızı ekleyin
# https://cloud.google.com/speech-to-text/docs/quickstart
google_cloud_credentials_path = 'path/to/your/credentials.json'

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected to Discord!')

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # Mesaj bir ses dosyası içeriyorsa işlem yap
    if message.attachments:
        for attachment in message.attachments:
            if attachment.content_type.startswith('audio/'):
                await transcribe_audio(message, attachment.url)

    await bot.process_commands(message)

async def transcribe_audio(message, audio_url):
    # Google Cloud Speech-to-Text API'ye bağlan
    client = speech.SpeechClient.from_service_account_file(google_cloud_credentials_path)

    # Ses dosyasını indir
    audio_data = await message.attachments[0].read()

    # Dosyayı çalabilmek için geçici olarak kaydet
    with open('temp.mp3', 'wb') as f:
        f.write(audio_data)

    # Dosyayı çal
    voice_channel = await message.author.voice.channel.connect()
    voice_channel.play(discord.FFmpegPCMAudio('temp.mp3'), after=lambda e: print('done', e))

    # Konfigürasyonu ayarla
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="tr-TR",  # Dil kodunu uygun bir şekilde değiştirin
    )

    # Transkripti al
    audio = speech.RecognitionAudio(content=audio_data)
    response = client.recognize(config=config, audio=audio)

    # Transkripti metin kanalına gönder
    for result in response.results:
        await message.channel.send(f"**Ses Dosyası Transkripti:**\n{result.alternatives[0].transcript}")

    # Ses kanalından ayrıl
    await voice_channel.disconnect()

# Ana kod
if __name__ == "__main__":
    bot.run(token)
