# 1- Girilen bir sayının 50-100 arasında olup olmadığını kontrol ediniz.
"""
sayi = int(input("Enter the number: "))
if (50 < sayi < 100):
    print("The number is between 50 and 100")
elif (sayi < 50):
    print("The number is less than 50")
elif (sayi > 100):
    print("The number is greater than 100")
"""

# 2- Girilen bir sayının pozitif tek(odd) sayı olup olmadığını kontrol ediniz.
# tek = odd
# çift = even
'''
sayi = int(input("Enter the number: "))
if (sayi > 0) and (sayi % 2 == 1):
    print("The number is odd and positive.")
elif (sayi < 0) and (sayi % 2 == 1) :
    print("The number is odd but negative.")
elif (sayi > 0) and (sayi % 2 == 0):
    print("The number is positive but even number.")
else:
    print("The number is not odd and positive. It is even and negative.")
'''

# 3- Username ve parola bilgileri ile giriş kontrolü yapınız. 
'''
_username = "sadikturan"
_password = "1234"
username = input("Username: ")
password = input("Password: ")

if (username.strip() == "sadikturan") and (password.strip() == "1234"):
    print("Username and password is correct. Welcome...")
else:
    print("Try again.")
# boşluklar alınmalı ===> strip()
'''

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
'''
a = int(input("first number: "))
b = int(input("second number: "))
c = int(input("third number: "))

if (a > b) and (a > c):
    print("The first number is the greatest..")
elif (b > a) and (b > c):
    print("The second number is the greatest..")
elif (c > a) and (c > b):
    print("The third number is the greatest..")
'''


# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    a-) Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    b-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    c-) Finalden 70 alındığında ortalamanın önemi olmasın.
'''
_vize1 = float(input("Birinci vize: "))
_vize2 = float(input("İkinci vize: "))
_final = float(input("Final: "))
ort = (((_vize1 + _vize2) / 2)  * (0.6)) + (_final * 0.4) #ortalama
ort = round(ort,3) #virgülden sonra max 3 eleman.
print("Ortalama: ",ort)
'''

'''
#first
if (ort > 50):
    print("Geçti :)")
else:
    print("Kaldı :(")
'''

"""
#second
if (ort >= 50) and (_final >= 50):
    print("Geçti :)")
else:
    print("Kaldı :(")
"""

#third
'''
if (ort > 50) or (_final >= 70):
    print("Geçti :)")
else:
    print("Kaldı :(")
'''

#third_2
'''
if (_final >= 70) and (ort <= 50):
    print("Ort. yetmedi ama final kurtardı :)))")
elif (ort >= 50) and (_final >= 50):
    print("Geçti :)")
else:
    print("Kaldı :(")
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

if (0 < index < 18.4):
    print("Zayıf")
elif (18.5 < index < 24.9):
    print("Normal")
elif (25 < index < 29.9):
    print("Fazla Kilolu")
elif (30 < index < 34.9):
    print("Obez")