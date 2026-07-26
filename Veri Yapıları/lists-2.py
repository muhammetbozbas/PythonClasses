diller = ['Python', 'C#', 'Java', 'Javascript']
 
sonuc = diller
sonuc = type(diller) # List
sonuc = diller[0:2] # 0 ile 2. index arasını alır (0,1),  2 dahil değil
sonuc = diller[2:]  # 2 ile sonuna kadar alır.
# İLK YAZILAN DAHİLDİR İKİNCİ DEĞİLDİR!!     
sonuc = diller[-4:-1]
sonuc = diller[:-2]

# diller[0] = 'Html'  # 0. indexi 'Html' ile değiştirir.
diller[-1] = 'Html' 
sonuc = diller

sonuc = len(diller)  # Eleman sayısını yazdırır.

sonuc = diller + ['Angular', 'Vuejs']  # Liste içine eleman eklerken '+' kullanarak ekleyebiliriz.

# if bloğu => koşul ifadeleri
if 'Python' in diller:
    print("Değer, listenin bir elemanıdır.")

# Döngüler => diller içerisindeki elemanları alt alta yazdırdı.
for x in diller:
    print(x)

del diller[0]  # diller içerisindeki 'Python' elemanını del ile sildirdik.
sonuc = diller




print(sonuc)

