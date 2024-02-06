import discord
from discord.ext import commands
from google.cloud import speech_v1p1beta1 as speech
from key import token

# Google Cloud Speech-to-Text API'yi kullanmak için servis anahtarınızı ekleyin
# https://cloud.google.com/speech-to-text/docs/quickstart
google_cloud_credentials_path = 'path/to/your/credentials.json'

intents = discord.Intents.default()
intents.messages = True  # Mesajları dinlemek için intents'i etkinleştir

bot = commands.Bot(command_prefix="!", intents=intents)

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
    audio = speech.RecognitionAudio(content=audio_data)

    # Konfigürasyonu ayarla
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="tr-TR",  # Dil kodunu uygun bir şekilde değiştirin
    )

    # Transkripti al
    response = client.recognize(config=config, audio=audio)

    # Transkripti metin kanalına gönder
    for result in response.results:
        await message.channel.send(f"**Ses Dosyası Transkripti:**\n{result.alternatives[0].transcript}")

# Ana kod
if __name__ == "__main__":
    bot.run(token)