# yaş >= 18 ve (mezuniyet == 'lise' ya da  mezuniyet == 'üniversite')

x = 8

# 1- and Operatörü (ve)

# sonuc = 5 < x < 15
sonuc = (x > 5) and (x < 15) # True ve True => True (mantıktaki 've' ile aynı) 
# biri bile false ise sonuc false olur.

hak = 3
devam = 'e'
sonuc = (hak > 0) and (devam == 'e')

# 2- or Operatörü (veya) [1 V 0 = 1]

# (x > 0) => pozitif
# (x % 2 == 0) => çift
sonuc = (x > 0) or (x % 2 == 0) # biri bile doğru olsa yeter

# not Operatörü => ifadenin değilini alır.
sonuc = not(x >  0) # 'x sıfırdan büyük değil mi?' (soruyu tersten sormak için)

# x, 5-10 arasında bir çift sayı mı ?

sonuc = ((x>5) and (x<10)) and (x % 2 == 0)

print(sonuc)

