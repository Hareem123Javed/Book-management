# app/views/fine_calculation.py

import tkinter as tk
from tkinter import ttk
from datetime import datetime

class FineCalculatorWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Fine Calculator")
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Fine Calculation", font=("Arial", 16)).pack(pady=10)

        frame = ttk.Frame(self.root)
        frame.pack(pady=10)

        ttk.Label(frame, text="Due Date (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
        self.due_date_entry = ttk.Entry(frame)
        self.due_date_entry.grid(row=0, column=1, padx=5)

        ttk.Label(frame, text="Return Date (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5)
        self.return_date_entry = ttk.Entry(frame)
        self.return_date_entry.grid(row=1, column=1, padx=5)

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.pack(pady=10)

        ttk.Button(self.root, text="Calculate Fine", command=self.calculate_fine).pack()

    def calculate_fine(self):
        try:
            due_date = datetime.strptime(self.due_date_entry.get(), "%Y-%m-%d")
            return_date = datetime.strptime(self.return_date_entry.get(), "%Y-%m-%d")
            delta = (return_date - due_date).days
            fine = 0
            if delta > 0:
                fine = delta * 10  # Rs.10 per late day
            self.result_label.config(text=f"Fine: Rs. {fine}")
        except ValueError:
            self.result_label.config(text="Invalid date format")

if __name__ == "__main__":
    root = tk.Tk()
    app = FineCalculatorWindow(root)
    root.mainloop()

