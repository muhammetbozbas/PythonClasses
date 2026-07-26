website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
exapmle = ' Hello World '
result = exapmle.strip() 
print(result)

ex2 = website.strip('elh') # İçeriye yazdığımız karakterleri siler.
print(ex2)


# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
k = 'www.sadikturan.com'
msg = k.replace('www.','').replace('.com','') #1
print(msg)


l = "www.sadikturan.com".strip("w.com") # 2, silme komutudur, parantez içi boşsa boşlukları siler, doluysa yazılanı siler.
print(l)


# 3- 'kursAdi' karakter dizisinin tüm karakterlerini küçük harf yapın.
sonuc = kursAdi.lower()
print(sonuc)

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a')) 
four = website.count('a') # Count, saydırma komutudur. İçindekinden kaç tane olduğunu söyler. 
print(four)
four2 = website.count('www', 0,10) # 0 ve 10 arası arar.
print(four2)

# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
five = website.startswith("www")
five2 = website.endswith("com")

print(five)
print(five2)

# 6- 'website' içinde '.com' ifadesi var mı?
six = website.find('com') # Kaçıncı indexten itibaren var olduğunu yazdırır. Eğer yoksa '-1' yazdırır.
print(six)                # rfind veya lfind olarak da yazabiliriz. Aradığımız ifade  birden fazla varsa ve diğerini bulmak istiyorsak işe yarar.
six2 = website.index('www')
print(six2)               # 'index' ile ararsak da aynısı olur ancak aradığımız yoksa 'Value Error' hatası alırız.

# 7- 'kursAdi' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
seven = kursAdi.isalpha()  # tüm karakterler alfabetik mi ? (t-f)
seven2 = kursAdi.isdigit() # tüm karakterler sayısal mı ? (t-f)
print(seven)
print(seven2)

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
eight = 'Contents'.center(50, '*') # Ortalıyor
eight2 = 'Contents'.ljust(50, '*') # Soldan
eight3 = 'Contents'.rjust(50, '*') # Sağdan

print(eight)
print(eight2)
print(eight3)


# 9- 'kursAdi' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
nine = kursAdi.split() #1
print(nine)
nine2 = '-'.join(nine)
print(nine2)


nine3 = kursAdi.replace(' ', '-') #2
print(nine3)



# 10-'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
x = "Hello World"
ten = x.replace('Hello', 'There')
print(ten)


# 11-'kursAdi' karakter dizisini boşluk karakterlerinden ayırın.
kursAdi = kursAdi.lower().replace(':','') #1
eleven = kursAdi.split()
print(eleven)

print(kursAdi.lower().replace(',','').split()) #2, her şeyi tek satıra sığdırabiliriz.