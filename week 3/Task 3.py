print("------ Billing ------")
number_of_items = int(input("How many items? "))
total = 0

for item_number in range(1, number_of_items + 1):
    item_name = input(f"Item {item_number} name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    subtotal = price * quantity
    total = total + subtotal

    print(f"Subtotal: ${subtotal:.2f}")
    print()

gst = total * 0.15
final_total = total + gst

print(f"Subtotal: ${total:.2f}")
print(f"GST (15%): ${gst:.2f}")
print(f"Total: ${final_total:.2f}")