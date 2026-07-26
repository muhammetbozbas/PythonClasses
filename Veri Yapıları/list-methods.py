sayilar = [1,5,8,9,3,45]
harfler = ["a","b","e","s","a","z","y",'m']


sonuc = min(sayilar) # Min sayı
sonuc = max(sayilar) # Max sayı

sonuc = min(harfler) # Alfabetik olarak ilk harfi alır. (kelime olsa da)
sonuc = max(harfler) # Alfabetik olarak sonu alır.

# ekleme
sayilar.append(61) # Listenin sonuna eleman ekler.
sayilar.insert(3,55) # Ekleyeceğimiz elemanın konumunu belirtmen zorundayız. (3. indexe ekledi)
sayilar.insert(len(sayilar),150) # Yine sonuna eklemiş olduk.

# silme
sayilar.pop() # Son elemanı siler (boşken) (int)
sayilar.pop() # Tekrar yazıldığında yine sonuncuyu siler.
sayilar.pop(-2) # Verilen index numarasındaki elemanı siler.
sayilar.remove(8) # Yazılan değeri siler. (int, str)
harfler.remove("y") 

# sıralama
sayilar.sort() # Listeyi küçükten büyüğe sıralar.
harfler.sort() # Listeyi alfabetik sıralar.
sayilar.reverse() # Listeyi ters çevirir, sıralanmışsa büyükten küçüğe çıkmış olur.

print(sayilar.count(5)) # Kaç tane olduğunu sorar.
print(harfler.count('a'))

print(sayilar.index(55)) # Yazılan ifadenin index numarasını sorgular.
sayilar.clear() # Listedeki elemanları siler, listeyi boşaltır. 




sonuc = sayilar





print(sonuc)