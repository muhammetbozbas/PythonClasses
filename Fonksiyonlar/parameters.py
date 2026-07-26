#fonksiyondaki parantezin içine yazdığımız şey parametresidir


def selamla(isim):
    return "Merhaba, " + isim

sonuc = selamla("Muhammet")
sonuc = selamla("Medine")

def toplam(a,b):
    return a + b

sonuc = toplam(10,20)
sonuc = toplam(30,20)



def yasHesapla(dogumYili):
    return 2026 - dogumYili

sonuc = yasHesapla(2007)
sonuc = yasHesapla(1977)

def emekliligeKacYilKaldi(dogumYili, isim):
    yas = yasHesapla(dogumYili)

    kalanSure = 65 - yas

    if kalanSure > 0:
        print(f"{isim}, emekliliğinize {kalanSure} yıl kaldı.")
    else:
        print(f"{isim}, zaten {abs(kalanSure)} yıl önce emekli oldunuz") #abs fonksiyonu içine yazılan değerin mutlağını alır. (absoulute)
        

emekliligeKacYilKaldi(2007, "Muhammet")
emekliligeKacYilKaldi(1950, "Ali")




