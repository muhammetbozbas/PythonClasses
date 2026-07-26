# (1 - sonsuz) aralığındaki her sayının karesini getiren fonksiyon.

def my_func():
    x = 0
    while True:
        yield x*x # ====> yield 'ı geriye döndürmek istediğim değerle kullanıyorum. return gibi.
        x += 1

# gen = my_func() #referansını alıyoruz.
# while True:
#     print(next(gen))

"""
gen = (i for i in my_func())
while True:
    print(next(gen))
"""

"""
# This creates an infinite generator of squares using itertools.count
import itertools

squares_gen = (x * x for x in itertools.count(0))

print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
print(next(squares_gen))  # 4
"""
# Fibonacci serisini hem normal hem de generator fonk. ile oluşturun.
"""
x = 1
y = 1
while True:
    print(x)
    print(y)
    x = x + y
    y = x + y
"""
# def fibo():
#     x = 1
#     y = 1
#     print(x)
#     print(y)
#     while True:
#         x = x + y 
#         y = x + y
#         yield x
#         yield y

# gen = fibo()
# k = 0
# while True:
#     print(next(gen))


## liste şeklinde fibo serisi
def fibo_list(max):
    sayilar = []
    a, b = 0, 1
    while len(sayilar) <= max:
        sayilar.append(b)
        a, b = b, a+b
    return sayilar
print(fibo_list(15))

# def fibo_baba(max):
#     a, b = 0, 1
#     count = 0
#     while count < max:
#         a, b = b, a+b
#         yield b
#         count += 1

# gen = fibo_baba(15)
# while True:
#     try:
#         print(next(gen))
#     except StopIteration:
#         break


# Performans testlerini yapın.

import sys
liste = [i**2 for i in range(100000)]
# print(sys.getsizeof(liste)) # ==> 800984

liste2 = (i**2 for i in range(100000))
# print(sys.getsizeof(liste2)) # ==> 208

import time

list_start_time = time.time()
sum([i**2 for i in range(500000000)])
list_stop = time.time() - list_start_time

gen_start_time = time.time()
sum((i**2 for i in range(500000000)))
gen_stop = time.time() - gen_start_time

# print(list_stop, gen_stop)
# 78.61348700523376, 17.42286777496338 
#fark çok belirgin

#generator kullanarak ramdan çok fena tasarruf ediyoruz.
# büyük dosyaları okuma sırasında bu kullanım çok işe yarayacaktır.