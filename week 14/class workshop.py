class InventoryManagement:
    def __init__ (self):
        self.productlist=[]
        self.salelist=[]
        self.product_id=1
    def product_registration(self):
        name=input("Enter the product name")
        for product in self.productlist:
            if product["name"].lower() == name.lower():
                print("Product", {product["name"]}, "name is already registered")
                return
        price=float(input("Enter the product price"))
        stock=int(input("Enter the number of stock"))
        product = {"ID": self.product_id, "name": name, "price": price, "stock": stock}
        self.productlist.append(product)
        print("Product registered successfully")
        print("Product ID:", self.product_id)
        self.product_id += 1
    def update_stock(self):
        product_id=int(input("PLZ enter the product ID: "))
        for product in self.productlist:
            if product["ID"]==product_id:
                quantity = int(input("Enter the new stock quantity"))
                product["stock"]=quantity
                print ("Stock Updated sucecessfully and new stock: ", product["stock"])
                return
        print("Product not found")
    def sell_product(self):
        id = int(input("Enter the product ID to sell"))
        qunty_sales = int(input("Enter the quantity to sell: "))
        for product in self.productlist:
            if product["ID"]==id:
                new_stock=product["stock"] - qunty_sales
                product["stock"]=new_stock
                total = qunty_sales*product["price"]
                sale={"ID":id, "Quantity":qunty_sales, "total":total}
                self.salelist.append(sale)
        print("Product not found")
    def search_product(self):
        id = int(input("Enter the product ID: "))
        for product in self.productlist:
            if product["ID"] == id:
                print("Product ID:", product["ID"])
                print("Product Name:", product["name"])
                print("Product Price:", product["price"])
                print("Stock Quantity:", product["stock"])
                return
        print("Product not found")
    def display_summary(self):
        total_products = len(self.productlist)
        total_items = 0
        total_sales = 0
        for sale in self.salelist:
            total_items += sale["Quantity"]
            total_sales += sale["total"]
        print("Total number of products:", total_products)
        print("Total items sold:", total_items)
        print("Total sales value:", total_sales)
        for product in self.productlist:
            print("Product Name:", product["name"])
            print("Current Stock:", product["stock"])
    def menu(self):
        while True:
            print("Product Management System")
            print("1: Add Product")
            print("2: Update Stock")
            print("3: Sell Product")
            print("4: Search Product")
            print("5: View Sales Summary")
            print("6: Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.product_registration()
            elif choice == "2":
                self.update_stock()
            elif choice == "3":
                self.sell_product()
            elif choice == "4":
                self.search_product()
            elif choice == "5":
                self.display_summary()
            else:
                break
system = InventoryManagement()
system.menu()
