"""
Utility screen implementation with drag & drop and utility console
"""

import tkinter as tk
from constants.app_config import AppConfig
from functions.utility_functions import UtilityFunctions
from gui.components.modern_frame import ModernFrame
from gui.components.drag_drop import DragDropWidget
from gui.components.utility_console import UtilityConsole

class UtilityScreen:
    def __init__(self, parent):
        self.parent = parent
        self.functions = UtilityFunctions()
        self.frame = None
        self.utility_console = None
    
    def create_screen(self):
        """Create the utility screen"""
        if self.frame:
            return self.frame  # Return existing frame for fast switching
        
        self.frame = ModernFrame(self.parent)
        
        # Main content area (horizontal layout)
        content_area = ModernFrame(self.frame)
        content_area.pack(fill=tk.BOTH, expand=True)
        
        # Left section - Drag & Drop (wider)
        left_section = ModernFrame(content_area)
        left_section.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        left_section.configure(width=700)  # Same width as unlock screen
        
        # Section title
        left_title = tk.Label(
            left_section,
            text="🔧 Utility Tools - Drop BIOS File Here",
            font=(AppConfig.FONT_FAMILY, 12, "bold"),
            bg=AppConfig.PRIMARY_COLOR,
            fg="#333333"
        )
        left_title.pack(pady=(0, 10))
        
        # Drag & Drop widget
        self.drag_drop = DragDropWidget(left_section, self.on_file_selected)
        drag_drop_widget = self.drag_drop.get_widget()
        drag_drop_widget.pack(fill=tk.BOTH, expand=True)
        
        # Right section - Utility Console (takes remaining space)
        right_section = ModernFrame(content_area)
        right_section.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        # Utility console
        self.utility_console = UtilityConsole(right_section)
        console_widget = self.utility_console.get_widget()
        console_widget.pack(fill=tk.BOTH, expand=True)
        
        return self.frame
    
    def on_file_selected(self, filepath, filename, reset_all=False):
        """Handle file selection from drag & drop"""
        if self.utility_console:
            self.utility_console.update_file_info(filepath, filename, reset_all)
