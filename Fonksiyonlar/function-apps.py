# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 
'''
def kelime(txt, adet):
    print(txt,adet)    

kelime('merhaba \n', 3) 
'''

# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.
"""
def hesapla(kenar1, kenar2):
    alan = kenar1 * kenar2
    cevre = 2 * (kenar1 + kenar2)

    return f"Alan: {alan}, Çevre: {cevre}"

print(hesapla(3,5))
"""

# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)
"""
def yaziTura():
    k = ['yazi', 'tura']
    import random
    print(random.choice(k))

yaziTura()
"""

'''
def yaziTuraAt():
    import random
    sayi = random.random() #bize 0 ile 1 arasında rastgele float bir sayı verir.

    if sayi > 0.5:
        return 'Tura'
    else:
        return 'Yazı'

print(yaziTuraAt())
'''

# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.
#asalları liste formatında yazan ifade.
def asal(ilk,ikinci):
    asalmi = True
    asallar = []
    while ilk <= ikinci:
        for i in range(2,ilk):
            if ilk % i != 0:
                asalmi = True
            else:
                asalmi = False
                break
        if asalmi:
            asallar.append(ilk)
        ilk += 1
    print(asallar)
# asal(2,100)

#asalları tek tek alt alta yazdıran ifade
def asalBul(a,b):
    for k in range(a,b+1):
        if k > 1:
            for i in range(2,k):
                if k % i == 0:
                    break
            else:
                print(k)
                    
asalBul(10,20)


# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.

def bolen(sayi):
    bolenler = []
    for k in range(1,sayi):
        if sayi % k == 0:
            bolenler.append(k)
    return bolenler

print(bolen(10))



