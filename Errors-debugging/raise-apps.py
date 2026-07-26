#  benim çözümlerim
# 1- Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin.

"""
import math
def fact(a):
    if a is not int:
        raise TypeError("int değer girmelisiniz")
    if a < 0 :
        raise ValueError("negatif sayıların faktöriyeli alınmaz!")
    
    sonuc = math.factorial(a)
    print(sonuc)

# fact("a")
# fact(-5)
# fact(5.4)

"""


# 2- Girilen parola içinde türkçe karakter hatası veriniz.
turkceKarakterler = ("ç","ü","ğ","ş","ö")

passw = input("sifre giriniz: ")
for p in passw:
    if p in turkceKarakterler:
        raise TypeError("Turkce karakter kullanmayınız!!")
    


#   hoca çözümleri
# 1- Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin.

# def faktoriyel(x):
#     x = int(x)

#     if (x<0):
#         raise ValueError("Negatif değer")

#     sonuc = 1
#     for i in range(1, x+1):
#         sonuc *= i

#     return sonuc

# for i in [5,7,'a',2,-4,'10a']:
#     try:
#         x = faktoriyel(i)
#     except ValueError as e:
#         print(e)
#         continue
#     else:
#         print(x)

# 2- Girilen parola içinde türkçe karakter hatası veriniz.

def parolaKontrol(parola):
    turkce_karakterler = "şçğüöıİ"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Parola türkçe karakter içeremez.")

    print('geçerli parola')

parola = input('parola: ')

try:
    parolaKontrol(parola)
except TypeError as e:
    print(e)
