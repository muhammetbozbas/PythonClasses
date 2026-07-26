def do_twice(func):
    def wrapper_do_twice(*args,**kwargs):  #farklı türde değişken sayıda param gönderilebilmesi için (**args,**kwargs)
        return func(*args,**kwargs)
        func(*args,**kwargs)
    return wrapper_do_twice

@do_twice
def hello():
    print("Hello")

@do_twice
def greet(msg):
    print("Hello" , msg)

@do_twice
def return_greeting(name):
    print("greeting function")
    return f"Hello, {name}."

# hello()
# greet("world")

# return_greeting("Muhammet")
print(return_greeting("Muhammet"))