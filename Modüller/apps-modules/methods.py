from db import urunler

def urunGuncelle(key,value):
    urunler.update({
        key : value
    })

def urunEkle(key,value):
    urunler[key] = value

def urunleriGetir(dict):
    for x,y in dict.items():
        print(x,':',y)




