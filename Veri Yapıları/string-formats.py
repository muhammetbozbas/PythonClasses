name = 'muhammet'  # 0
surname = 'bozbas' # 1
age = 18           # 2

print("My name is {} {}. I'm {} years old.".format(name,surname,age))
print("My name is {0} {1}. I'm {2} years old.".format(name,surname,age))
print("My name is {n} {s}. I'm {a} years old.".format(n=name,s=surname,a=age))
number = 200/700
print('the result is {n:1.5}'.format(n=number))
print('the result is {n:5.2}'.format(n=number)) 
# baştaki yer tutucudur, sonraki sayı ise virgülden sonra kaç basamak yazılacağını belirtir.
# round komutu ile yaptığımız işlemi yapmış olduk.

print(f"My name is {name} {surname}. I'm {age} years old.")
# f string dediğimiz ifade
# değişkenleri parantezlerin içine yazarız.
# int ifadeyi de yazabiliriz (age), str(age) yapmamıza gerek kalmaz.

