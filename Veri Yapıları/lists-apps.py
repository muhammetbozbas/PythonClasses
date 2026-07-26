# 1-  "Samsung S5,Samsung S6,Samsung S7,Samsung S8" elemanlarına sahip bir liste oluşturunuz.
phones = ['Samsung S5', 'Samsung S6', 'Samsung S7', 'Samsung S8']

# 2-  Liste Kaç elemanlıdır ?
eleman = len(phones)
print(eleman)

# 3-  Listenin ilk ve son elemanı nedir ?
print(phones[0]) # ILK
print(phones[-1]) # SON


# 4-  "Samsung S5" değerini "Samsung S9" ile değiştirin.
phones[0] = 'Samsung S9'

# 5-  "Samsung S6" listenin bir elemanı mıdır ?
if 'Samsung S6' in phones:
    print("Samsung S6 in phones")


# 6-  Listenin -3 indeksindeki değer nedir ?
print(phones[-3]) # S6

# 7-  Listenin ilk 2 elemanını alın.
print(phones[0:2])  # S9, S6

# 8-  Listenin son 2 elemanı yerine "Samsung S9" ve "Samsung S10" değerlerini ekleyin
phones[-2:] = ['Samsung S9',"Samsung S10"]

print(phones)

# 9-  Listenin üzerine "IPhone X" ve "IPhone XR" değerlerini ekleyin.
phones = phones + ["IPhone X", "IPhone XR"]
print(phones)

# 10- Listenin son elemanını silin.
del phones[-1]

# 11- Liste elemanlarını tersten yazdırınız.
print(phones[::-1]) # Baştan sona -1 artarak.

# 12- Aşağıdaki verileri bir liste içinde saklayınız. 

      # kullaniciA: Yiğit Bilgi 2010, (70,60,70)
      # kullaniciB: Sena Turan  1999, (80,80,70)
      # kullaniciC: Ahmet Turan 1998, (80,70,90) 
ogrenciA = ["Yiğit","Bilgi",2010,(70,60,70)]
ogrenciB = ["Sena","Turan",1999,(80,80,70)]
ogrenciC = ["Ahmet","Turan",1998,(80,70,90)]

list = [ogrenciA,ogrenciB,ogrenciC]

for ogrenci in list:      # the best
    ad = ogrenci[0]
    soyad = ogrenci[1]
    yas = 2025-ogrenci[2]
    ort = (ogrenci[3][0] + ogrenci [3][1] + ogrenci[3][2]) / 3
    print(f"{ad} {soyad} [{yas}] : {ort}")



# 13- Liste elemanlarını ekrana yazdırınız.
for x in list: # Rastgele bir değişken atarız. Elemanları alt alta yazdırır.
    print(x)
