def get_items():
    items = {}

    while True:
        item = input("Enter item name: ").strip()

        if item == "done":
            break

        price = float(input("Enter price: "))
        items[item] = price

    return items


def print_items(items):
    print("Items:")
    total = 0

    for item in items:
        price = items[item]
        print(item, f"{price:g}")
        total = total + price

    print(f"Total = {total:g}")