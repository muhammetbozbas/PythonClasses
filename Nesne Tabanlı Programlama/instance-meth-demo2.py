# car class
# brand, model, year, speed
# accelerate and brake


class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Speed: {self.speed}"
    
    def accelerate(self, amount):
        self.speed += amount
        
    
    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0
        

c1 = Car("Toyota","Corolla",2001)

c1.accelerate(50)
print(c1.display_info())
c1.brake(60)
print(c1.display_info())

