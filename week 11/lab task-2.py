class ShoppingCart:
    def __init__ (self,c_name, p_name, price, quantity):
        self.c_name = c_name
        self.p_name = p_name
        self.price = price
        self.quantity = quantity
    def calculate_total(self):
        total=self.quantity*self.price
        return total
    def discount(self):
        if self.calculate_total() >= 500:
            total = (self.calculate_total()*0.4)
            print("Discount: ",total)
            f_total = self.calculate_total()-total
            print("Total After Discount: ",f_total)
        else:
            print("Discount applicable only for purchese more than 500$")
    def display_info(self):
        print("Coustomer Name: ",self.c_name)
        print("Product Name: ",self.p_name)
        print("Quantity: ",self.quantity)
coustomer1 = ShoppingCart("Abdullah", "Jet", 700, 2)
coustomer1.display_info()
coustomer1.discount()
coustomer2 = ShoppingCart("Emran", "Nokia Phone", 20, 5)
coustomer2.display_info()
coustomer2.discount()

