liste = ["1","2","5a","10b","abc","10","50"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz
"""
for s in liste:
    try:
        sonuc = int(s)
        print(sonuc)
    except ValueError:
        continue
"""

# 2: Kullanıcı 'quit (q)' değerini girmedikçe aldığınız her inputun sayı 
# olduğundan emin olunuz aksi halde hata mesajı yazın.

"""
while True:   
    x = input("Sayi: ")
    if (x=='q'):
        break

    try:
        sonuc = float(x)
        break
    except ValueError:
        print("hatalı sayı")
        continue
"""

# 3: Dictionary ve key bilgilerini parametre olarak alan get(d, key)
# fonksiyonu hazırlayınız.
urun = {"urunAdi":"samsung s10"}

# d["fiyat"] => KeyError

# get(d, "fiyat") => None
# get(d, "urunAdi") => samsung S10


""" benim yaptığım (mantık sıfır)
def urunler(a,b):    
    sonuc = a.get(b)
    print(sonuc)

try:
    urunler(urun,'urunAdi')
except NameError:
    print('urun bulunamadı')
"""

'''
def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None
    
print(get(urun,'urunAdi'))
'''