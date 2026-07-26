# 1: sayilar listesini while ile ekrana yazdırın.
sayilar = [4,6,9,10,35,57,89,125,244]
'''------!!!!interesting!!!!-------
i = 0
while (i < len(sayilar)):
    print(sayilar[i])
    i += 1
--------------------------------
'''
# while sayilar:
#     print(sayilar.pop()) #listeyi sondan silerek yazar. içeri 0 yazarsak da baştan silerek sırayla yazar.


# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları 
# ekrana yazdırın.
"""
a = int(input("1. değer: "))
b = int(input("2. değer: "))

x = a  #kullanıcının yazdığı değeri değiştirmemek için yeni bir değişken oluşturduk.
while x < b:
    if (a%2==1):
        print(x)
    x += 1
"""    


# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
"""
sayi = 100
while sayi > 0:
    print(sayi)
    sayi -=1
"""
# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
'''
sayi = []
while len(sayi) <= 4: #index numarasına göre düşün
    sayi.append(input("sayi giriniz: "))
    print(sayi)
'''

sayilar = []
i = 0
while (i<5):
    sayi = int(input("sayi: "))
    sayilar.append(sayi)
    i += 1
sayilar.sort() 
print(sayilar)