
import tkinter as tk

window = tk.Tk()
window.title("Supermarket GUI")
window.geometry("500x500")

tk.Label(window, text="Enter Item Name:").pack()
item_name = tk.Entry(window)
item_name.pack()

tk.Label(window, text="Enter Item Price:").pack()
item_price = tk.Entry(window)
item_price.pack()

item_pr = {}


def add():
    name = item_name.get()
    price = item_price.get()

    if name.strip() == "":
        result.config(text="Please enter an item name.")
        return

    try:
        price = float(price)
    except ValueError:
        result.config(text="Please enter a valid price.")
        return

    if price < 0:
        result.config(text="Price cannot be negative.")
        return

    item_pr[name] = price

    result.config(text="Item added successfully.")

    item_name.delete(0, tk.END)
    item_price.delete(0, tk.END)


def calculate_total():
    total = 0

    for price in item_pr.values():
        total = total + price

    result.config(text="Total Price: $" + str(round(total, 2)))


def display_item():
    cont_text = ""

    for name, price in item_pr.items():
        cont_text = cont_text + name + ": $" + str(price) + "\n"

    result.config(text=cont_text)


tk.Button(window, text="Add Item", command=add).pack()
tk.Button(window, text="Calculate Total", command=calculate_total).pack()
tk.Button(window, text="Display Items", command=display_item).pack()

result = tk.Label(window, text="Result:")
result.pack()

window.mainloop()
