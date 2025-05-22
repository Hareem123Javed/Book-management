import tkinter as tk
from tkinter import messagebox
from app.services import book_services

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard - Book Management")
        self.geometry("700x500")
        self.resizable(False, False)

        book_services.create_table()

        self.selected_index = None  # For tracking selected book index

        # Input Frame
        input_frame = tk.LabelFrame(self, text="Book Information", padx=10, pady=10)
        input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(input_frame, text="Title:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.title_entry = tk.Entry(input_frame, width=50)
        self.title_entry.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Author:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.author_entry = tk.Entry(input_frame, width=50)
        self.author_entry.grid(row=1, column=1, padx=5)

        tk.Label(input_frame, text="ISBN:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.isbn_entry = tk.Entry(input_frame, width=50)
        self.isbn_entry.grid(row=2, column=1, padx=5)

        tk.Label(input_frame, text="Year:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.year_entry = tk.Entry(input_frame, width=50)
        self.year_entry.grid(row=3, column=1, padx=5)

        # Button Frame
        btn_frame = tk.Frame(self)
        btn_frame.grid(row=1, column=0, pady=10)

        tk.Button(btn_frame, text="Add Book", width=15, command=self.add_book).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Delete Selected", width=15, command=self.delete_book).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Update Selected", width=15, command=self.update_book).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Display Books", width=15, command=self.load_books).grid(row=0, column=3, padx=5)

        # Listbox Frame
        list_frame = tk.LabelFrame(self, text="Books List", padx=10, pady=10)
        list_frame.grid(row=2, column=0, padx=10, pady=10)

        self.book_list = tk.Listbox(list_frame, width=90, height=15)
        self.book_list.pack(side=tk.LEFT, fill=tk.BOTH)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.book_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.book_list.yview)

        self.book_list.bind("<<ListboxSelect>>", self.load_selected_book)

        self.load_books()

    def load_books(self):
        self.book_list.delete(0, tk.END)
        for book in book_services.get_books():
            self.book_list.insert(tk.END, f"{book[0]} | {book[1]} | ISBN: {book[2]} | Year: {book[3]}")

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        isbn = self.isbn_entry.get()
        year = self.year_entry.get()

        if title and author and isbn and year:
            try:
                book_services.add_book(title, author, isbn, int(year))
                self.clear_inputs()
                self.load_books()
            except ValueError:
                messagebox.showerror("Error", "Year must be a number.")
        else:
            messagebox.showwarning("Warning", "All fields are required.")

    def delete_book(self):
        selected = self.book_list.curselection()
        if not selected:
            messagebox.showerror("Error", "Select a book to delete.")
            return

        book_str = self.book_list.get(selected[0])
        title, author, isbn, year = self.parse_book_str(book_str)

        book_services.delete_book(title, author, isbn, int(year))
        self.clear_inputs()
        self.load_books()

    def update_book(self):
        if self.selected_index is None:
            messagebox.showerror("Error", "Select a book to update.")
            return

        try:
            title = self.title_entry.get()
            author = self.author_entry.get()
            isbn = self.isbn_entry.get()
            year = int(self.year_entry.get())

            original_str = self.book_list.get(self.selected_index)
            old_title, old_author, old_isbn, old_year = self.parse_book_str(original_str)

            book_services.update_book(
                old_title, old_author, old_isbn, old_year,
                title, author, isbn, year
            )
            self.clear_inputs()
            self.load_books()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update: {e}")

    def load_selected_book(self, event):
        selected = self.book_list.curselection()
        if not selected:
            return
        self.selected_index = selected[0]
        book_str = self.book_list.get(self.selected_index)
        title, author, isbn, year = self.parse_book_str(book_str)

        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(0, title)
        self.author_entry.delete(0, tk.END)
        self.author_entry.insert(0, author)
        self.isbn_entry.delete(0, tk.END)
        self.isbn_entry.insert(0, isbn)
        self.year_entry.delete(0, tk.END)
        self.year_entry.insert(0, year)

    def parse_book_str(self, book_str):
        parts = book_str.split(" | ")
        title = parts[0].strip()
        author = parts[1].strip()
        isbn = parts[2].replace("ISBN:", "").strip()
        year = parts[3].replace("Year:", "").strip()
        return title, author, isbn, year

    def clear_inputs(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.isbn_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.selected_index = None

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()
