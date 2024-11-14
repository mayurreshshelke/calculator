import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def button_click(item):
    current = entry_text.get()
    entry_text.set(current + str(item))

# Function to clear the input field
def clear():
    entry_text.set("")

# Function to all clear the input field
def all_clear():
    entry_text.set("")

# Function to calculate the expression
def calculate():
    try:
        result = eval(entry_text.get())
        entry_text.set(result)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
    except Exception:
        messagebox.showerror("Error", "Invalid Input")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.config(bg="#333333")
root.resizable(0, 0)

# Entry field to display the expression/result
entry_text = tk.StringVar()
entry = tk.Entry(
    root, textvariable=entry_text, font=('Arial', 24), bg="#222222", fg="white",
    bd=0, insertwidth=4, width=14, borderwidth=8, relief="groove"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)

# Define button colors
button_bg = "#4CAF50"    # Button background
button_fg = "white"      # Button text color
operator_bg = "#FF9500"  # Operator button color
clear_bg = "#FF3B30"     # Clear button color
equal_bg = "#1E90FF"     # Equals button color
ac_bg = "#D9534F"        # All Clear button color

# Button Layout
buttons = [
    ('AC', 1, 0), ('%', 1, 1), ('C', 1, 2), ('/', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('00', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3),
]

# Create and place buttons with styling
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(
            root, text=text, font=('Arial', 18), bg=equal_bg, fg=button_fg,
            command=calculate, relief="ridge", bd=0, activebackground="#1E90FF", activeforeground="white"
        )
    elif text == 'C':
        button = tk.Button(
            root, text=text, font=('Arial', 18), bg=clear_bg, fg=button_fg,
            command=clear, relief="ridge", bd=0, activebackground="#FF6347", activeforeground="white"
        )
    elif text == 'AC':
        button = tk.Button(
            root, text=text, font=('Arial', 18), bg=ac_bg, fg=button_fg,
            command=all_clear, relief="ridge", bd=0, activebackground="#D9534F", activeforeground="white"
        )
    elif text in {'+', '-', '*', '/', '.'}:
        button = tk.Button(
            root, text=text, font=('Arial', 18), bg=operator_bg, fg=button_fg,
            command=lambda t=text: button_click(t), relief="ridge", bd=0, activebackground="#FF9500", activeforeground="white"
        )
    else:
        button = tk.Button(
            root, text=text, font=('Arial', 18), bg=button_bg, fg=button_fg,
            command=lambda t=text: button_click(t), relief="ridge", bd=0, activebackground="#4CAF50", activeforeground="white"
        )
    
    # Place button with padding and adjust size
    button.grid(row=row, column=col, ipadx=20, ipady=20, padx=5, pady=5, sticky="nsew")

# Adjust grid to make buttons stretchable
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the application
root.mainloop()
