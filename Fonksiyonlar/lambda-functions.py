# lambda parameter: (expression) !parametreler paranteze alınmaz!

# sonuc = (lambda a: a**2)(4)
# print(sonuc)

#
multiply = lambda a: a**2
sonuc = multiply(5)
#

#
toplama = lambda a,b,c: (a+b+c)
sonuc = toplama(1,4,7)
#

#
tersCevir = lambda str: str[::-1]
sonuc = tersCevir("Muhammet")
#

def myFunc(n):
    return lambda a: a*n

multiply2 = myFunc(2) #2 ile çarpar
multiply3 = myFunc(3) #3 ile çarpar

sonuc = multiply2(10) #10*2
sonuc = multiply3(10) #10*3
sonuc = multiply3(20) #20*3

print(sonuc)

""" aynı işlemi lambda kullanmadan böyle yaparız
def my(n):
    def multi(k):
        return k * n 
    return multi    #dışa return etmezsen fonk bir şey döndürmez
    
mk = my(2)
print(mk(3))
"""

