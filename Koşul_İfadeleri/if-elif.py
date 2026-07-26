# if bloğuna ekstra soru sormak için "elif" kullanılır.
# normalde if false değeri getirirse else'e atlardı ancak
#   bazı durumlarda ekstra soru sormamız gerekebilir
#   biz de elif bloğunu yazarak if false verdiğinde elif'ten soru ekleyebiliriz.
'''
x = 20
y = 20

if (x > y):
    print("x, y'den büyüktür.")
elif (x == y):
    print("x, y'ye eşittir.")
else:
    print("y, x'ten büyüktür.")
'''

sayi = int(input("Enter a number: "))
if (sayi > 0):
    print("The number is positive")
elif (sayi == 0):
    print("THE NUMBER İS = '0'")
else:
    print("The number is negative")
