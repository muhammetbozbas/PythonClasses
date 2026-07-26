# 1- 3 ürün bilgisini (id,ad,fiyat) kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
# 2- Ürün id bilgisini kullanıcıdan alıp ilgili ürün bilgisini gösterin.

"""
id1 = input("id1: ")
ad1 = input("ad1: ")
fiyat1 = input("fiyat1: ")



id2 = input("id2: ")
ad2 = input("ad2: ")
fiyat2 = input("fiyat2: ")



id3 = input("id3: ")
ad3 = input("ad3: ")
fiyat3 = input("fiyat3: ")


urunler = {
        id1 : {
            'ad': ad1,
            'fiyat': fiyat1,
        },
        id2 : {
            'ad': ad2,
            'fiyat': fiyat2,
        },
        id3 : {
            'ad': ad3,
            'fiyat': fiyat3,
        }
    }
#2
personalID = input("İstediğiniz ürünün id bilgisini yazınız: ")
print(urunler[personalID])
"""

urunler = {}

id = input("id: ")
ad = input("ad: ")
fiyat = input("fiyat: ")

urunler[id] = {
    "ad": ad,
    "fiyat": fiyat,
}

id = input("id: ")
ad = input("ad: ")
fiyat = input("fiyat: ")

urunler[id] = {
    "ad": ad,
    "fiyat": fiyat,
}

id = input("id: ")
ad = input("ad: ")
fiyat = input("fiyat: ")

urunler[id] = {
    "ad": ad,
    "fiyat": fiyat,
}

personalId = input("istediğiniz ürün id: ")
urun = urunler[personalId]

print(f"id: {personalId}, urunAdi: {urun["ad"]}, urunFiyati: {urun["fiyat"]}")





