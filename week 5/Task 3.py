items = {}

while True:
    item = input("Enter item name: ")

    if item == "done":
        break

    price = float(input("Enter price: "))
    items[item] = price

print("Items entered:")
total = 0

for item in items:
    price = items[item]
    print(item, f"{price:g}")
    total = total + price

print(f"Grand total = {total:g}")