# dict veri yapısı değiştirilebilir, indexlenebilir ancak SIRALANAMAZ.  
# key - value  (anahtar - değer ilişkisi)

# 41 => kocaeli
# 34 => istanbul

'''
sehirler = ['kocaeli', 'istanbul']
plakalar = [41,34]

print(plakalar[1], sehirler[1])
print(plakalar[0], sehirler[0])

# example
print("İstanbulun plakasi; ")
print(plakalar[sehirler.index('istanbul')])
'''

# bu metotlar uzun ve karmaşık key - value ilişkisi ile daha kolay ve açık olanını yapabiliriz.
# süslü parantez!!

#1
plakalar = {'kocaeli': 41, 'istanbul': 34}
print(plakalar['kocaeli']) 
# plakalar içinde kocaeliyi anahtar yaptık ve kocaeli yazdığımızda elimize onun değeri geçti


plakalar['trabzon'] = 61
plakalar['izmir'] = 36
plakalar['izmir'] = 35 # yanlış yazılan durumlarda bu şekilde tekrar yazarak değiştirebiliriz. 

# plakalara içinde bu değerler olmadığı için direkt ekledi

print(plakalar)

#2
ogrenciler = {
   100: {
     "ad": "Cinar",
     "soyad": "Turan",
     "yas": 12,
     "notlar": [80,90,70]
    },
    101: {
        "ad" : "Ada",
        "soyad" : "Bilgi",
        "yas" : 5,
        "notlar": [85,95,100]
    }
}
# dict içine dict tanımlayıp onları numaralandırdık.
# verdiğimiz numaranın içine de öğrencinin tüm bilgilerini yazdık.
# bunu yaparken ':'kullanıp her satır sonuna da ',' attık.

print(ogrenciler[101])
print(ogrenciler[100]['ad'])  # 100 içindeki 'ad' anahtarının değerini aldık.
sonuc = ogrenciler[100]['notlar'] 
print(sonuc)

ort = (ogrenciler[100]["notlar"][0] + ogrenciler[100]["notlar"][1] + ogrenciler[100]["notlar"][2]) / 3
print(ort) # Ortalama aldık.
