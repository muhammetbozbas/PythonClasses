# kodu istediğimiz bir satırda durdurup oraya kadar değişkenlerin
#   almış oldukları değerleri görebiliriz.
"""
import pdb

one = 'one'
two = 'two'
pdb.set_trace()
sonuc = one + two

three = 'three'
sonuc += three
print(sonuc)
"""
# l => list
# n => next line
# p => print
# c => contunie

def add_numbers(a,b,c):
    import pdb; pdb.set_trace()
    return a+b+c

print(add_numbers(1,2,3))