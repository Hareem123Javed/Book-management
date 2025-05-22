import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.services.lending_service import lend_book

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class BookLendingUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Lending")
        self.root.geometry("400x350")

        frame = tk.Frame(root)
        frame.pack(anchor="n", pady=20)

        tk.Label(frame, text="Member ID:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.member_id_entry = tk.Entry(frame, width=30)
        self.member_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Book ISBN:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.book_id_entry = tk.Entry(frame, width=30)
        self.book_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Date Borrowed (YYYY-MM-DD):").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.date_entry = tk.Entry(frame, width=30)
        self.date_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="Due Date (YYYY-MM-DD):").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.due_date_entry = tk.Entry(frame, width=30)
        self.due_date_entry.grid(row=3, column=1, padx=5, pady=5)

        self.lend_button = tk.Button(frame, text="Lend Book", command=self.handle_lend, width=20)
        self.lend_button.grid(row=4, column=0, columnspan=2, pady=15)

    def handle_lend(self):
        member_id = self.member_id_entry.get().strip()
        isbn = self.book_id_entry.get().strip()
        date_borrowed = self.date_entry.get().strip()
        due_date = self.due_date_entry.get().strip()

        if not member_id or not isbn or not date_borrowed or not due_date:
            messagebox.showerror("Error", "All fields are required!")
            return

        success, message = lend_book(member_id, isbn, date_borrowed, due_date)
        if success:
            messagebox.showinfo("Success", message)
            self.clear_fields()
        else:
            messagebox.showerror("Database Error", message)

    def clear_fields(self):
        self.member_id_entry.delete(0, tk.END)
        self.book_id_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))
        self.due_date_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = BookLendingUI(root)
    root.mainloop()
