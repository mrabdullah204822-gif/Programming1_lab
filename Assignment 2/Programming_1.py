class Requisition:
    def __init__(self, requisition_id, date, staff_id, staff_name):
        self.requisition_id = requisition_id
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"

    def add_requisition(self):
        print("Add Requisition Items")
        answer = "yes"

        while answer == "yes":
            item_name = input("Enter Item Name: ")

            try:
                item_price = float(input("Enter Item Price: "))
            except ValueError:
                print("Please enter a valid price.")
                continue

            if item_price <= 0:
                print("Price must be greater than zero.")
                continue

            item = {"name": item_name, "price": item_price}
            self.items.append(item)

            self.total = self.total + item_price

            answer = input("Add another item (yes/no): ").lower()

            while answer != "yes" and answer != "no":
                answer = input("Please enter yes or no: ").lower()

        self.total = round(self.total, 2)

        print("Total: $", self.total)
        return self.total

