# Destede kalan kart sayısı için kartSayisi() isminde bir metot.
# Destedeki kartları karıştırmak için KartlariKaristir() isminde bir metot.
# kartDagit() ismindeki metot belirtilen adet kadar kartı dağıtmalıdır. Destedeki kalan kart sayısına dikkat.
# kartAt() ismindeki metot elden bir kart atmak için kullanılsın.

class Kart:
    def __init__(self,tip,deger):
        self.tip = tip
        self.deger = deger

    def __repr__(self):
        return f"{self.tip} {self.deger}"

import random
class Deste:
    types = ['karo','sinek','kupa','maça']
    values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    
    def __init__(self):
        self.cards = [Kart(t,y) for t in Deste.types for y in Deste.values]
        
    def kartSayisi(self):
        kartSayi = len(self.cards)
        return kartSayi

    def KartlariKaristir(self):
        if (len(self.cards)) < 52:
            raise ValueError("You cannot mix the cards, game is started already")
        random.shuffle(self.cards)

    def kartDagit(self,adet):
        kartsayisi = self.kartSayisi()
        if kartsayisi == 0:
            raise ValueError("There is not more card.")
        adet = min([kartsayisi,adet]) #ikisi arasından minimumu seçer. (önlem olmuş olur)
        inHand = self.cards[-adet:]
        self.cards = self.cards[:-adet]
        return inHand
        
    def kartAt(self):
        return self.kartDagit(1)[0]   # [0] atılan kart parantezden çıksın diye
        



deste1 = Deste()
deste2 = Deste()

print(deste1.kartSayisi())

# deste1.KartlariKaristir()
print(deste1.cards)
print(deste1.kartDagit(7))
# print(deste1.cards)

print(deste1.kartAt())
# print(deste1.cards)





