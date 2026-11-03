# main.py
import tkinter as tk
from database import init_db
from GUI.styles import apply_theme
from GUI.login import LoginWindow


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Smart Campus Resource Booking System")
        self.geometry("1000x650")

        # Apply the theme we just created
        apply_theme(self)

        self.current_user = None

        # Initialize the database (just in case it wasn't created yet)
        init_db()

        # Start on the login screen
        self.show_login()

    def clear(self):
        """Destroys all widgets currently on the screen to clear it."""
        for w in self.winfo_children():
            w.destroy()

    def show_login(self):
        """Clears the screen and loads the Login Window."""
        self.clear()
        self.current_user = None
        LoginWindow(self, self)


if __name__ == "__main__":
    app = App()
    app.mainloop()