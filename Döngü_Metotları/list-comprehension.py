liste = [10,4,7,9,70]

sayilar = []

for i in range(10):
    i *= 2
    sayilar.append(i)
#bu işlemi tek satırda halledebiliriz.


# [expression for item in list]
# sonuc = [k*k for k in range(10)]
# sonuc = [k*2 for k in liste]

isim = "Ahmet"
isimler = ["Ahmet", "ali", "Çınar", "DeNiz"]

sonuc = [c.upper() for c in isim]
sonuc = [str(sayi) for sayi in liste] #ifadeleri str formatında yazdırdık.
sonuc = [i for i in isimler] #isimler listesini hiçbir şey yapmadan yazdırır.
sonuc = [i.lower() for i in isimler] 



print(sonuc)
