# Identity Operator: is
# Adres karşılaştırması yapılır, liste içindeki değerler aynı olabilir adres aynı değilse false.
'''
x = y = [1,2,3]
z = [1,2,3]
print(x is z) #false
print(x is y) #strue
'''
#ornek
'''
x = [1,2,3]
y = [2,4]

del x[2]
y[1] = 1
y.reverse()
print(x is y) => x, y objesi midir?
print(x is not y) => x, y objesi değil midir?
print(x==y)
'''
# iki listenin de içini benzettik ancak referantan dolayı is komutu false verdi.


# Membership Operator: in
x = ["banana", "apple"]
print("banana" in x)

name = "muhammet" #harf sorgulaması da yapabiliriz
print("m" in name)
