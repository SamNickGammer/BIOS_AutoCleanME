#!/usr/bin/env python3
"""
Main entry point for the Python GUI application
"""

from gui.main_window import MainWindow
from constants.app_config import AppConfig

def main():
    """Initialize and run the application"""
    app = MainWindow()
    app.run()

if __name__ == "__main__":
    main()