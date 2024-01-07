import random
# # Kullanıcının parolasının içerebileceği tüm karakterleri içeren bir değişken oluşturun
# karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
# # Örneğin: "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
# # Programın oluşturulan parolayı saklayacağı bir değişken oluşturun
# # Bir değişken oluşturun ve kullanıcıdan parolanın uzunluğunu girmesini isteyin
# parola_uzunlugu = int(input("parolanin uzunlugunu kac olsun?"))
# #  Karakter değişkeninden rastgele bir karakter seçmek ve bunu oluşturulan parolanın bulunduğu değişkene eklemek için bir döngü ve random kütüphanesi kullanın
# parola = ""

# for i in range(parola_uzunlugu):
#   rastgele = random.choice(karakterler) 
#   parola += rastgele
  
# # Elde edilen parolayı konsola yazdırın
# print(parola)

def sifre_olusturucu(parola_uzunlugu):
    karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    parola = ""
    for i in range(parola_uzunlugu):
      rastgele = random.choice(karakterler) 
      parola += rastgele

    return parola
  
