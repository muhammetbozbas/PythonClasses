isimler = ['Ada','Yiğit','Hasan','Beril']
yaslar = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
isimler.append("Cenk")
print(isimler)

# 2-  "Sena" değerini listenin başına ekleyiniz.
isimler.insert(0,"Sena")
print(isimler)

# 3-  "Yiğit" ismini listeden siliniz.
# isimler.remove("Yiğit")
print(isimler)

# 4-  "Yiğit" isminin indeksi nedir ?
print(isimler.index("Yiğit"))

# 5-  "Beril" listenin bir elemanı mıdır ?
if "Beril" in isimler:
    print("'Beril' in isimler.")

sonuc = "Beril" in isimler # True - False olarak verir. 
print(sonuc)

# 6-  Liste elemanlarını ters çevirin.
isimler.reverse()
yaslar.reverse()
print("Lists was reversed: ",isimler, yaslar)

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
isimler.sort() 
print(isimler)

# 8-  yaslar listesini rakamsal büyüklüğe göre sıralayınız.
yaslar.sort()
print(yaslar)

# 9-  s = "IPhone X,IPhone XR" karakter dizisini listeye çeviriniz.
s = ["IPhone X,IPhone XR"]
print(s) #1

s = "IPhone X,IPhone XR"
iphones = s.split(',') # virgülden ayırdı.
print(iphones) #2
 

# 10- yaslar dizisinin en büyük ve en küçük elemanı nedir ?
min = min(yaslar)
max = max(yaslar)

print(f"min = {min} , max = {max}") 

# 11- yaslar dizisinde kaç tane 1998 değeri vardır ?
print(yaslar.count(1998))

# 12- yaslar dizisinin tüm elemanlarını siliniz.
yaslar.clear()
print(yaslar)

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
"""" (Kendi yaptığım)
print("3 tane marka bilgisi giriniz")
print("1 =" )
one = input()
print("2 =")
two = input()
print("3 =")
three = input()
markalar = [one, two, three] #1
"""

markalars = [] # Boş liste
marka = input("İlk marka: ")
markalars.append(marka)
marka = input("İkinci marka: ")
markalars.append(marka)
marka = input("Sonuncu marka: ")
markalars.append(marka)
print(markalars)
