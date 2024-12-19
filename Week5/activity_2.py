# Base class: Vehicle
class Vehicle:
    def move(self):
        pass

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Demonstrating polymorphism
def demonstrate_polymorphism(vehicles):
    for vehicle in vehicles:
        vehicle.move()

# Create objects
car = Car()
plane = Plane()
boat = Boat()

# Call the move method for each object
vehicles = [car, plane, boat]
demonstrate_polymorphism(vehicles)
