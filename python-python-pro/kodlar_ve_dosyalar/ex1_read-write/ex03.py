import os
## kök dizini bul ##
print(os.listdir('./'))
## kök dizin ##
root = "./kodlar_ve_dosyalar/ex1_read-write"

# Daha kısa bir versiyonu:
with open(f'{root}/text.txt', 'r', encoding='utf-8') as f:
    print(f.read())
    
