import tkinter as tk

window = tk.Tk()
window.title("Requisition System")
window.geometry("400x400")

items = []
total = 0
requisition_id = 10001


def add_item():
    item_name = item_entry.get()
    item_price = float(price_entry.get())

    items.append({
        "name": item_name,
        "price": item_price
    })

    item_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)


def calculate_total():
    global total

    total = 0

    for item in items:
        total += item["price"]

    total_label.config(text="Total: $" + str(total))


def check_approval():
    staff_id = staff_id_entry.get()

    if total < 500:
        status = "Approved"
        approval_reference = staff_id + str(requisition_id)[-3:]
    else:
        status = "Pending"
        approval_reference = "N/A"

    status_label.config(text="Status: " + status)
    reference_label.config(
        text="Approval Reference Number: " + approval_reference
    )


tk.Label(window, text="Staff Name").pack()
staff_name_entry = tk.Entry(window)
staff_name_entry.pack()

tk.Label(window, text="Staff ID").pack()
staff_id_entry = tk.Entry(window)
staff_id_entry.pack()

tk.Label(window, text="Date").pack()
date_entry = tk.Entry(window)
date_entry.pack()

tk.Label(window, text="Item Name").pack()
item_entry = tk.Entry(window)
item_entry.pack()

tk.Label(window, text="Item Price ($)").pack()
price_entry = tk.Entry(window)
price_entry.pack()

tk.Button(window, text="Add Item", command=add_item).pack(pady=10)

tk.Button(
    window,
    text="Calculate Total",
    command=calculate_total
).pack(pady=10)

tk.Button(
    window,
    text="Check Approval",
    command=check_approval
).pack(pady=10)

requisition_label = tk.Label(
    window,
    text="Requisition ID: " + str(requisition_id)
)
requisition_label.pack()

total_label = tk.Label(window, text="Total: $0")
total_label.pack()

status_label = tk.Label(window, text="Status: Pending")
status_label.pack()

reference_label = tk.Label(
    window,
    text="Approval Reference Number:"
)
reference_label.pack()

window.mainloop()