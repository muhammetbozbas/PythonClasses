"""
class Product:
    def __init__(self,name,price):
        self.name = name
        if price >= 0:
            self._price = price
        else:
            raise ValueError("fiyat için negatif değer ataması yapılamaz.")
    
    def set_price(self,value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("fiyat için negatif değer ataması yapılamaz.")

    def get_price(self):
        return self._price
    
p1 = Product("IPhone 13", 34000)
# p1._price = -34000 ===> bu şekilde negatif değer atanabilir, önüne geçmek için _price dedik
#işaretlemiş olduk. (private object)
print(p1.get_price())
# p1.set_price(-1300) ==> ValueError
  
"""
  #### bunlarla uğraşmamak için property kullanabiliriz.

class Product:
    def __init__(self,name,price,description):
        self.name = name
        self.description = description
        if price >= 0:
            self._price = price
        else:
            raise ValueError("fiyat için negatif değer ataması yapılamaz.")
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("fiyat için negatif değer ataması yapılamaz.")
        
    #an another example
    @property
    def short_description(self):
        return self.description[:10] #slicing işlemi.
    
    # def set_price(self,value):
    #     if value >= 0:
    #         self._price = value
    #     else:
    #         raise ValueError("fiyat için negatif değer ataması yapılamaz.")

    # def get_price(self):
    #     return self._price

p1 = Product("IPhone 13", 34000,"iphone 13 apple'ın çıkardığı en kral telefondur.")
# p1.price = -123443
print(p1.price)
print(p1.short_description)