# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price  # Private attribute to demonstrate encapsulation

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Price must be a positive value.")

    def display_info(self):
        print(f"Smartphone: {self.brand} {self.model}, Price: ${self.__price}")

# Subclass: Smartwatch
class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, battery_life):
        super().__init__(brand, model, price)
        self.battery_life = battery_life

    def display_info(self):
        super().display_info()
        print(f"Battery Life: {self.battery_life} hours")

# Creating objects
phone = Smartphone("Apple", "iPhone 14", 999)
watch = Smartwatch("Samsung", "Galaxy Watch 6", 299, 48)

# Demonstrate encapsulation
phone.display_info()
phone.set_price(899)
print(f"Updated Price: ${phone.get_price()}")

# Demonstrate inheritance
watch.display_info()
