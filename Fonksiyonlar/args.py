
list = (10,20,30,40)

def toplam(sayilar ):
    sonuc = 0
    for i in sayilar:
        sonuc += i
    return sonuc

print(toplam(list))


def toplam(*args):  #aslında *args argümanların takma adı olmuş oluyor. (*) değişken sayıda eklediğimizi belirtiyor.
    print(type(args)) #<class 'tuple'>
    print(args)
    sonuc = 0
    for i in args:
        sonuc += i 
    return sonuc

print(toplam(10,20))