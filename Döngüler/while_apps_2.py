#    Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (urunAdi, fiyat) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

#------BAŞTA DICT FORMATINDA OLUŞTURDUĞUMUZ DURUM------
'''
urunler = {}
urun_sayisi = int(input("urun sayisi giriniz: "))

i = 0
while (i < urun_sayisi):
    urunAdi = input("urun adi giriniz: ")
    fiyat = input("fiyat bilgisi giriniz: ")
    urunler[urunAdi] = fiyat
    i += 1
'''
    
#for kullanarak yazdırma (başta dict oluşturma)
# for ad,fiyat in urunler.items():
#     print(f"Ad: {ad}  Fiyat: {fiyat}")

"""
items = list(urunler.items()) #dict => indexlenemez ancak while index mantığında çalışır.
k = 0
while k < len(items):
    ad, fiyat = items[k]
    print(f"Ad: {ad} Fiyat: {fiyat}")
    k += 1
"""

#-------BAŞTA LIST FORMATINDA OLUŞTURDUĞUMUZ DURUM------

tumUrunler = [] #boş bir liste oluşturdum
adet = int(input("urun adedi giriniz: "))

i = 0
while (i < adet):
    ad = input("urun adi: ")
    fiyat = input("urun fiyati: ")
    tumUrunler.append({
        'ad': ad,
        'fiyat': fiyat
    })
    i += 1

k = 0
while (k < len(tumUrunler)):
    print(f"Ad {k + 1}: {tumUrunler[k]['ad']} Fiyat {k + 1}: {tumUrunler[k]['fiyat']}") #tumUrunler içinden k indexinin key değerini yazdık.
    k += 1

# k + 1 olayını ben ekledim 

