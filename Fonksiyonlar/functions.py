# herhangi bir class ile ilişkisi yok sen tanımlayacaksın
# arada boşluk yok, sayısal ifadeyle başlamayacak.
# mesela önceden tanımlanan append metodunu istediğimiz kadar kullanabildiğimiz gibi bu kendi oluşturduğumuzu da istediğimiz kadar kullanabiliriz.

def selamlama():
    print('merhaba')
# selamlama()

"""
for i in range(11): # döngüye alıp bu şekilde 10 kere merhaba yazdırabiliriz.
    selamlama()
"""

#bunu oluştururken döngüyü fonksiyon içine de koyabilirdik:
'''
    def selamlama():
        for i in range(11):
            print('merhaba')
    selamlama()
'''

def topla():
    a=1
    b=2
    print(a+b)

topla()