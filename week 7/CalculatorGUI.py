
import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("500x500")

tk.Label(window, text="Enter First Number:").pack()
num1 = tk.Entry(window)
num1.pack()

tk.Label(window, text="Enter Second Number:").pack()
num2 = tk.Entry(window)
num2.pack()


def add():
    try:
        number1 = float(num1.get())
        number2 = float(num2.get())

        calculation = number1 + number2

        result.config(text="Result: " + str(calculation))

    except ValueError:
        result.config(text="Please enter valid numbers.")


def sub():
    try:
        number1 = float(num1.get())
        number2 = float(num2.get())

        calculation = number1 - number2

        result.config(text="Result: " + str(calculation))

    except ValueError:
        result.config(text="Please enter valid numbers.")


def mul():
    try:
        number1 = float(num1.get())
        number2 = float(num2.get())

        calculation = number1 * number2

        result.config(text="Result: " + str(calculation))

    except ValueError:
        result.config(text="Please enter valid numbers.")


def div():
    try:
        number1 = float(num1.get())
        number2 = float(num2.get())

        if number2 == 0:
            result.config(text="Cannot divide by zero.")
            return

        calculation = number1 / number2

        result.config(text="Result: " + str(calculation))

    except ValueError:
        result.config(text="Please enter valid numbers.")


def avg():
    try:
        number1 = float(num1.get())
        number2 = float(num2.get())

        calculation = (number1 + number2) / 2

        result.config(text="Average: " + str(calculation))

    except ValueError:
        result.config(text="Please enter valid numbers.")


tk.Button(window, text="Addition", command=add).pack()
tk.Button(window, text="Subtraction", command=sub).pack()
tk.Button(window, text="Multiplication", command=mul).pack()
tk.Button(window, text="Division", command=div).pack()
tk.Button(window, text="Average", command=avg).pack()

result = tk.Label(window, text="Result:")
result.pack()

window.mainloop()
