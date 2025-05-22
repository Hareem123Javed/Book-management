
# app/views/inventory_reports.py

import tkinter as tk
from tkinter import ttk

class InventoryReportsWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Reports")
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Inventory Reports", font=("Arial", 16)).pack(pady=10)

        self.tree = ttk.Treeview(self.root, columns=("ID", "Title", "Author", "Available"), show="headings")
        self.tree.heading("ID", text="Book ID")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Author", text="Author")
        self.tree.heading("Available", text="Available")
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Dummy data for now
        books = [
            (1, "Python Basics", "John Smith", 3),
            (2, "Advanced Python", "Alice Brown", 0),
            (3, "Data Science", "Mike Green", 5)
        ]

        for book in books:
            self.tree.insert("", tk.END, values=book)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryReportsWindow(root)
    root.mainloop()
