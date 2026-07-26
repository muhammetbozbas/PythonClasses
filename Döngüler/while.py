sayilar = [2,5,7,9]

# for => collection
#   bir liste, grup için kullanılır

# while => koşul için kullanılır.
#   ... olduğu sürece demektir, koşul True sonucunu verdiği sürece uygulama çalışır
# control + c ile uygulamayı durdurabilirsin
'''
i = 0 #döngüyü kontrol etmek için bir kontrol değişkenine ihtiyacımız var
while i <= 100:
    if (i%2==1):
        print("tek sayı:",i)
    else:
        print("çift sayı:",i)
    i += 1
'''

username = ''

while not username:
    username = input("username: ")

print(f"hi {username}")