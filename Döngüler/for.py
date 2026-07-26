'''
list []
tuple ()
dict {} key-value
'''

numbers = [1,2,3,6,8,9]
# numbers içindeki elemanları i değişkeni içerisine tek tek atıyor.
# for i in numbers:
#     print(i)

'''
for i in numbers:
    print("Merhaba")
# liste içinde kaç eleman varsa "merhaba"yı kadar yazdırıyor.
'''

# ----names = ["ali", "deniz", "yağmur", "muhammet"]-----
# names içindeki tüm verileri isim adlı değişkene atıyor ve yazdırıyoruz
# for isim in names:
    # print(isim)

'''
-----name = "Muhammet Bozbas"----
for a in name:
    print(a)
# bu sefer de her bir karakteri tek tek attı
'''

# _tuple = [(1,2),(4,5),(6,7)] # bu bir liste ancak her bir elemanı aslında bir tuple

# for a,b in _tuple:
#     print(a,b)

_dict = {'k1':1, 'k2':2, 'k3':3}

for x in _dict: #bu döngü key değerlerini yazdırır.
    print(x)

for x in _dict: #bu ise keylerden value'ya ulaşır.
    print(_dict[x])
# önce döngüden keyleri x içine atar, sonra da "print(_dict[x])" ile key keyi sırayla _dict içine yazarak valueye ulaşır.

for x in _dict.values(): # bu metot ile de direkt value'ye ulaşabiliriz.
    print(x)

for j,l in _dict.items():
    print(j,l)