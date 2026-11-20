class supermarket:
    def __init__ (self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def add_item(self, amount):
        self.quantity = self.quantity + amount
    def remove_item(self,amount):
        self.quantity = self.quantity - amount

    def calculate_total(self):
        total=self.price*self.quantity
        return total
    def display_info(self):
        print("Name: ",self.name)
        print("Price: ",self.price)
        print("Quantity: ",self.quantity)
        #print("Total: ",total)
coustomer1 = supermarket("Bread ", 3, 2)
#coustomer1.display_info()
coustomer2 = supermarket("Pen", 5, 6 )
#coustomer2.display_info()
coustomer1.add_item(5)
coustomer1.display_info()
n1=coustomer1.calculate_total()
n2=coustomer2.calculate_total()
g_tototal = n1+n2