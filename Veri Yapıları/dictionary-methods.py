opelObj = {
    "marka" : "Opel",
    "model" : "Corsa",
    "yil" : 2020
}

sonuc = opelObj["marka"]
sonuc = opelObj.get("marka") # dict içinden value çağırma işini 'get' ile de yapabiliriz.

# dict içindeki her bir elemanı x içine kopyalıyor ve ayrı ayrı yazdırıyor.
# ancak value bilgilerine ulaşamıyoruz.
for x in opelObj:
    print(x)

# bu şekilde ulaşabiliriz ==> 1.
for x in opelObj:
    print(opelObj[x])

# 2
for x in opelObj.values(): # dict.values() ile direkt value'ye kolayca ulaşabiliriz.
    print(x)

# key - value ikilisini yazdırmak istiyorsak
for x,y in opelObj.items():
    print(x,y)

# var mı yok mu
sonuc = "marka" in opelObj
print(sonuc) # True - False olarak alırız.

result = len(opelObj) # eleman sayısı
print(result)

opelObj["renk"] = "kirmizi" # olmayan değeri ekledik

"""
opelObj.pop("renk")         # yazılan değeri siler 
opelObj.popitem()           # son değeri siler 
del opelObj["marka"]        # yazılan değeri siler
del opelObj                 # name 'opelObj' is not defined
opelObj.clear()             # içini boşaltır
"""

# objeyi kopyala
obj = opelObj
obj["marka"] = "Mazda"

print(obj)
print(opelObj)
# aslında iki objenin adreslerini (referan no) kopyaladık yani
# birinde yaptığımız değişiklik ikisine de yansıdı.

obj2 = opelObj.copy() # referansı değil de kendisini kopyalamış oluruz
obj2["marka"] = "Mercedes"
print(obj)
print(obj2)

# update ile de değişiklik yapabiliriz.
opelObj.update({
    "marka": "Bmw",
    "yil": 2025,
    "renk": "Mavi"
})
print(opelObj)