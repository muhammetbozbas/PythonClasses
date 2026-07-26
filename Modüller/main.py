import module

sonuc = module.sayi
sonuc = module.sayilar
sonuc = module.ogrenci["ad"]
sonuc = module.ogrenci["notlar"]
sonuc = module.topla(10,20)


import module as m  #module ==> m

sonuc = m.sayilar

from module import ogrenci  #büyük dosyalarda daha etkili olacaktır.

from module import ogrenci, topla, sayi  #birkaç tanesini birlikte ekleyebiliriz


sonuc = ogrenci
sonuc = topla(10,20)


from module import *  #tüm içeriği import ettik.

sonuc = sayi
sonuc = ogrenci["notlar"]
 
print(sonuc)

