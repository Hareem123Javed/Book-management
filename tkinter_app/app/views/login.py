import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

# Database setup
def connect_db():
    if not os.path.exists("library.db"):
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS admins (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)
        # Insert default admin user
        cursor.execute("INSERT OR IGNORE INTO admins (username, password) VALUES (?, ?)", ("admin", "admin123"))
        conn.commit()
        conn.close()

connect_db()

class LoginPanel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Library Management System - Admin Login")
        self.geometry("350x250")
        self.configure(bg="#f0f0f0")

        tk.Label(self, text="Admin Login", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=20)

        tk.Label(self, text="Username:", bg="#f0f0f0").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Password:", bg="#f0f0f0").pack()
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Login", command=self.check_login).pack(pady=15)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM admins WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()
        conn.close()

        if result:
            messagebox.showinfo("Login Success", f"Welcome {username}!")
            self.destroy()
            # You can call the next UI here
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

if __name__ == "__main__":
    app = LoginPanel()
    app.mainloop()