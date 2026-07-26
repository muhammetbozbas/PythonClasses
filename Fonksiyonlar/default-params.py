def selamlama(isim, mesaj):
    print(f"{mesaj}, {isim}.")

selamlama('Muhammet', 'Hoş geldiniz')
selamlama('Muhammet', 'İyi günler')
#normalde bu şekilde tanımlarız ancak mesaj kısmına bir şey yazmazsak hata alırız.
# selamlama('Muhammet')
#  TypeError: selamlama() missing 1 required positional argument: 'mesaj'

def selamlama(isim = 'Muhammet', mesaj = 'Günaydın'):
    print(f"{mesaj}, {isim}.")

selamlama() #boş olsa dahi default yazdığımızı yazar.
selamlama('Muhammet', 'Hoş geldiniz') #bir şey yazarsak da onu yazar. 

def usAlma(taban, us=2):
    return taban ** us

# eğer default ayarlama işlemini ilk parametre için yapıp ikinci için yapmazsak hata alırız.
#  SyntaxError: parameter without a default follows parameter with a default

sonuc = usAlma(2,5)
sonuc = usAlma(2)

print(sonuc)


def toplam(a,b):
    return a + b

def cikarma(a,b):
    return a - b

# def islem(a,b):
    # return toplam(a,b)  ===> burada işlemin ne olduğunu da kullanıcıdan almalıyız ki iki işlemi tek bir fonksiyona sığdırabilelim.

def islem(a,b,fn):
    return fn(a,b)   #önceden toplam yazdığım yere fn diye random bir isim yazdım ve a,b'yi de onun içine koydum.

print(islem(1,6,cikarma)) #islemi çağırdığımız için fonksiyon ismi de girmemiz gerekiyor. parantez yok=> fonksiyonu çağırmıyoruz referansı istiyoruz.
                          #parantez koysak içine değer ayrıca değer de isterdi.
                          
def islem(a,b,fn = toplam): #böyle yaptığımızda da hiçbir şey yazmadığımızda toplama yapar.
    return fn(a,b) 

print(islem(5,6))