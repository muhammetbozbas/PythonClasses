class Person:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Person nesnesi türetildi")

    def intro(self):
        print(self.name, self.surname, self.age)

class Student(Person):   #bu sekilde person içinde bir student nesnesi türetebiliriz.
    # def __init__(self, name, surname, age, number):
    #     Person.__init__(self,name, surname, age)
    #     self.number = number
    #     print("Student nesnesi türetildi.")

    def __init__(self, name, surname, age, number):
        super().__init__(name, surname, age)
        self.number = number
        print("Teacher nesnesi türetildi.")
    
    def intro(self):
        print(self.name, self.surname, self.age, self.number)

    def study(self):
        print(f"{self.number} is studying right now.")

class Teacher(Person):
    # def __init__(self, name, surname, age, branch):
    #     Person.__init__(self,name, surname, age)
    #     self.branch = branch
    #     print("Teacher nesnesi türetildi.")

    def __init__(self, name, surname, age, branch):
        super().__init__(name, surname, age)
        self.branch = branch
        print("Teacher nesnesi türetildi.")
    
    def teach(self):
        print(f"{self.name} teacher is teaching {self.branch} at the moment.")

p1 = Person("Ahmet","Turan",20)
p1.intro()

s1 = Student("Ali", "Yilmaz", 25, 476)
s1.intro()
s1.study()

t1 = Teacher("Can", "Yilmaz", 35, "Math")
t1.intro()
t1.teach()