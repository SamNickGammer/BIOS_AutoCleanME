
import tkinter as tk
from constants.app_config import AppConfig

class ModernFrame(tk.Frame):
    """Modern styled frame"""
    
    def __init__(self, parent, **kwargs):
        default_style = {
            'bg': AppConfig.PRIMARY_COLOR,
            'relief': tk.FLAT,
            'bd': 0
        }
        default_style.update(kwargs)
        super().__init__(parent, **default_style)