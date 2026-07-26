def greeting(name):
    print("hello", name)

# print(greeting("ali"))
# print(greeting)

sayHello = greeting #adresler aynı oldu

del sayHello  #greetinge bir şey olmaz
# print(sayHello)

#encapsulation
def outer(num1):
    print("outer")
    def inner_increment(num1):
        print("inner")
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1 ,num2)

# outer(10)
# inner_increment(10)   # NameError: name 'inner_increment' is not defined

def factorial(number):
    if not isinstance(number,int):
        raise TypeError("Number must be an integer.")
    def inner_fact(number):
        if 0 < number <= 1:
            return 1
        elif number < 0:
            raise ValueError("Factorial is not defined for negative numbers.")

        return number * factorial(number-1)    # n * (n-1)!
    return inner_fact(number)

# print(factorial(-6))

try:
    print(factorial(5))
except Exception as ex:
    print(ex)

