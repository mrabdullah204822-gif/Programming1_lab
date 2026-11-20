    item_message.config(text="Item Added")


def calculate_total():
    global total

    total = 0

    for price in prices:
        total = total + price

    total_output.config(text=str(total))


def check_approval():
    status = "Pending"
    reference = "N/A"

    if total < 500:
        status = "Approved"
        last_three = str(requisition_id)[-3:]
        reference = staff_id_box.get() + last_three

    status_output.config(text=status)
    reference_output.config(text=reference)


tk.Label(window, text="Staff Name:").grid(row=0, column=0)
staff_name_box = tk.Entry(window)
staff_name_box.grid(row=0, column=1)

tk.Label(window, text="Staff ID:").grid(row=1, column=0)
staff_id_box = tk.Entry(window)
staff_id_box.grid(row=1, column=1)

tk.Label(window, text="Date:").grid(row=2, column=0)
date_box = tk.Entry(window)
date_box.grid(row=2, column=1)

tk.Label(window, text="Item Name:").grid(row=3, column=0)
item_box = tk.Entry(window)
item_box.grid(row=3, column=1)

tk.Label(window, text="Item Price:").grid(row=4, column=0)
price_box = tk.Entry(window)
price_box.grid(row=4, column=1)

add_button = tk.Button(window, text="Add Item", command=add_item)
add_button.grid(row=5, column=0)

total_button = tk.Button(window, text="Calculate Total", command=calculate_total)
total_button.grid(row=5, column=1)

approval_button = tk.Button(window, text="Check Approval", command=check_approval)
approval_button.grid(row=6, column=0, columnspan=2)

item_message = tk.Label(window, text="")
item_message.grid(row=7, column=0, columnspan=2)

tk.Label(window, text="Requisition ID:").grid(row=8, column=0)
id_output = tk.Label(window, text=str(requisition_id))
id_output.grid(row=8, column=1)

tk.Label(window, text="Total:").grid(row=9, column=0)
total_output = tk.Label(window, text="0")
total_output.grid(row=9, column=1)

tk.Label(window, text="Status:").grid(row=10, column=0)
status_output = tk.Label(window, text="Pending")
status_output.grid(row=10, column=1)

tk.Label(window, text="Approval Reference Number:").grid(row=11, column=0)
reference_output = tk.Label(window, text="")
reference_output.grid(row=11, column=1)

window.mainloop()