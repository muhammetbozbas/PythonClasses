r = float(input("Yarıçap: ")) # r, tam sayı değilse int kullanarak veri kaybı yaşarız.
alan = 3 * (r**2) # işlem önceliği olsa da clean kod için parantez kullanmalıyız.
cevre = 2 * 3 * r
result = "Alan: " + str(alan) +  " Çevre: " + str(cevre)
#iki bilgi de str olsun ki "+" ile birleştirilebilsin.
print(result)



# mil = km / 1.609344

km = print("Km = ?")
km = input()
mile = float(km) / 1.609344
mile = round(mile, 3) # yuvarlama için kullanılır virgül sonrası basamak kadar yuvarlar, kısaltır.
print(str(km) + " km = " + str(mile) + " miles")


# Km'yi str olarak aldık ve mile dönüştürürken floata çevirdik.



