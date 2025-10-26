"""
Application functions and business logic
"""

import tkinter as tk
from tkinter import messagebox

class AppFunctions:
    def __init__(self):
        pass
    
    def show_hello_world(self):
        """Display a hello world message"""
        messagebox.showinfo("Hello", "Hello World!")
    
    def show_custom_message(self, title, message):
        """Display a custom message dialog"""
        messagebox.showinfo(title, message)
    
    def show_error(self, message):
        """Display an error message"""
        messagebox.showerror("Error", message)
    
    def show_warning(self, message):
        """Display a warning message"""
        messagebox.showwarning("Warning", message)
    
    def ask_yes_no(self, title, question):
        """Ask a yes/no question and return the result"""
        return messagebox.askyesno(title, question)