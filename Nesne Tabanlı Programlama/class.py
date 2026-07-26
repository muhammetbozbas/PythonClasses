# Class

class Ogrenci:
    # method ==> fonksiyon
    # attribute ==> değişken
    pass

# Object, Instance

ogrenci1 = Ogrenci()
ogrenci2 = Ogrenci()

# print(type(ogrenci))  # <class '__main__.Ogrenci'>
# print(ogrenci1, ogrenci2)        # <__main__.Ogrenci object at 0x1009646e0> <__main__.Ogrenci object at 0x100ba4550>


class Product:
    pass

p1 = Product() # samsung
p2 = Product() # iphone
p3 = Product() # xiaomi

products = [p1,p2,p3]

for p in products:
    print(p)
    print(type(p))

""" ciktisi
<__main__.Product object at 0x102fcc830>
<class '__main__.Product'>
<__main__.Product object at 0x102fbc690>
<class '__main__.Product'>
<__main__.Product object at 0x102fbc7d0>
<class '__main__.Product'>
"""