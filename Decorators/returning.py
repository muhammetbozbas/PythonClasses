def usalma(number):
    def inner(power):
        return number ** power

    return inner

two = usalma(2)
three = usalma(3)
# print(three(2))
# print(two(3))

def yetki_sorgula(page):
    def inner(role):
        if role == "Admin":
            return "{0} rolü {1} sayfasına ulaşabilir".format(role,page)
        else:
            return "{0} rolü {1} sayfasına ulaşamaz".format(role,page)
    return inner

user1 = yetki_sorgula("Software Development")
# print(user1("Admin"))
# print(user1("User"))


def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
        
    def carpim(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim

    if islem_adi == "toplama":
        return toplam
    else:
        return carpim

toplama = islem("toplama")
carpim = islem("carpma")
print(toplama(10,23))
print(carpim(10,23))