# And => True and True => True ==> All()
# Or => True or False => True ==> Any()

sonuc = all([True,True,True]) #hepsi True ==> True çıkar  [all]
sonuc = all([True,False,False]) #hepsi True değil ==> False çıkar  [all]
sonuc = any([True,False,False]) #True var ==> True çıkar  [any]

sayilar = [0,1,2,3,5,7,61]
sonuc = [bool(sayi) for sayi in sayilar]
#[False, True, True, True, True, True]
sonuc = all([bool(sayi) for sayi in sayilar])
# False ===> 0 yüzünden hepsi True olmadığı için sonuç da False çıktı
sonuc = any([bool(sayi) for sayi in sayilar])
# True
sonuc = all([bool(sayi) for sayi in sayilar if sayi%2==0])

sonuc = [sayi%2==0 for sayi in sayilar] #sayilar içindekilerin tümü çift mi diye tek tek sorduk
sonuc = all([sayi%2==0 for sayi in sayilar]) #çıkan listedekilerin hepsinde True mu yazıyor(çift sayı mı?) diye sorduk diyebiliriz kısaca.
sonuc = any([sayi%2==0 for sayi in sayilar]) #çıkan listedekilerin herhangi biri çift mi diye sorduk diyebiliriz kısaca.


kisiler = ["ali","ahmet","çınar"]

sonuc = [kisi[0] == "a" for kisi in kisiler]
sonuc = all([kisi[0] == "a" for kisi in kisiler])
sonuc = any([kisi[0] == "a" for kisi in kisiler])


print(sonuc)
