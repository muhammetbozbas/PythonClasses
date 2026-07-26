a, b, c = 2, 5, 12

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile a,b,c toplamının farkı nedir ?
'''
print("İki sayı giriniz")
first = int(input("1 => "))
second = int(input("2 => "))
print(first * second) - (a + b + c))
'''

# 2- c' nin  b' ye kalansız bölümünü hesaplayınız.
print(c//b) 
# 3- (a,b,c) toplamının mod 3' ü nedir ? (bölümünden kalan al)
result = (a + b + c) % 3
print(result)
# 4- b' nin a. kuvvetini hesaplayınız.
us = b ** a
print(us)


sayilar = 1, 5, 7, 10, 3
# 5- a, *b, c = sayilar işlemine göre c' nin küpü kaçtır ? 
a, *b, c = sayilar
print(a,b,c)
print(c ** 3)
# 6- a, *b, c = sayilar işlemine göre b nin değerleri toplamı kaçtır ?
a, *b, c = sayilar # burada b değişkeni liste oluyor ve
toplam = (b[0] + b[1] + b[2]) # burada da listede toplama yapıyoruz.
print(toplam)