"""
Home screen implementation with modern light design
"""

import tkinter as tk
from constants.app_config import AppConfig
from functions.app_functions import AppFunctions
from gui.styles import ModernButton, ModernFrame

class HomeScreen:
    def __init__(self, parent):
        self.parent = parent
        self.functions = AppFunctions()
        self.frame = None
    
    def create_screen(self):
        """Create the modern home screen"""
        if self.frame:
            self.frame.destroy()
        
        self.frame = ModernFrame(self.parent)
        
        # Main content container
        content_container = ModernFrame(self.frame)
        content_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Welcome section
        welcome_label = tk.Label(
            content_container,
            text="Welcome to Home",
            font=(AppConfig.FONT_FAMILY, 20, "normal"),
            fg=AppConfig.TEXT_COLOR,
            bg=AppConfig.PRIMARY_COLOR
        )
        welcome_label.pack(pady=(0, 8))
        
        # Subtitle
        subtitle_label = tk.Label(
            content_container,
            text="Your main dashboard and control center",
            font=(AppConfig.FONT_FAMILY, AppConfig.FONT_SIZE),
            fg="#666666",  # Gray text
            bg=AppConfig.PRIMARY_COLOR
        )
        subtitle_label.pack(pady=(0, 30))
        
        # Action buttons section
        buttons_frame = ModernFrame(content_container)
        buttons_frame.pack(pady=20)
        
        # Sample action button
        hello_button = ModernButton(
            buttons_frame,
            text="Say Hello World",
            command=self.functions.show_hello_world
        )
        hello_button.pack(pady=8)
        
        # Info section
        info_frame = ModernFrame(content_container)
        info_frame.pack(fill=tk.X, pady=(40, 0))
        
        info_text = tk.Label(
            info_frame,
            text="Use the navigation buttons above to access different tools and utilities.",
            font=(AppConfig.FONT_FAMILY, AppConfig.FONT_SIZE),
            fg="#777777",  # Muted text
            bg=AppConfig.PRIMARY_COLOR,
            wraplength=600,
            justify=tk.CENTER
        )
        info_text.pack()
        
        return self.frame