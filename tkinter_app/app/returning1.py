import tkinter as tk
from views.book_return_ui import BookReturnUI

if __name__ == "__main__":
    root = tk.Tk()
    app = BookReturnUI(root)
    root.mainloop()
