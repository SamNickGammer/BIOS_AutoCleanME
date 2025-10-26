"""
Unlock screen implementation with modern light design
"""

import tkinter as tk
from constants.app_config import AppConfig
from functions.unlock_functions import UnlockFunctions
from gui.components.modern_button import ModernButton
from gui.components.modern_frame import ModernFrame

class UnlockScreen:
    def __init__(self, parent):
        self.parent = parent
        self.functions = UnlockFunctions()
        self.frame = None
    
    def create_screen(self):
        """Create the modern unlock screen"""
        if self.frame:
            self.frame.destroy()
        
        self.frame = ModernFrame(self.parent)
        
        # Main content container
        content_container = ModernFrame(self.frame)
        content_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            content_container,
            text="Unlock",
            font=(AppConfig.FONT_FAMILY, 20, "normal"),
            fg=AppConfig.ACCENT_COLOR,
            bg=AppConfig.PRIMARY_COLOR
        )
        title_label.pack(pady=(0, 8))
        
        # Description
        desc_label = tk.Label(
            content_container,
            text="Device unlock and security bypass tools",
            font=(AppConfig.FONT_FAMILY, AppConfig.FONT_SIZE),
            fg="#666666",
            bg=AppConfig.PRIMARY_COLOR
        )
        desc_label.pack(pady=(0, 30))
        
        # Action buttons
        buttons_frame = ModernFrame(content_container)
        buttons_frame.pack(pady=20)
        
        unlock_button = ModernButton(
            buttons_frame,
            text="Start Unlock Process",
            command=self.functions.start_unlock
        )
        unlock_button.pack(pady=8)
        
        return self.frame