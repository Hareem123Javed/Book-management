import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

def setup_admin_db():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    ''')
    cursor.execute('INSERT OR IGNORE INTO admins (username, password) VALUES (?, ?)', ('admin', 'admin123'))
    conn.commit()
    conn.close()

setup_admin_db()

class LoginPanel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("300x200")

        tk.Label(self, text="Username").pack()
        self.username = tk.Entry(self)
        self.username.pack()

        tk.Label(self, text="Password").pack()
        self.password = tk.Entry(self, show='*')
        self.password.pack()

        tk.Button(self, text="Login", command=self.check_login).pack()

    def check_login(self):
        user = self.username.get()
        pw = self.password.get()

        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM admins WHERE username=? AND password=?", (user, pw))
        result = cursor.fetchone()

        if result:
            self.destroy()
            from app.views.dashboard import Dashboard
            app = Dashboard()
            app.mainloop()
        else:
            messagebox.showerror("Error", "Invalid login")

if __name__ == '__main__':
    app = LoginPanel()
    app.mainloop()