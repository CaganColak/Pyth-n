import os
## kök dizini bul ##
print(os.listdir('./'))
## kök dizin ##
root = "./kodlar_ve_dosyalar/ex1_read-write"

# Ve işte bir metin dosyasının tamamını nasıl yeniden yazabileceğimiz:
file = open(f'{root}/metinbelgesi.txt', 'w', encoding='utf-8')
text = 'Yeni Yazı'
file.write(text)
file.close() 
