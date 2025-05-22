import tkinter as tk
from tkinter import ttk
from datetime import datetime

class FineCalculatorWindow:
    def __init__(self, root, member_id, isbn, return_date, due_date):
        self.root = root
        self.root.title("Fine Calculator")
        self.root.geometry("450x300")

        self.member_id = member_id
        self.isbn = isbn
        self.return_date = return_date
        self.due_date = due_date

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Fine Calculation", font=("Arial", 16)).pack(pady=10)

        frame = ttk.Frame(self.root)
        frame.pack(pady=10)

        ttk.Label(frame, text="Member ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        ttk.Label(frame, text=self.member_id).grid(row=0, column=1, padx=5, sticky="w")

        ttk.Label(frame, text="ISBN:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        ttk.Label(frame, text=self.isbn).grid(row=1, column=1, padx=5, sticky="w")

        ttk.Label(frame, text="Due Date:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.due_date_var = tk.StringVar(value=self.due_date)
        self.due_date_entry = ttk.Entry(frame, textvariable=self.due_date_var, state="readonly")
        self.due_date_entry.grid(row=2, column=1, padx=5)

        ttk.Label(frame, text="Return Date:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.return_date_entry = ttk.Entry(frame)
        self.return_date_entry.insert(0, self.return_date)
        self.return_date_entry.grid(row=3, column=1, padx=5)

        self.result_label = ttk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        button_frame = ttk.Frame(self.root)
        button_frame.pack()

        ttk.Button(button_frame, text="Calculate Fine", command=self.calculate_fine).grid(row=0, column=0, padx=10)
        ttk.Button(button_frame, text="Clear", command=self.clear_fields).grid(row=0, column=1, padx=10)

        ttk.Label(self.root, text="* Fine = Rs. 10 per late day", foreground="gray").pack(pady=5)

    def calculate_fine(self):
        due_date_str = self.due_date_var.get()
        return_date_str = self.return_date_entry.get().strip()

        if not due_date_str or not return_date_str:
            self.result_label.config(text="Please check both date fields.", foreground="red")
            return

        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
            return_date = datetime.strptime(return_date_str, "%Y-%m-%d")

            delta = (return_date - due_date).days
            if delta > 0:
                fine = delta * 10  # Rs.10 per day
                self.result_label.config(
                    text=f"Late by {delta} days. Fine: Rs. {fine}",
                    foreground="darkred"
                )
            else:
                self.result_label.config(
                    text="Book returned on time. No fine!",
                    foreground="green"
                )
        except ValueError:
            self.result_label.config(
                text="Invalid date format. Please use YYYY-MM-DD.",
                foreground="red"
            )

    def clear_fields(self):
        self.return_date_entry.delete(0, tk.END)
        self.result_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    # For standalone testing (optional)
    # app = FineCalculatorWindow(root, "123", "9781234567897", "2025-05-22", "2025-05-15")
    root.mainloop()
