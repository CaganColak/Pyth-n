import os
## kök dizini bul ##
print(os.listdir('./'))
## kök dizin ##
root = "./kodlar_ve_dosyalar/ex1_read-write"

# Bu kod parçacığı bir metin dosyasının tamamını okumamızı sağlar
file = open(f'{root}/text.txt', 'r', encoding='utf-8')
text = file.read()
print(text)
file.close()

