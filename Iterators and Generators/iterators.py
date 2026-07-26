# iterable? ==> yinelenebilir demek. Yani içinde tek tek dolaşabiliriz. Listeler gibi


sayilar = [1,2,3,4,5]
isim = "Sena"
a = 10
dict = {
    "ad":"muhammet",
    "soyad": "bozbas"
}

# for i in sayilar:
    # print(i)

# print(dir(sayilar)) #==> __iter__ var
# print(dir(isim)) #==> __iter__ var
# print(dir(a)) #==> __iter__ yok
# print(dir(dict)) #==> __iter__ var


# iterator?

# for döngüsü bizim için iterator tanımlar ve dolaşır
#peki biz nasıl yaparız?

"""
sayilar = [1,2,3,4,5]

iterator = iter(sayilar) #listeler iterator değildir, önce iterator tanımladık.

while True:
    try:
        sayi = next(iterator)
        print(sayi)
    except StopIteration:
        break
"""

#geliştirelim

sayilar = [1,2,3,4,5]
s = "Sena"

def my_func(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            sayi = next(iterator)
            func(sayi)
        except StopIteration:
            break

# my_func(sayilar, print)
# my_func(s, print)

def kare_al(x):
    print(x*x)

my_func(sayilar,kare_al)

