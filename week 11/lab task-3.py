class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print("Product:", self.name)
        print(f"Price: ${self.price}")
        print("Quantity:", self.quantity)

    def add_quantity(self, amount):
        self.quantity = self.quantity + amount

    def remove_items(self, amount):
        if amount > 0 and amount <= self.quantity:
            self.quantity = self.quantity - amount
        else:
            print("Cannot remove that quantity")

    def calculate_total(self):
        return self.price * self.quantity


bread = Product("Bread", 3, 2)
milk = Product("Milk", 4, 1)
apples = Product("Apples", 2, 3)
bananas = Product("Bananas", 1, 4)

print("Starting products")
bread.display_info()
milk.display_info()
apples.display_info()
bananas.display_info()

print()
print("Updated quantities")
milk.add_quantity(2)
milk.display_info()

bread.add_quantity(3)
bread.display_info()

apples.add_quantity(2)
apples.display_info()

print()
print("Removing apples")
apples.remove_items(2)
apples.display_info()
apples.remove_items(10)

bread.quantity = 2
milk.quantity = 3
apples.quantity = 2

print()
print(f"Bread total: ${bread.calculate_total()}")

basket = [bread, milk, apples]
bill = 0

print()
print("================================")
print("        MY SUPERMARKET")
print("================================")

for product in basket:
    product.display_info()
    item_total = product.calculate_total()
    print(f"Total: ${item_total}")
    print()

    bill = bill + item_total

print("--------------------------------")
print(f"TOTAL BILL: ${bill}")
print("================================")
print("Thank you for shopping!")