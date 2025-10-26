"""
ME Clean screen implementation with modern light design
"""

import tkinter as tk
from constants.app_config import AppConfig
from functions.me_clean_functions import MECleanFunctions
from gui.styles import ModernButton, ModernFrame

class MECleanScreen:
    def __init__(self, parent):
        self.parent = parent
        self.functions = MECleanFunctions()
        self.frame = None
    
    def create_screen(self):
        """Create the modern ME Clean screen"""
        if self.frame:
            self.frame.destroy()
        
        self.frame = ModernFrame(self.parent)
        
        # Main content container
        content_container = ModernFrame(self.frame)
        content_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            content_container,
            text="ME Clean",
            font=(AppConfig.FONT_FAMILY, 20, "normal"),
            fg=AppConfig.ACCENT_COLOR,
            bg=AppConfig.PRIMARY_COLOR
        )
        title_label.pack(pady=(0, 8))
        
        # Description
        desc_label = tk.Label(
            content_container,
            text="Management Engine cleaning tools and utilities",
            font=(AppConfig.FONT_FAMILY, AppConfig.FONT_SIZE),
            fg="#666666",
            bg=AppConfig.PRIMARY_COLOR
        )
        desc_label.pack(pady=(0, 30))
        
        # Action buttons
        buttons_frame = ModernFrame(content_container)
        buttons_frame.pack(pady=20)
        
        clean_button = ModernButton(
            buttons_frame,
            text="Start ME Clean Process",
            command=self.functions.start_me_clean
        )
        clean_button.pack(pady=8)
        
        return self.frame