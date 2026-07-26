# Deste sınıfı

# kart tipleri   => karo,sinek,kupa,maça
# kart değerleri => A,2,3,4,5,6,7,8,9,10,J,Q,K

# Deste sınıfındaki kartlar listesine 52 kartı for ve list comprehension ile ekleyin


class Kart:
    def __init__(self,tip,deger):
        self.tip = tip
        self.deger = deger

    def __repr__(self):
        return f"{self.tip} {self.deger}"
    
class Deste:
    types = ['karo','sinek','kupa','maça']
    values = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
    def __init__(self):
        self.cards = [Kart(t,y) for t in Deste.types for y in Deste.values]
        print(self.cards)
        

deste1 = Deste()
deste2 = Deste()
    
    