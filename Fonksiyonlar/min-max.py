sayilar = [1,5,7,45,25,89]
harfler = ['a','v','h','s']
isimler = ['muhammet','medine','sena','osman','fazile']

sonuc = min(sayilar) # min sayı
sonuc = max(sayilar)

sonuc = min(harfler) #alfabetik küçükten büyüğe
sonuc = max(harfler)

sonuc = min(isimler)
sonuc = max(isimler)

sonuc = [len(isim) for isim in isimler] #isimlerdeki her bir ismin harf sayısı
sonuc = min(len(isim) for isim in isimler) #en düşük harf sayısı olanın harf sayısı
sonuc = max(len(isim) for isim in isimler) #en yüksek harf sayısı olanın harf sayısı

sonuc = max(isimler, key=lambda n: len(n)) #en yüksek harfli isim
sonuc = min(isimler, key=lambda n: len(n)) #en düşük harfli isim


urunler = [
    {"title":"iphone x" ,"price":5000},
    {"title":"iphone xr" ,"price":6000},
    {"title":"iphone 11" ,"price":7000}
]

sonuc = max(urunler,key = lambda p: p["price"]) #fiyatı en büyük olanı
sonuc = max(urunler,key = lambda p: p["price"])["title"] 
#sonuc = urunler["title"] ==> bir üstteki işlem kafa karıştırmasın :)
sonuc = max(urunler,key = lambda p: p["price"])["price"]
print(sonuc)

# az öncekini max kullanmadan nasıl yapardık ?

k = 0

for urun in urunler:
    if urun["price"] > k:
        k = urun["price"]

print(k)