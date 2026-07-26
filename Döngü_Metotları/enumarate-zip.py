markalar = ["opel", "bmw", "mercedes"]

"""
index = 0
for marka in markalar:
    print(f"{index + 1}-{markalar[index]}")
    index += 1
"""

#enumarate
'''
obj1 = enumerate(markalar) #her elemana bir index numarası veriyor.

print(type(obj1))
print(list(obj1))

for index,value in enumerate(markalar):
    print(f"{index + 1}-{value}")

for index,value in enumerate(markalar,1): #direkt başlamasını istediğimiz sayıyı da yazabiliriz.
    print(f"{index}-{value}")
'''

#zip

liste1 = [1,2,3,4,5]
liste2 = ['a','b','c','d','e','f']
liste3 = [100,200,300,400,500]

print(list(zip(liste1,liste2,liste3))) #liste1 den liste2'ye elemanları tek tek eşleştiriyor. Arta kalanları göz ardı etti ('f')

for item in zip(liste1,liste2):
    print(item)

for a,b,c in zip(liste1,liste2,liste3):
    print(f"{a}-{b}-{c}")
