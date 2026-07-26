# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. 
# Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır. 
'''
name = input("İsim: ").strip()
age = int(input("Yas: "))
eduInformation = input("Eğitim bilgilerinizi giriniz (ilkokul, ortaokul, lise, üniversite): ")

if (age >= 18):
    print("Yaşınız tutuyor.")
    if (eduInformation.strip() == "lise" , "üniversite"):
        print(f"Eğitim durumunuz da yeterli. Tebrikler {name}")
    else: 
        print("Eğitim durumunuz yetersiz.")
else:
    print("Yaşınız yetersiz.")
'''

# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık 
# gelen not bilgisini yazdırınız.
#    0-24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5
'''
first = int(input("İlk yazılı sonucunu giriniz: "))
second = int(input("İkinci yazılı sonucunu giriniz: "))
sozlu = int(input("Sözlü sonucu: "))

ort = (first + second + sozlu) /3

print("Ortalama bilginiz: {})

if 0 <= ort <= 24:
    ort = 0
elif 25 <= ort <= 44:
    ort = 1
elif 45 <= ort <= 54:
    ort = 2
elif 55 <= ort <= 69:
    ort = 3
elif 70 <= ort <= 84:
    ort = 4
elif 85 <= ort <= 100:
    ort = 5
else:
    print("Hesaplanamıyor. Notlar 0 ile 100 aralığında olmalıdır!")
    quit()

print(f"NOT BİLGİSİ: {ort}")
'''
# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#    1. Bakım => 1. yıl     
#    2. Bakım => 2. yıl      
#    3. Bakım => 3. yıl     
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#    *** datetime modülünü kullanmanız gerekiyor.  
#    (simdi) - (2018/8/1) => gün

from datetime import datetime
today = datetime.today() # bugünü yıl, ay, gün olarak aldı.

year = int(input("yıl: "))
month = int(input("ay: "))
day = int(input("gün: "))

cikis = datetime(year, month, day)
fark = today - cikis
gun = fark.days
print(gun, "gün önce trafiğe çıktınız")

if (gun <= 365) and (gun >= 0):
    print("1. Bakım tarihiniz gelmiştir.")
elif (gun <= 365*2) and (gun > 365):
    print("2. Bakım tarihiniz gelmiştir.")
elif (gun <= 365*3) and (gun > 365*2):
    print("3. Bakım tarihiniz gelmiştir.")
else:
    print("0 ila 3 yıl arasında bir tarih olmalı.")
# bu uygulama geliştirilecek!!!