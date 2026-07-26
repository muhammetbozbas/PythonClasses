name = "muhammet"
surname = "bozbas"
age = "18"

msg = "my name is " + name + " and my surname is " + surname + '.'

print(len(msg)) #kaç karakter olduğunu öğreniriz.
print(msg)
print(msg[0]) #0'dan soldan başlar, -1 ile de sağdan başlar (m)
print(msg[-1]) #sağdan başlar (.)
print(msg[-45]) # m 
print(msg[0:5]) # 0 ile 5 arasındaki karakterleri yazar.
print(msg[:15]) #en baştan 15'e kadar => ilkini yazmadık.
print(msg[15:]) # 15'ten sona kadar => sonuncuyu yazmadık.
print(msg[-46:-1]) # aynısını eksili değerleri ile yazdık.
# son yazdığımız karakter dahil edilmez!
print(msg[0:20:2]) # artış sayısı normalde 1'dir, ancak biz değiştirebiliriz.
print(msg[::5]) # baştan sona kadar yazar, adım sayısı farklıdır.
print(msg[::-1]) # baştan sona kadar tersten yazar.








