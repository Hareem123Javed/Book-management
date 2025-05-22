import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class BookLendingUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Lending")
        self.root.geometry("400x300")

        # Container frame to hold form
        frame = tk.Frame(root)
        frame.pack(anchor="n", pady=20)

        # Member ID
        tk.Label(frame, text="Member ID:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.member_id_entry = tk.Entry(frame, width=30)
        self.member_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Book ID
        tk.Label(frame, text="Book ID:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.book_id_entry = tk.Entry(frame, width=30)
        self.book_id_entry.grid(row=1, column=1, padx=5, pady=5)

        # Date Borrowed
        tk.Label(frame, text="Date Borrowed (YYYY-MM-DD):").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.date_entry = tk.Entry(frame, width=30)
        self.date_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        # Button
        self.lend_button = tk.Button(frame, text="Lend Book", command=self.lend_book, width=20)
        self.lend_button.grid(row=3, column=0, columnspan=2, pady=15)

    def lend_book(self):
        member_id = self.member_id_entry.get().strip()
        book_id = self.book_id_entry.get().strip()
        date_borrowed = self.date_entry.get().strip()

        if not member_id or not book_id or not date_borrowed:
            messagebox.showerror("Error", "All fields are required!")
            return

        messagebox.showinfo("Success", f"Book ID {book_id} lent to Member ID {member_id} on {date_borrowed}.")


if __name__ == "__main__":
    root = tk.Tk()
    app = BookLendingUI(root)
    root.mainloop()

