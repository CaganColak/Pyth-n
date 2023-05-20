import random

kullanilan_karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
print("Şifre Oluşturucuya Hoşgeldiniz.")
sifre_uzunluk = int(input("Oluşturulacak Şifre İçin Uzunluk Giriniz(Sayı)= "))
sifre_adet = int(input("Kaç Adet Şifre Oluşturulsun(Sayı)"))

for i in range(sifre_adet):
    sifre = ""
    for i in range(sifre_uzunluk):
        sifre += random.choice(kullanilan_karakterler)

        print("Random Şifreniz : ",sifre)
