import sys
import os

# Add the project root to Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from app.views.login_admin_panel import LoginPanel

if __name__ == "__main__":
    app = LoginPanel()
    app.mainloop()
