"""

    User Interface
    @gl36

    20/06/2025

"""

# Imports
# from tkinter import messagebox, filedialog

import ttkbootstrap as ttk
import ttkbootstrap.dialogs as dialogs
from ttkbootstrap.constants import *

# Class
class Header:
    def __init__(self, master: ttk.Window, title: str, description: str = None):

        self.frame = ttk.Frame(master)
        self.label_title = ttk.Label(self.frame, text=title, font={"family": "Helvetica", "weight": "bold", "size": 15}, anchor="w")
        self.label_title.pack(side="left", expand=True, fill=True)

        if description:
            self.label_description = ttk.Label(self.frame, text=description, anchor="w")
            self.label_description.pack(side="left", fill=True)

class App:
    def __init__(self, window_title: str):
        # Properties
        self.menus: dict[str, ttk.Menu] = {}

        # Initialise Tk
        self.root = ttk.Window(title=window_title, themename="darkly")
        self.root.resizable(False, False)

        # Create UI - Change as necessary

        ## Menubar
        self.menubar = ttk.Menu(self.root)

        ## Variables
        self.var_destination = ttk.StringVar()

        ## Header
        self.app_header = Header(self.root, )
    
    def create_menu(self, name: str):
        menu = ttk.Menu(self.menubar)

        self.menus[name] = menu
        self.menubar.add_cascade(label=name, menu=menu)
    
    def create_menubutton(self, menu_name: str, button_name: str, command):
        self.menus[menu_name].add_command(label=button_name, command=command)

# Source - https://stackoverflow.com/a/58527868
# Posted by tgikal
# Retrieved 2026-11-23, License - CC BY-SA 4.0

import ctypes

def raise_console(console_toggle):
    """Brings up the Console Window."""
    if console_toggle:
        # Show console
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 4)
    else:
        # Hide console
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)


if __name__ == "__main__":
    App("Test app").root.mainloop()