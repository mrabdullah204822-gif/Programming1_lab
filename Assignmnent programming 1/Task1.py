def add_requisition(counter):

    print("Enter your information:")

    date = input("Date: ")
    staff_id = input("Staff ID: ")
    staff_name = input("Staff Name: ")

    requisition_id = counter + 10000

    print("Requisition ID:", requisition_id)

    items = []
    total = 0

    print("Add items:")

    answer = "yes"

    while answer == "yes":
        item_name = input("Item Name: ")
        item_price = float(input("Item Price ($): "))

        items.append(item_name)
        items.append(item_price)

        total = total + item_price

        answer = input("Add another item (yes/no): ")

    print("Total: $", total)

    return date, staff_id, staff_name, requisition_id, items, total


counter = 1

date, staff_id, staff_name, requisition_id, items, total = add_requisition(counter)