# sum(...) içindeki liste elemanlarını toplar.

sayilar = [34,2,5,7,98]

sonuc = sum(sayilar)
sonuc = sum(sayilar,10)

urunler = [
    {"title":"iphone x" ,"price":5000},
    {"title":"iphone xr" ,"price":6000},
    {"title":"iphone 11" ,"price":7000},
    {"title":"iphone 11 Pro" ,"price":0}
]

sonuc = [urun["price"] for urun in urunler] #ürünlerin fiyatlarını liste şeklinde yazar
sonuc = sum([urun["price"] for urun in urunler]) #fiyatları toplar

# toplamFiyat = sum([urun["price"] for urun in urunler])
# sonuc = toplamFiyat / len(urunler) ====> sorun şu ki listede fiyatı 0 olan eleman olabilir

#böyle kurtarabiliriz.
toplamFiyat = sum([urun["price"] for urun in urunler])
urunAdet = len([urun for urun in urunler if urun["price"] > 0])
sonuc = toplamFiyat / urunAdet

################## round
sonuc = round(10.2)
sonuc = round(10.6)
sonuc = round(10.5)
sonuc = round(1.42424242, 2) #1.42 #(noktadan sonra ik basamak)
sonuc = round(1.42624242, 2  ) #1.43

print(sonuc)


