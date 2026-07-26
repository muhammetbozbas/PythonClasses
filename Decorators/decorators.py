def selamlama(fn):
    def wrapper(s):
        print("Hoş geldiniz.")
        fn(s)
        print("Görüşmek üzere.")
    return wrapper

@selamlama   #altta yaptığımız g= ... tarzı şeyleri yapmadan bu şekilde decorator kullanarak kısaltabiliriz.
def gunaydin(ad):
    print("Günaydın benim adım " + ad)

@selamlama
def iyigunler(ad):
    print("İyi günler benim adım " + ad)

# g = selamlama(gunaydin)
# i = selamlama(iyigunler)

gunaydin("Muhammet")
iyigunler("Medine")