'''
    1-100 arasında rastegele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
    buldurmaya çalışın. 
    ** "random modülü" için "python random" şeklinde arama yapın.
    ** 100 üzerinden puanlama yapın.
    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
'''

import random

# number = random.randrange(1,100) #rastgele üretilen numara.
number = random.randint(1,100) #rastgele üretilen numara. max dahil


hak = int(input("Kaç tahminde bilebilirsiniz: "))
soru = (100 / hak) #yanlış başına kaybedilen puan. her sorunun puan değeri.

userNumber = int(input("1 ile 100 arasında bir numara giriniz: "))

while userNumber <= 0:
    userNumber = int(input("Negatif numara girdiniz tekrar giriniz(hakkınız gitmeyecektir): "))


while userNumber != number:
    hak -= 1
    if hak == 0:
            print(f"Elendiniz.. Tutulan sayı: {number}")
            break
    print(f"{hak} hak kaldı.")
    if userNumber < number:
        userNumber = int(input("Yukarı: "))
        if hak == 0:
            print(f"Elendiniz.. Tutulan sayı: {number}")
            break
        continue
    elif userNumber > number:
        userNumber = int(input("Aşağı: "))
        if hak == 0:
            print(f"Elendiniz.. Tutulan sayı: {number}")
            break
        continue
else:
    puan = hak * soru
    print(f"Tebrikler. {int(puan)} puan kazandınız.")

        
