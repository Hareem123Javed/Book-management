# app/views/inventory_reports.py

import tkinter as tk
from tkinter import ttk
import mysql.connector

class InventoryReportsWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Reports")
        self.root.geometry("600x400")
        self.create_widgets()
        self.load_data_from_db()

    def create_widgets(self):
        ttk.Label(self.root, text="Inventory Reports", font=("Arial", 16)).pack(pady=10)

        # Add 'ISBN' and remove 'Available'
        self.tree = ttk.Treeview(self.root, columns=("ISBN", "Year", "Title", "Author"), show="headings")
        # self.tree.heading("ID", text="Book ID")
        self.tree.heading("ISBN", text="ISBN")
        self.tree.heading("Year", text="Year")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Author", text="Author")
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def load_data_from_db(self):
        try:
            # Update these parameters to match your MySQL setup
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="library",
                port=3307
            )
            cursor = connection.cursor()
            cursor.execute("SELECT  ISBN, Year,Title, Author FROM books")
            rows = cursor.fetchall()
            print(f"Number of rows fetched: {len(rows)}")  # Debug print

            for row in rows:
                print(row)  # Print each row fetched
                self.tree.insert("", tk.END, values=row)

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Database error: {err}")

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryReportsWindow(root)
    root.mainloop()
