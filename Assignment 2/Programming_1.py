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

requisitionlist = []
requisition_id = 10001

while True:
    print("========== Requisition System ==========")
    print("1. Submit New Requisition")
    print("2. Display All Requisitions")
    print("3. Manager Response")
    print("4. Requisition Statistics")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Enter your information")

        date = input("Enter Date: ")
        staff_id = input("Enter Staff ID: ")
        staff_name = input("Enter Staff Name: ")

        requisition = Requisition(requisition_id, date, staff_id, staff_name)

        print("Requisition ID:", requisition.requisition_id)

        requisition.add_requisition()
        requisition.requisition_approval()

        requisitionlist.append(requisition)

        print("Requisition submitted successfully.")
        print("Requisition ID:", requisition.requisition_id)
        print("Total: $", requisition.total)
        print("Status:", requisition.status)
        print("Approval Reference Number:", requisition.approval_reference)

        requisition_id += 1

    elif choice == "2":
        if len(requisitionlist) == 0:
            print("No Requisitions Submitted.")

        else:
            requisitionlist[0].display_requisitions(requisitionlist)

    elif choice == "3":
        try:
            req_id = int(input("Enter Requisition ID: "))
        except ValueError:
            print("Please enter a valid Requisition ID.")
            continue

        found = False

        for requisition in requisitionlist:
            if requisition.requisition_id == req_id:
                found = True

                if requisition.status == "Pending":
                    print("1. Approve")
                    print("2. Not approved")
                    print("3. Keep Pending")

                    decision = input("Enter your choice: ")
                    requisition.respond_requisition(decision)

                else:
                    print("This requisition is not Pending")

                break

        if found == False:
            print("Requisition ID not found.")

    elif choice == "4":
        if len(requisitionlist) == 0:
            print("Displaying the Requisition Statistics")
            print("Total number of requisitions submitted:", 0)
            print("Total number of approved requisitions:", 0)
            print("Total number of pending requisitions:", 0)
            print("Total number of not approved requisitions:", 0)

        else:
            requisitionlist[0].requisition_statistics(requisitionlist)

    elif choice == "5":
        print("Thank you for using Requisition System.")
        break

    else:
        print("Please enter a valid choice.")