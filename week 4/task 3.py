shopping_list = []

while True:
    item = input("Enter item: ")

    if item == "done":
        break

    shopping_list.append(item)

print("Shopping List:", shopping_list)
print("First two items:", shopping_list[:2])
print("Last item:", shopping_list[-1:])

if len(shopping_list) > 0:
    shopping_list.pop()

print("Shopping List:", shopping_list)