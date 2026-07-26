# break => ona geldiği zaman döngüyü tamamen bitirir.
# continue => kendisinden sonraki satırları çalıştırmadan tekrar döndürür.



"""
name = "Muhammet Bozbaş"

for harf in name:
    if (harf == "e"):
        continue # e'ye geldiği zaman continue kod satırı çalışır ve buna denk geldiği anda döngü başa atlar sonrakiler yazdırılmaz. 
    # print(harf)

for harf in name:
    if (harf == "e"):
        break   #e ye kadar olan harfleri yazdırır ve döngüden çıkar.
    print(harf)

"""

# i = 0
# while (i < 5):
#     if (i == 3):
#         break
#     print(i)
#     i += 1
# print("döngü bitti.")


# 1-100 arasındaki çift sayılar toplamı
i = 0
toplam = 0
while (i <= 100):
    i += 1
    if (i%2==1):
        continue
    toplam += i
        
print(f"Toplam: {toplam}")


