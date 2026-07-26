"""
liste = [3,5,7,9]

for i in liste:
    print(i)

    
# for ile kolayca yazdırabiliriz. (elimizde bir liste varken)
# ya yoksa
"""

'''
r = range(10)
r = range(100)
r = range(10,50)
r = range(100, 10, -2)
r = range(0,-10,-1)

sonuc = list(r)
print(sonuc)
'''

# for i in range(10,15):
#     print(i)

# for i in range(50,100,10):
#     print(i)

for i in range(100,200): #100-200 arasındaki çift sayılar.
    if (i%2==0):
        print(i)
   