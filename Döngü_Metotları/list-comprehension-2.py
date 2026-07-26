# for item in liste:
#     if (koşul):
#         expression

# [expression for item in liste if (koşul)]

sayilar = [1,5,8,9,15,62]
sonuc = []
 
# for sayi in sayilar:
#     if (sayi % 2 == 0):
#         sonuc.append(sayi)

sonuc = [sayi*2 for sayi in sayilar if (sayi % 2 == 0)] # sayılar çift demek. Uyguladığımız koşul liste için geçerli.
sonuc = [sayi if sayi % 2 == 0 else 'tek sayi' for sayi in sayilar] # Uygulanan filtre tüm sayılar için geçerli oldu tek olanlar yerine 'tek sayi' yazdı.

''' 
fiyatlar = [1000,3000,5000,0,4000]
vergiler = []

# for fiyat in fiyatlar:
#     if fiyat > 0:
#         vergiler.append(fiyat * 1.18)
#     else:
#         print('Vergi Hesaplanmadı.')

vergiler = [fiyat * 1.18 for fiyat in fiyatlar if fiyat>0]
#fiyatlar içinden fiyatı 0'dan büyük olan değerleri hesaplayıp yazdırdı
vergiler = [fiyat * 1.18 if fiyat > 0 else 'vergi hesaplanmadı' for fiyat in fiyatlar] 
#fiyat değeri 0 olan için 'fiyat hesaplanmadı' yazdırdık diğerlerine aynı işlem uygulandı.

print(vergiler)  
'''
## --for kullanarak iç içe döngüler--
# sonuc = []
# for x in range(3):
#     for y in range(3):
#         sonuc.append((x,y))

# print(sonuc)

sonuc = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(sonuc)