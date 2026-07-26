class Person:

    # yapıcı metotlar (constructor)
    def __init__(self,name,surname,year):
        
        # object attributes, instance attributes
        self.name = name
        self.surname = surname
        self.year = year
    #instance methods
    def intro(self):
        return f"My name is {self.name} and surname is {self.surname}."
    
    def calculate_age(self):
        return f"Age: {2026 - self.year}"

# Object, Instance
p1 = Person("Muhammet","Bozbas",2007)
p2 = Person("Sena","Bozbas",2007)


print(p1.intro())
print(p1.calculate_age())

print(p2.intro())
print(p2.calculate_age())