import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from services.book_return_service import process_book_return
from tkinter_app.fine_calculation import FineCalculatorWindow

class BookReturnUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Return")
        self.root.geometry("400x300")

        frame = tk.Frame(root)
        frame.pack(anchor="n", pady=20)

        tk.Label(frame, text="Member ID:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.member_id_entry = tk.Entry(frame, width=30)
        self.member_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="ISBN:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.book_id_entry = tk.Entry(frame, width=30)
        self.book_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Date Returned (YYYY-MM-DD):").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.date_entry = tk.Entry(frame, width=30)
        self.date_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        self.return_button = tk.Button(frame, text="Return Book", command=self.return_book, width=20)
        self.return_button.grid(row=3, column=0, columnspan=2, pady=15)

    def return_book(self):
        member_id = self.member_id_entry.get().strip()
        isbn = self.book_id_entry.get().strip()
        date_returned = self.date_entry.get().strip()

        if not member_id or not isbn or not date_returned:
            messagebox.showerror("Error", "All fields are required!")
            return

        success, message, due_date = process_book_return(member_id, isbn)
        if success:
            messagebox.showinfo("Success", message)
            fine_window = tk.Toplevel(self.root)
            FineCalculatorWindow(fine_window, member_id, isbn, date_returned, due_date)
        else:
            messagebox.showwarning("Warning", message)
