urunler = [
    {'name':'iphone 8', 'price': '4000' },
    {'name':'iphone 8 Plus', 'price': '5000' },
    {'name':'iphone X', 'price': '6000' },
    {'name':'iphone XR', 'price': '7000' },
    {'name':'iphone 11', 'price': '8000' },
    {'name':'samsung s10', 'price': '6000' },
]
# 1- Tüm ürün bilgilerini listeleyiniz.
'''
for urun in urunler:
    print(urun["name"],':',urun["price"])

for urun in urunler:
    print(f"urun adı: {urun["name"]} ve urun fiyatı: {urun["price"]}")
'''
# 2- Ürünlerin fiyatları toplamı nedir ?
'''
toplam = 0
for total in urunler:
    x = int(total['price'])
    toplam = toplam + x 
print(f"urun toplamları: {total} TL)
'''

# 3- Ürünlerden fiyatı en fazla 6000 olan ürünleri gösteriniz ?
"""1
for max in urunler:
    names = max['name']
    six = int(max['price'])
    if six <= 6000:
        print(names,':', six)
"""

'''2 (daha iyi) ikisini de ben yaptım :]
for urun in urunler:
    if int(urun["price"]) <= 6000:
        print(f"{urun["name"]}: {urun["price"]}")
'''
# 4- Kullanıcıdan alınan anahtar kelimeyi içeren ürünleri bulunuz.
"""
key = input("Aranan ürün: ")
for urun in urunler:
    if urun['name'].find(key.lower()) > -1:
        print(f"{urun}")
#string bilgi içerisinde aramayı find veya index ile yapabiliriz.
"""