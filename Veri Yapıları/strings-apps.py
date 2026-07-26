website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Proglamlama."

# 'kursAdi' karakter dizisinde kaç karakter bulunmaktadır ?
print(len(kursAdi)) # len ile karakter sayısını öğreniriz.

total = len(kursAdi)
print(total)

# 'website' içinden www karakterlerini alın
print(website[7:10])

# 'website içinden com karakterlerini alın
print(website[-3:])

# 'kursAdi içinden ilk 15 ve son 15 karakterlerini alın.
print(kursAdi[:15])
print(kursAdi[0:15])
print(kursAdi[-15:])

# 'kursAdi ifadesindeki karakterleri tersten yazdırın.
result = kursAdi[::-1]
print(result)

# 'Hello world' içindeki w ifadesini W ile değiştirin.
m = 'W'
print("Hello {}orld ".format(m)) #1

s = 'Hello world'
s = s[0:6] + 'W' + s[-4:] #2


# abc ifadesini yan yana 3 defa yazdırın.
numbers = 'abc '
print(numbers * 3)

name, surname, age, job = 'Sadık','Turan', 37 ,'öğretmen'
# Yukarıdaki verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
# 'Benim adım Sadık Turan, Yaşım 37 ve mesleğim öğretmen.'

sonuc = "Benim adım " + name + ' ' + surname + ', Yaşım ' + str(age) + ' ve mesleğim ' + job + '.'
sonuc2 = "Benim adım {} {}, Yaşım {} ve mesleğim {}.".format(name,surname,age,job)
sonuc3 = f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}. "

print(sonuc)
print(sonuc2)
print(sonuc3)




