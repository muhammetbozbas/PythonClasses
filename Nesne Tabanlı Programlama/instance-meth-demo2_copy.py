# car class
# brand, model, year, speed
# accelerate and brake

# add engine and fuel mechanism

class Car:
    def __init__(self,brand,model,year,mpg):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
        self.engine = False
        self.fuel = 100
        self.MPG = mpg #fuel efficiency for km

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Engine: {self.engine}, Speed: {self.speed}, Fuel: {int(self.fuel)}, Fuel Efficiency(MPG): {self.MPG}"
    
    def start_stop(self, x):
        if x == "start":
            self.engine = True
        elif x == "stop" and self.speed == 0:
            self.engine = False
        else:
            print(f"Try Again. Engine Condition is {self.engine}")

    def accelerate(self, amount, time):
        if self.engine == True:
            # km1 == 500  # maximum range
            km1 = (amount * time) / 2 
            if km1 <= 500:
                self.speed += amount # speed changing
                print(f"{km1}. km")

                self.fuel = 100 - (km1 / self.MPG) *2 
                if self.fuel <= 0 :
                    self.fuel = 0
                
                if self.fuel == 0:
                    print(f"Fuel: {self.fuel}, please go to fuel station")
            else:
                print("Wrong input. This car's range is 500km.")
                self.engine = False  #it had stopped the car
        else:
            print("---Start the Engine---")
            
    
    def brake(self, amount, time):
        if self.engine == True:
            km1 = (amount * time) / 2 
            if km1 <= 500:
                self.speed -= amount # speed changing
                print(f"{km1}. km")

                self.fuel = 100 - (km1 / self.MPG) *2 
                if self.fuel <= 0 :
                    self.fuel = 0
                
                if self.fuel == 0:
                    print(f"Fuel: {self.fuel}, please go to fuel station")
        else:
            print("---Start the Engine---")

        if self.speed < 0:
            self.speed = 0


        

c1 = Car("Toyota","Corolla",2001,15)

c1.start_stop("start")
print(c1.display_info())
c1.accelerate(100,4)
print(c1.display_info())
# c1.brake(50,1)
# print(c1.display_info())
