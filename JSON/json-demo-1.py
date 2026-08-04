#Not: işlem dosya üzerinde ise tekil, obje üzerinde ise çoğul metot kullanırız(loads,dumps)


# urunAdi, fiyat, satistaMi ve kategori bilgilerini alarak json veri türünde kayıt yapan fonks.
#  urun bilgilerini getiren fonksiyon.

import json
def kayit(urunAdi,fiyat,satistami,kategori):
    urun = {
        "name" : urunAdi,
        "price" : fiyat,
        "saleinfo" : satistami,
        "category" : kategori
    }
    with open("urunler.json","w",encoding="utf-8") as file:
        json.dump(urun,file,ensure_ascii=False,indent=2)

# kayit("iPhone 13",33000,True,"Phone")

def bilgiler():
    with open("urunler.json") as file:
        info = json.load(file)
        print(f"ad: {info["name"]}, fiyat:{info["price"]}, satista mi: {info["saleinfo"]}, kategori: {info["category"]}")

bilgiler()