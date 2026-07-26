class Product:
    def __init__(self, ad, fiyat,aktifmi=False):
        self.name = ad
        self.price = fiyat
        self.isActive = aktifmi
        print('product nesnesi oluşturuldu')

p1 = Product("Samsung S10", 5000,True) 
p2 = Product("IPhone 13", 34000)

print(p1.name,p1.price, p1.isActive)
print(p2.name,p2.price, p2.isActive)
