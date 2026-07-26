#   YONTEM 1
# import math

# value = dir(math)
# value = help(math)
# value = help(math.factorial)

# value = math.sqrt(49) #karekök alır
# value = math.factorial(5) #faktöriyel alır
# value = math.floor(5.9) #aşağı yuvarlar ==> 5.9 == 5
# value = math.ceil(5.9) #yukarı yuvarlar ==> 5.1 == 6

import math as islem
value = islem.factorial(5)   #bu sayede verdiğimiz takma isim ile module ulaşabildik


#   YONTEM 2

# from math import *  #hepsini import ettik

from math import factorial, sqrt

def sqrt(x):
    print('x : '+ str(x))
#hangisi aşağıdaysa o kullanılır, aynı isim olsa bile

# value = factorial(5)
value = sqrt(16)
# value = ceil(9.8)

print(value)