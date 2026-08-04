class Product:
    def __init__(self,name,price,id):
        self.name = name
        self.price = price
        self.id = id

p1 = Product("Samsung S10",5000,1)
p2 = Product("Samsung S11",7000,2)

# products = [p1.__dict__,p2.__dict__]
products = {
    p1.id:
        p1.__dict__,
    p2.id:
        p2.__dict__}



import json

with open("products.json","w") as file:
    json.dump(products,file,indent=2)

with open("products.json") as file:
    data = json.load(file)

urunler = []

# for p in data:
#     urunler.append(Product(p["name"],p["price"]))
#     print(p)

for key,value in data.items():
    urunler.append(p1)
    print(urunler)