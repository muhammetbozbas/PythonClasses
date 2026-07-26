# ------1- Girilen 2 sayıdan hangisi büyüktür ?-----

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# result = (a < b)
# print(f"{a}, {b}'den büyüktür: {result}")


''' (ben yaptim)
if a < b:
    print("a, b'den küçüktür")
else:
    print("a, b'den büyüktür")
'''

# -----2- Girilen bir sayının tek mi çift mi olduğunu yazdırın.------

# sayi = int(input("tek-çift sorgusu için sayi giriniz: ") )
# sonuc = ((sayi % 2) == 0)
# print(sonuc)

'''
if sonuc == True:
    print(sayi, "çift bir sayidir.")
else:
    print(sayi, "tek bir sayidir")
'''

# 3- Girilen bir sayının negatif pozitif durumunu yazdırın
"""
sayi = int(input("'-,+' sorgulaması için sayı giriniz: "))
sonuc = (sayi > 0)
print(f"'{sayi}' pozitiftir: {sonuc}")
"""

# ------4- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
"""
first = float(input("Enter the your first vize: "))
second = float(input("Enter the your second vize: "))
final = float (input("Enter the your final: "))

ort = (((first + second) / 2) * (60/100)) + (final * (40/100))
print("Not ortalamanız: ", ort)
"""

#  -----  Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# print(f"Not ortalamanız: {ort} ve geçme - kalma durumunuz: {ort >= 50} ")

"""
if ort >= 50:
    print("GEÇTİ")
else:
    print("KALDI")
"""

# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: info@sadikturan.com parola:12345)
mail = input("Enter the email information: ")
password = (input("Enter the password: "))

mailkontrol = (mail.strip().lower() == "info@sadikturan.com") # baş ve sondaki boşlukları silmeliyiz ve küçük harf yapmalıyız.
passkontrol = (password.strip() == "12345")

print(f"Email is {mailkontrol}, Password is {passkontrol}")


