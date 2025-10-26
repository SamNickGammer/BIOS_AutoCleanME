"""
Unlock screen implementation with drag & drop and unlock console
"""

import tkinter as tk
from constants.app_config import AppConfig
from functions.unlock_functions import UnlockFunctions
from gui.components.modern_frame import ModernFrame
from gui.components.drag_drop import DragDropWidget
from gui.components.unlock_console import UnlockConsole

class UnlockScreen:
    def __init__(self, parent):
        self.parent = parent
        self.functions = UnlockFunctions()
        self.frame = None
        self.unlock_console = None
    
    def create_screen(self):
        """Create the unlock screen"""
        if self.frame:
            return self.frame  # Return existing frame for fast switching
        
        self.frame = ModernFrame(self.parent)
        
        # Main content area (horizontal layout)
        content_area = ModernFrame(self.frame)
        content_area.pack(fill=tk.BOTH, expand=True)
        
        # Left section - Drag & Drop (wider)
        left_section = ModernFrame(content_area)
        left_section.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        left_section.configure(width=700)  # Increased width for better visibility
        
        # Section title
        left_title = tk.Label(
            left_section,
            text="🔓 Unlock BIOS - Drop BIOS File Here",
            font=(AppConfig.FONT_FAMILY, 12, "bold"),
            bg=AppConfig.PRIMARY_COLOR,
            fg="#333333"
        )
        left_title.pack(pady=(0, 10))
        
        # Drag & Drop widget
        self.drag_drop = DragDropWidget(left_section, self.on_file_selected)
        drag_drop_widget = self.drag_drop.get_widget()
        drag_drop_widget.pack(fill=tk.BOTH, expand=True)
        
        # Right section - Unlock Console (takes remaining space)
        right_section = ModernFrame(content_area)
        right_section.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        # Unlock console
        self.unlock_console = UnlockConsole(right_section)
        console_widget = self.unlock_console.get_widget()
        console_widget.pack(fill=tk.BOTH, expand=True)
        
        return self.frame
    
    def on_file_selected(self, filepath, filename, reset_all=False):
        """Handle file selection from drag & drop"""
        if self.unlock_console:
            self.unlock_console.update_file_info(filepath, filename, reset_all)