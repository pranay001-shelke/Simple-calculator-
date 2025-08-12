import tkinter as tk
from tkinter import messagebox

# Functions
def click_button(value):
    entry_field.insert(tk.END, value)

def clear_entry():
    entry_field.delete(0, tk.END)

def calculate():
    try:
        expression = entry_field.get()
        result = eval(expression)
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, result)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")
    except:
        messagebox.showerror("Error", "Invalid input.")

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry field
entry_field = tk.Entry(root, font=("Arial", 18), bd=5, relief="solid", justify="right")
entry_field.pack(fill="x", padx=10, pady=10)

# Buttons
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font=("Arial", 14), height=2, width=5,
                        command=lambda value=btn_text: calculate() if value == '=' else click_button(value))
        btn.pack(side="left", expand=True, fill="both")

# Clear button
clear_btn = tk.Button(root, text="Clear", font=("Arial", 14), height=2, bg="red", fg="white", command=clear_entry)
clear_btn.pack(fill="x")

root.mainloop()
