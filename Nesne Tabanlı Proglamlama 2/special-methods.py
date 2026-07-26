liste = [1,2,3]
# print(len(liste))


s = "Hello World"
# print(len(s))

class Film:
    def __init__(self,baslik,yonetmen,sure):
        self.baslik = baslik
        self.yonetmen = yonetmen
        self.sure = sure
    
    def __str__(self):
        return f"{self.baslik}, {self.yonetmen} tarafindan yonetildi."

    def __repr__(self):
        return f"{self.baslik}, {self.yonetmen} tarafindan yonetildi."
    
    def __len__(self):
        return self.sure

    def __del__(self):
        print("film objesi silindi") #kullanıldıktan hemen sonra bellekten silindiği için bu yazı her çalıştırıldığında yazacaktır. İlla da del kullanmamıza gerek yok.    
f = Film("film adi","yonetmen adi",120)

print(str(f))
print(len(f)) # (__len__) kullandığımzı için burada sanki filmin uzunluğunu normal len kullanarak soruyor gibi kullanbiliriz

