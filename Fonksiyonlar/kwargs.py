# def displayUser(*args):
#     print(type(args))
#     print(args)

# displayUser()

def displayUser(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print(type(kwargs ))
    print(kwargs)
    print('\n')



displayUser(username = 'Kevin', email = 'dadkevin@gmail.com')
displayUser(username = 'Kevin', email = 'dadkevin@gmail.com', country = 'USA')


def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,61,key1='value1',key2='value2')

# 10,20,30 sırasıyla a,b,c'ye gidiyor
# diğer sayılar args içinde tuple oluyor
# key-value değerleri ise dict formatına dönüşüyor

