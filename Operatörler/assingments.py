# a = 5
# b = 10
# c = 20

a, b, c = 5, 10, 20

a, b = b, a   # a ile b'yi yer değiştirir.

a += 5   # a = a + 5
a -= 5   # a = a - 5
a *= 5   # a = a * 5
a /= 5   # a = a / 5
a %= 5   # a = a % 5 (mod alma) (bölümden kalan alma)
a **= 5  # a = a ** 5 (üs alma)
a //= 5  # a = a // 5 (tam bölme)

'''
values = (1,2,3)
(a,b,c) = values
print(a,b,c)

'''

values = (1,2,3,4,5)
a, b, *c = values
print (a, b, c)
# bu durumda artan fazlalık ifadeleri '*' sayesinde c içine atar
a, b, *c = values # ilk ikisi a,b de kalanlar c
a, *b, c = values # ilki a sonu c kalanlar b
*a, b, c = values # son iki b, c kalanlar a

