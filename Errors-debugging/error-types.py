"""
x = int(input("x: "))
y = int(input("y: "))

print(x / y)
"""
# bu işlemde iki farklı tür hata alabilirz
# (ZeroDivisionError) (ValueError)

#########error types##########

# SyntaxError ==> Yazım yanlışı

# hlkfslf;;
# def yazdir((:
    # pass
# print("merhab"a)


# NameError ==> tanımlanmamış değişken kullanımı

# print(ad)


# TypeError ==> hatalı parametre kullanımı
# len(5)
# 4 + 'a'

# IndexError ==> yanlış index numarası

# liste = ['merhaba']
# liste[1] ===> 0 olmalı

# ValueError ==> hatalı tip kullanımı
# int('10a')

# KeyError ==> key hatası
# d = {}
# d['ad']

# AttributeError ==> olmayan bir özelliiğe ulaşmak istediğimizde
# 'merhaba'.upper()
# 'merhaba'.Upper()


"""
pyhton built-in exceptions  ===> daha fazla hata türü için araştırılabilir.
"""