isimler = ["Ahmet","ali","Çınar","DeNiz"]
string = "Hello 123456 World."
yillar = [1983, 1999, 2008, 1956, 1986]
dereceler = [20,5,15,-2,0,-6]

# 1- "1-100" arasındaki sayılardan 12' e tam bölünebilen sayı listesi oluşturunuz.
'''
result = [sayi for sayi in range(1,101) if sayi % 12 == 0]
result = [sayi for sayi in range(1,101) if sayi%3==0 if sayi%4==0] #12'ye bölünebilme kuralını kullandık.
print(result)
'''
# 2- isimler listesindeki her ismi küçük harfe çevirip tersten yazdınız.
"""
sonuc = [isim.lower()[::-1] for isim in isimler]
print(sonuc)
""" 
#!! 3- verilen "string" içindeki rakamları içeren bir liste oluşturunuz.
'''
result = [rakam for rakam in string.split() if rakam.isdigit()] #rakam.isdigit() ==> int ifade mi diye sorar True değer aldıklarını listeye aktarır.
print(result)
'''

# 4- "yillar" dizisindeki her doğum yılı için yaş bilgisini içeren liste oluşturunuz.
'''
import datetime
yıl = datetime.datetime.now().year

age = [yıl-yas for yas in yillar]
print(age)
'''

# 5- "dereceler" listesinde bulunan hava sıcaklık bilgisine göre eksi değer için buzlanma tehlikesi yazdırınız.
ice = [buz if (buz >= 0) else 'buzlanma tehlikesi olan değer' for buz in dereceler]
print(ice)
