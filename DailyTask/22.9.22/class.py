class Car:
    
    def __init__(self, name, mileage):
        self.name = name 
        self.mileage = mileage 

    def description(self):                
        return f"The {self.name} car gives the mileage of {self.mileage}km/l"

Honda = Car("Honda City", 24.1)
print(Honda.description())