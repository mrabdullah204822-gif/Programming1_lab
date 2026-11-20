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

    def requisition_approval(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
        else:
            self.status = "Pending"
            self.approval_reference = "Not available"

    def respond_requisition(self, choice):
        if self.status == "Pending":
            if choice == "1":
                self.status = "Approved"
                self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
                print("Requisition Approved")

            elif choice == "2":
                self.status = "Not approved"
                self.approval_reference = "Not available"
                print("Requisition Not approved")

            elif choice == "3":
                print("Requisition remains Pending")

            else:
                print("Invalid choice")

        else:
            print("This requisition is not Pending")

    def display_requisition(self):
        print("--------------------------------")
        print("Date:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)

        print("Requisition Items:")

        for item in self.items:
            print(item["name"], "- $", item["price"])

        print("Total: $", self.total)
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_reference)

    def display_requisitions(self, requisitionlist):
        print("Printing Requisitions:")

        for requisition in requisitionlist:
            requisition.display_requisition()

    def requisition_statistics(self, requisitionlist):
        total_requisitions = len(requisitionlist)
        approved = 0
        pending = 0
        not_approved = 0

        for requisition in requisitionlist:
            if requisition.status == "Approved":
                approved += 1

            elif requisition.status == "Pending":
                pending += 1

            elif requisition.status == "Not approved":
                not_approved += 1

        print("Displaying the Requisition Statistics")
        print("Total number of requisitions submitted:", total_requisitions)
        print("Total number of approved requisitions:", approved)
        print("Total number of pending requisitions:", pending)
        print("Total number of not approved requisitions:", not_approved)

        return total_requisitions, approved, pending, not_approved

