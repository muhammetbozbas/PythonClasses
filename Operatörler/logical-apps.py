# 1- Girilen bir sayının 50-100 arasında olup olmadığını kontrol ediniz.
'''
sayi = int(input("Enter a number: "))
sonuc = (sayi >  50) and (sayi < 100)
print(f"{sayi}, 50 ile 100 arasındadır: {sonuc}")
'''

# 2- Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz.
'''
number = int(input("Enter a number: "))
sonuc = (number > 0) and (number % 2 != 0)

'''

# 3- Username ve parola bilgileri ile giriş kontrolü yapınız. 
'''
_username = input("Enter your username: ")
_password = input("Enter your password: ")
sonuc = (_username == "weaper") and (_password == "6161")
'''
# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
'''
a = int(input("the first number: "))
b = int(input("the second number: "))
c = int(input("the third number: "))
sonuc = (a > c) and (a > c)
print("a en büyük sayı: ", sonuc)
sonuc = (b > c) and (b > a)
print("b en büyük sayı: ", sonuc)
sonuc = (c > a) and (c > b)
print("c en büyük sayı: ", sonuc)
'''
# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.
'''
_vize1 = float(input("Birinci vize: "))
_vize2 = float(input("İkinci vize: "))
_final = float(input("Final: "))
ort = (((_vize1 + _vize2) / 2)  * (3/5)) + (_final * 2/5) #ortalama
sonuc = ((ort >= 50) and (_final >= 50)) or (_final >= 70)
print("Geçme durumunuz:", sonuc)
'''

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf 
#    18.5-24.9 => Normal  
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)
ad = input("Enter your name: ")
kilo = float(input("Enter your weight: "))
boy = float(input("Enter your height(type 'm'): "))
index = (kilo / (boy ** 2))
print(index)
if 0 < index < 18.4:
    print("zayıf")
if 18.5 < index < 24.9:
    print("normal")
if 24.9 < index < 29.9:
    print("fazla kilolu")
if 30 < index < 34.9:
    print("obez") 


