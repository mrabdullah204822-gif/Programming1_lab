phone_book = {}

while True:
    name = input("Enter name: ").lower()

    if name == "stop":
        break

    phone = input("Enter phone: ")
    phone_book[name] = phone

print(phone_book)