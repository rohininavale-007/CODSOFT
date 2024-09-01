# Make a gui calculator using python.

import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x250")  # Set the initial window size
        self.root.resizable(False, False)  # Make the window non-resizable

        # Create a frame for the input fields
        self.input_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.input_frame.pack(fill="x", padx=10, pady=10)

        # Create labels and entry fields for numbers
        self.num1_label = tk.Label(self.input_frame, text="Number 1:", font=("Helvetica", 12))
        self.num1_label.pack(side="left", padx=5)
        self.num1_entry = tk.Entry(self.input_frame, font=("Helvetica", 12), width=20)
        self.num1_entry.pack(side="left", padx=5)

        self.input_frame2 = tk.Frame(self.root, bg="#f0f0f0")
        self.input_frame2.pack(fill="x", padx=10, pady=10)

        self.num2_label = tk.Label(self.input_frame2, text="Number 2:", font=("Helvetica", 12))
        self.num2_label.pack(side="left", padx=5)
        self.num2_entry = tk.Entry(self.input_frame2, font=("Helvetica", 12), width=20)
        self.num2_entry.pack(side="left", padx=5)

        # Create a label and option menu for operation choice
        self.operation_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.operation_frame.pack(fill="x", padx=10, pady=10)

        self.operation_label = tk.Label(self.operation_frame, text="Operation:", font=("Helvetica", 12))
        self.operation_label.pack(side="left", padx=5)
        self.operation_var = tk.StringVar()
        self.operation_var.set("+")  # Default operation is addition
        self.operation_menu = tk.OptionMenu(self.operation_frame, self.operation_var, "+", "-", "*", "/")
        self.operation_menu.pack(side="left", padx=5)

        # Create a button to perform the calculation
        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate, bg="#4CAF50", fg="#ffffff", font=("Helvetica", 12))
        self.calculate_button.pack(fill="x", padx=10, pady=10)

        # Create a label to display the result
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.result_label.pack(fill="x", padx=10, pady=10)

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    messagebox.showerror("Error", "Cannot divide by zero!")
                    return

            self.result_label.config(text=f"Result: {result:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()