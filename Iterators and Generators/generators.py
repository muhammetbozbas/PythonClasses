# Every generator is an iterator, but not every iterator is a generator.
#iterator kullanırken her şeyi tek tek yazıyorduk(__iter__, __next__)
#generatorde yalnızca tek komutla arka planda bunların oluşturlmasını sağlıyoruz(yield)

def sayi_say(max):
    sayi = 1
    while sayi <= max:
        yield sayi
        sayi += 1

# for i in sayi_say(10):  
#     print(i)

#kendimiz yapalım...

"""
iterator = sayi_say(10)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
"""
# print(list(iterator)) ==> bunu kullanarak da liste içine alırız.

##list comprehension ile de yapabiliriz.
#eğer normal parantez ile list comp. yaparsak generator oluşturmuş oluruz. Tamamen baştan fonk. oluşturmaya gerek yok.

generator = (i for i in range(1,11))  
# print(generator) ==> <generator object <genexpr> at 0x1029e4ee0>


while True:
    try:
        print(next(generator))
    except StopIteration:
        break