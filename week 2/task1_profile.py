def add_requisition():
    counter = 10000

    print("Enter requisition details")

    requisition_date = input("Date: ")
    employee_id = input("Staff ID: ")
    employee_name = input("Staff Name: ")

    counter += 1
    req_id = counter

    print("Requisition ID:", req_id)

    requisition_items = []
    requisition_total = 0

    answer = "yes"

    while answer.lower() == "yes":
        product_name = input("Item Name: ")
        product_price = float(input("Item Price ($): "))

        requisition_items.append({
            "name": product_name,
            "price": product_price
        })

        requisition_total += product_price

        answer = input("Add another item (yes/no): ")

    print("Total:", requisition_total)

    return (
        requisition_date,
        employee_id,
        employee_name,
        req_id,
        requisition_items,
        requisition_total
    )