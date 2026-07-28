# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.
# "r": okuma modu => belirtilen konumda dosya olmalıdır.

f = open("msg.txt")  #bunun çalışması için ilgili dosya mutlaka aynı dizinde olmalıdır.

# print(f) # <_io.TextIOWrapper name='msg.txt' mode='r' encoding='UTF-8'>
# print(help(f))
print(f.read())


# read metodu ilk çalıştırıldığında baştan sona okur, tekrar çalışırsa ise kaldığı yerden 
#devam eder. 