# Base class Vehicle
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.__speed = 0  # Stronger encapsulation with __ (private attribute)

    def describe(self):
        return f"This is a {self.make} {self.model}."

    # Getter for speed (encapsulation)
    def get_speed(self):
        return self.__speed

    # Setter for speed with validation
    def set_speed(self, speed):
        if speed >= 0:
            self.__speed = speed
        else:
            print("Speed cannot be negative.")

    def drive(self):
        print(f"The {self.make} {self.model} is now driving at {self.__speed} km/h.")

# Subclass Car (inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors  # New attribute specific to Car

    # Overriding the describe method (Polymorphism)
    def describe(self):
        return f"This is a {self.make} {self.model} car with {self.num_doors} doors."

    def open_doors(self):
        print(f"Opening {self.num_doors} doors of the car.")

# Subclass Bike (inherits from Vehicle)
class Bike(Vehicle):
    def __init__(self, make, model, has_gear):
        super().__init__(make, model)
        self.has_gear = has_gear  # New attribute specific to Bike

    # Overriding the describe method (Polymorphism)
    def describe(self):
        gear_status = "has gears" if self.has_gear else "does not have gears"
        return f"This is a {self.make} {self.model} bike that {gear_status}."

    def drive(self):  # Overriding drive method to show different behavior
        print(f"The {self.make} {self.model} bike is now pedaling at a steady speed.")

# Example Usage
my_car = Car("Toyota", "Corolla", 4)
print(my_car.describe())
my_car.set_speed(60)
my_car.drive()
my_car.open_doors()

my_bike = Bike("Giant", "Escape 3", True)
print(my_bike.describe())
my_bike.set_speed(20)
my_bike.drive()
