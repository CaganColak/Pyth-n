import os
import random
import pygame
import threading
import time

def play_random_mp3(directory):
    #Belirttiğimiz dizindeki mp3 dosyalarını listeliyor
    mp3_files = [file for file in os.listdir(directory) if file.endswith(".mp3")]

    #Dosya yoksa hata mesajı
    if len(mp3_files) == 0:
        print("Belirtilen dizinde MP3 dosyası bulunamadı.")
        return

    #Rastgele mp3 dosyasını seçer
    random_mp3 = random.choice(mp3_files)

    #Pygame i başlatır
    pygame.init()

    try:
        #mp3 dosyasını çalmak için mixeri başlatıyor
        pygame.mixer.init()
        #mp3 dosyasını yüklüyor
        pygame.mixer.music.load(os.path.join(directory, random_mp3))
        #mp3 dosyasını çalıyor
        pygame.mixer.music.play()

        #mp3 dosyasının bitmesini bekler
        while pygame.mixer.music.get_busy():
            pass

    except pygame.error:
        print("MP3 dosyası çalınırken bir hata oluştu.")

    #pygame i kapatır
    pygame.mixer.quit()
    pygame.quit()

def play_random_mp3_random_time(directory):
    while True:
        #10 ila 40 saniye arası rastgele bir süre seçer
        wait_time = random.randint(10,40)
        time.sleep(wait_time)

        #rastgele bir mp3 dosyası seçer
        play_random_mp3(directory)

#mp3 dosyalarının bulunduğu dizin
mp3_directory = "MP3 DOSYALARININ BULUNDUĞU DİZİNİ GİRİN"

#rastgele zaanda rastgele mp3 dosyasını çalar
play_thread = threading.Thread(target=play_random_mp3_random_time, args=(mp3_directory,))
play_thread.start()