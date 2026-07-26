class Person:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Person nesnesi türetildi")

    def intro(self):
        print(self.name, self.surname, self.age)

class Student(Person):   #bu sekilde person içinde bir student nesnesi türetebiliriz.
    pass

class Teacher(Person):
    pass

p1 = Person("Ahmet","Turan",20)
p1.intro()

s1 = Student("Ali", "Yilmaz", 25)
s1.intro()

t1 = Teacher("Can", "Yilmaz", 35)
t1.intro()