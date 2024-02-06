from gtts import gTTS

def text_to_speech_and_save(text):

    # Kullanıcının Gireceği Mesaj
    #text = input("Enter the text you want to convert to MP3: ")

    # Dil Seçme
    language = 'tr'

    # Specify the speed (adjust as needed)
    speed = 1.5  # You can experiment with different values

    tts = gTTS(text=text, lang=language, slow=False)

    # Dosyayı Kaydeden Kod
    #filename = input("Enter the desired filename (include .mp3 extension): ")
    filename = "filename.mp3"
    tts.save(filename)
    #print(f'Text converted to MP3 with Turkish language and saved as {filename}')
    return filename

text_to_speech_and_save()
