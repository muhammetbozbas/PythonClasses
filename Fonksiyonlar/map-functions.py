#listedeki elemanların üzerinde bir işlem uygulayıp liste şeklinde output alırız.
""" aslında bu işlemi yapacağız
sayilar = [1,2,4,6,7]
kareleri = []

for sayi in sayilar:
    kareleri.append(sayi**2)

print(kareleri)
"""

sayilar = [1,2,4,6,7,-1] #iterable object
str_sayilar = ["1","2","4","6","9"] 
isimler = ["muhammet","Medine"]
users = [
    {"ad": "ali", "soyad": "Yılmaz"},
    {"ad": "ahmet", "soyad": "Yılmaz"}
]

def kareAl(sayi):
    return sayi ** 2

sonuc = list(map(kareAl, sayilar))
#aynı işlemi tek satır kodla yapabiliriz.
sonuc2 = list(map(lambda sayi: sayi ** 2, sayilar))

sonucStr= list(map(int,str_sayilar)) #listedeki str ifadelerin hepsini int'e çevirdik
sonucAbs= list(map(abs,sayilar))
sonucFloat = list(map(float,sayilar))
isim = list(map(len,isimler))
isimm = list(map(str.capitalize,isimler))
isimm = list(map(str.lower,isimler))
user = list(map(lambda x: x["ad"],users))
#kullanıcılar içindeki sadece ad bilgilerini aldık.


print(sonuc)
print(sonuc2)
print(sonucStr)
print(sonucAbs)
print(sonucFloat)
print(isim)
print(isimm)
print(user)