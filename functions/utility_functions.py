"""
Utility specific functions
"""

import tkinter as tk
from tkinter import messagebox
import platform
import os

class UtilityFunctions:
    def __init__(self):
        pass
    
    def show_system_info(self):
        """Display system information"""
        system_info = f"""
System: {platform.system()}
Release: {platform.release()}
Version: {platform.version()}
Machine: {platform.machine()}
Processor: {platform.processor()}
        """
        messagebox.showinfo("System Information", system_info.strip())
    
    def check_disk_space(self):
        """Check available disk space"""
        messagebox.showinfo("Disk Space", "Checking available disk space...")
    
    def run_diagnostics(self):
        """Run system diagnostics"""
        messagebox.showinfo("Diagnostics", "Running system diagnostics...")