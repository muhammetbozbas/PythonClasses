#glocal scope
x = 'global x'

def function():
    # local scope
    x = 'local x'
    print(x)

function()
print(x)

##################

#global 
name = 'Çınar'

def changeName(new_name):
    # local
    name = new_name
    print(name)

changeName('Ada')
print(name)


###############

name = 'global string'

def greeting():
    name = 'Muhammet'

    def hello():
        name = 'Ada'
        print('Hello ' + name)
    hello()

greeting()

################

x = 50

def test(x):
    print(f'x: {x}')

    x = 100
    print(f'x changed to {x}')
# içeride fonk. değiştirilmesi dışarıda tanımlanan fonksiyonun değerini değiştirmez.
test(x)
print(x)

#bu yüzden global keywordunu kullanmamız gerekiyor.

def test():
    global x
    print(f'x: {x}')

    x = 100
    print(f'x changed to {x}')

test()
print(x)