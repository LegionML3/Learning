# Question: We have a class defined for vehicles.
# Create two new vehicles called car1 and car2. 
# Set car1 to be a red convertible worth $60,000.00 with a name of 
# Fer, and car2 to be a blue van named Jump worth $10,000.00.

# code:

class vehicle:
    def __init__(self, color, type, price, name):
        self.color = color
        self.type = type
        self.price = price
        self.name = name

car1 = vehicle("red", "convertible", 60000.00, "Fer")
car2 = vehicle("blue", "van", 10000.00, "Jump")

print(f"Car 1: {car1.name}, Color: {car1.color}, Type: {car1.type}, Price: ${car1.price}")
print(f"Car 2: {car2.name}, Color: {car2.color}, Type: {car2.type}, Price: ${car2.price}")