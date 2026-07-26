msg = "   Welcome to our python course, I'm Muhammet."

result = msg.upper() # Tüm harfleri büyük harf yapar.
quest = msg.isupper() # "is" soru sorar, her harfi büyük mü ?
result2 = msg.lower() # Tüm harfleri küçük harf yapar.
result3 = msg.title() # Her kelimenin baş harfini büyük yapar.
result4 = msg.capitalize() # Yalnızca cümlenin baş harfini büyük harf yapar.
result5 = msg.strip() # Baş ve sondaki boşlukları siler(içi boşken). İçine ne yazılırsa onu siler.
result6 = msg.split() # Cümle dizi haline gelir, her kelimeyi bir eleman olarak alır. "[]"
extraresult6 = msg.split(',') # Virgüle kadar iki elemanlı dizi olarak ayırır.
extraresult6_1 = '-'.join(result6) # Her kelimeyi ayrı eleman almıştık, şimdi de onları '-' ile ayırdık.
index = msg.index('our') # Belirli bir yerin index numarasını bulur. (Kaçıncı karakterde olduğu)
result7 = msg.startswith("W") # Hangi harf ile başladığına t-f olarak cevap verir. (boşlukla başlıyor.)
result7_1 = msg.endswith(".")  # Ne ile bittiğine cevap verir.
result8 = msg.replace("Muhammet","Osman") # İlk yazdığım kelimeyi ikinciyle değiştirir. 
result8_1 = msg.lower().replace(' ','-').replace('.','') # Harfleri küçülttü, boşluğu '-' yaptı, noktaları kaldırdı.



print(result) 
print(quest)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(extraresult6)
print(extraresult6_1)
print(index)
print(result7)
print(result7_1)
print(result8)
print(result8_1)
 