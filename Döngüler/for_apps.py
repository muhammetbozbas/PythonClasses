sayilar = [1,5,16,35,57,72,75,10]

# 1- sayilar listesindeki her bir elemanı yazdırın.
'''
for k in sayilar:
    print(k)
'''
# 2- Sayilar listesindeki hangi sayılar 5'in katıdır ?
'''
for k5 in sayilar:
    if (k % 5 == 0):
        print(k5)
'''    
#---not first---- 3- Sayilar listesinde sayıların toplamı kaçtır ?
'''
toplam = 0
for sayi in sayilar:
    toplam = toplam + sayi
print(toplam)
'''

# 4- Sayilar listesindeki çift sayıların karesini alınız.
'''
for kare in sayilar:
    if (kare % 2 == 0):
        print(kare,":", kare ** 2)
'''

urunler = ['iphone 8 ','iphone 7','iphone X','iphone XR','samsung S10']
# 5- urunler listesindeki tüm ürünlerin 2.karakterlerini ekrana yazdırın.
'''
for y in urunler: #ikinci karakter 1. indexte olur ve liste olduğu için bu şekilde buluruz.
    print(y[1])
'''

#------not first--6- urunler listesinde içinde 'iphone' geçen kaç ürün vardır? (index,find)
count = 0
for phone in urunler:
    index = phone.find("iphone") #find yerine index kullansaydık bulamadığı zaman hata verirdi.
    if (index >= 0): # index > -1 de olurdu.
        count = count + 1 # count += 1 (kolay yol)
print(count)

'''
count diye bir variable oluşturup sıfıra eşitledik,
urunler içindeki her bir değeri phone adlı farklı bir variable içine attık,
index diye farklı bir variable oluşturup phone'a attığımız değerlerden 'iphone' olanları buldurduk,
if bloğu kullanarak 'iphone' olan değerlerden alacağımız '1' cevabını kullanarak bir toplama kurduk,
index -1'den büyükse count bir artacaktı,
en sonunda da ilk oluşturduğumuz değişkeni doldurup yazdırdık.
'''