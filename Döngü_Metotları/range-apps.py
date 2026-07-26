# 1- Çarpım tablosu hazırlayınız.

#   BASİT YÖNTEM
# for i in range(1,11):
#     print("*********")
#     for k in range(1,11):
#         print("{} x {} = {}".format(i,k,i*k))

''' ilk 5 yan yana altına sonraki 5
for i in range(1,11):
    for k in range(1,6):
        print("{} x {} = {}".format(k,i,i*k), end=' | ')
    print()
print('***********************************************************')

for i in range(1,11):
    for k in range(6,11):
        print("{} x {} = {}".format(k,i,i*k), end=' | ')
    print()
'''
 

# 2- Girilen bir sayının asal olup olmadığını kontrol ediniz..
"""1
x = int(input("Asal kontrolü için sayı giriniz: "))

if (x <= 1):
    print("Kontrol yapılamıyor, 1'den büyük değer giriniz.")
else:
    for i in range(2,x):
        if (x % i == 0): #tam bölünüyor demek.
            print("Asal değil.")
            break
    else:
        print("asal")
"""

'''2
y = 2
if x == 1:
    print("Asal değil")
elif x <= 0 :
    print("Girilen değer negatif olamaz.")
else:
    while y < x :
        if (x % y == 0): #tam bölünüyor demek.
            print("Asal Değil.")
            break
        y += 1
    else:
        print("Asal")
'''

"""3(the best)
sayi = int(input("Sayı: "))

asalmi = True

if sayi == 1:
    asalmi = False

for i in range(2,sayi):
    if (sayi % i == 0):
        asalmi = False
        break

if asalmi:
    print(f"{sayi} asaldır.")
else:
    print(f"{sayi} asal değildir.")
"""