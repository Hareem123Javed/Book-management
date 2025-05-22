import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class BookReturnUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Return")
        self.root.geometry("400x300")

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

        # Date Returned
        tk.Label(frame, text="Date Returned (YYYY-MM-DD):").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.date_entry = tk.Entry(frame, width=30)
        self.date_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        # Button
        self.return_button = tk.Button(frame, text="Return Book", command=self.return_book, width=20)
        self.return_button.grid(row=3, column=0, columnspan=2, pady=15)

    def return_book(self):
        member_id = self.member_id_entry.get().strip()
        book_id = self.book_id_entry.get().strip()
        date_returned = self.date_entry.get().strip()

        if not member_id or not book_id or not date_returned:
            messagebox.showerror("Error", "All fields are required!")
            return

        messagebox.showinfo("Success", f"Book ID {book_id} returned by Member ID {member_id} on {date_returned}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BookReturnUI(root)
    root.mainloop()
