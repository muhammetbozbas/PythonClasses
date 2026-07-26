# list
# tuple
# dictionary
# sets => indexlenemez, sıralanamaz

meyveler = {"elma", "armut", "üzüm", "kavun"} 
sebzeler = {"bezelye", "soğan"}

'''
for x in meyveler:
    print(x)
'''
# sonuc = meyveler[0]  (indexlenemez)
sonuc = "elma" in meyveler # bu şekilde kontrol edebiliriz.
meyveler.add("karpuz") # güncelleyemeyiz ama sonradan eleman ekleyebiliriz.
meyveler.update(["vişne", "kavun"]) # birden fazla da eleman ekleyebiliriz, aynı eleman iki defa yazılmaz
sonuc = len(meyveler) # eleman sayısını sorgulayabiliriz. 

meyveler.remove("karpuz") # eleman silebiliriz.
#silmeye çalıştığımız eleman listede yoksa 'KeyError' hatası verir.
meyveler.discard("vişne") # siler.
meyveler.discard("vişşne") # eleman listede yoksa bile hata vermez.
# remove ile discardın farkı remove hata veriyor, discard vermiyor.
# (aranan eleman listede yoksa)

sonuc = meyveler.pop() # silinen eleman yazdırılır, neyi sileceğini bilemeyiz.

"""
meyveler.clear() # seti temizler (boşaltır)
"""
sonuc = meyveler

sonuc = meyveler.union(sebzeler) # iki seti birleştirir.
# tekrarlayan eleman varsa 1 kere yazılır.






print(sonuc)
