#adında geçtiği gibi listeyi filteriyoruz
#bir listede istediğimiz özellikte olan elemanları başka bir liste şeklinde 
# çıktı olarak alıyoruz. (sadece istediğimiz kısmı alamayız, 'map' kullanılmalı.)

## eğer istersek daha sonradan 'map' kullanarak bunlar üzerinde değişiklik de yapabiliriz.

yaslar = [5,12,18,24,45]

def yetiskinmi(x):
    if x<18:
        return False
    else:
        return True
    
# for i in filter(yetiskinmi,yaslar):
#     print(i)

sonuc = list(filter(yetiskinmi,yaslar))
sonuc = list(filter(lambda x: x>=18,yaslar)) #def oluşturmak yerine bunu yaptık

sayilar = [0,1,25,6,8,9]
sonuc = list(filter(lambda x: x%2==0, sayilar)) #çiftleri buluyor.
sonuc = list(filter(lambda x: x%2!=0, sayilar)) #tekleri buluyor.

isimler = ["muhammet","sena","medine"]
sonuc = list(filter(lambda n: n[0]=="m",isimler))

#!!!#
sonuc = list(map(lambda n: n.upper(),filter(lambda n: n[0]=="m",isimler)))
# filtrelenmiş elemanlar içinden gelen değerlerin tüm harflerini büyüt dedik.

#böyle sadeleştirebiliriz.
filteredResult = filter(lambda n: n[0]=="m",isimler)
sonuc = list(map(lambda n: n.upper(),filteredResult))
 
###################
users = [
    {"username":"muhammetbozbas", "tweets": ["tweet 1","tweet 2"]},
    {"username":"senabozbas", "tweets": []},
    {"username":"medinebozbas", "tweets": ["tweet 1"]}
]
sonuc = list(filter(lambda n: len(n["tweets"])>0, users)) #tweet sayısı 0 dan büyük olanları yazdırdırır
sonuc = list(map(lambda n: n["username"].upper(),filter(lambda n: len(n["tweets"])>0, users)))
#az önce filterlediğimiz elemanların sadece username kısmını alıp büyük harfle yazdırır.

sonuc = [user for user in users if len(user["tweets"])>0] #ilk işlemin aynısı
sonuc = [user["username"].upper() for user in users if len(user["tweets"])>0] #ikinci işlemin aynısı
print(sonuc)  
