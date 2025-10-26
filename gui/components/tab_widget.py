"""
Custom tab widget for ME Clean screen - Light theme
"""

import tkinter as tk
from constants.app_config import AppConfig

class TabWidget:
    def __init__(self, parent):
        self.parent = parent
        self.tabs = {}
        self.tab_buttons = {}
        self.current_tab = None
        self.tab_frame = None
        self.content_frame = None
        
        self.create_tab_widget()
    
    def create_tab_widget(self):
        """Create the tab widget structure"""
        # Main container
        self.tab_widget = tk.Frame(self.parent, bg=AppConfig.PRIMARY_COLOR)
        
        # Tab buttons frame
        self.tab_frame = tk.Frame(
            self.tab_widget,
            bg=AppConfig.SECONDARY_COLOR,  # Light gray background
            height=40
        )
        self.tab_frame.pack(fill=tk.X, padx=10, pady=(10, 0))
        self.tab_frame.pack_propagate(False)
        
        # Content frame
        self.content_frame = tk.Frame(
            self.tab_widget,
            bg=AppConfig.PRIMARY_COLOR
        )
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def add_tab(self, tab_id, title, content_widget):
        """Add a new tab"""
        # Create tab button
        tab_button = tk.Button(
            self.tab_frame,
            text=title,
            command=lambda: self.switch_tab(tab_id),
            font=(AppConfig.FONT_FAMILY, AppConfig.BUTTON_FONT_SIZE, "bold"),
            bg="#ffffff",
            fg="#333333",
            relief=tk.FLAT,
            bd=0,
            highlightthickness=0,
            padx=20,
            pady=8,
            cursor='hand2'
        )
        tab_button.pack(side=tk.LEFT, padx=2, pady=5)
        
        # Store tab data
        self.tab_buttons[tab_id] = tab_button
        self.tabs[tab_id] = content_widget
        
        # If this is the first tab, make it active
        if not self.current_tab:
            self.switch_tab(tab_id)
    
    def switch_tab(self, tab_id):
        """Switch to specified tab"""
        # Hide current tab content
        if self.current_tab and self.current_tab in self.tabs:
            self.tabs[self.current_tab].pack_forget()
            # Reset previous button style
            self.tab_buttons[self.current_tab].configure(
                bg="#ffffff",
                fg="#333333"
            )
        
        # Show new tab content
        if tab_id in self.tabs:
            self.tabs[tab_id].pack(fill=tk.BOTH, expand=True)
            # Highlight active button
            self.tab_buttons[tab_id].configure(
                bg="#4CAF50",  # Green for active tab
                fg= AppConfig.BUTTON_ACTIVE_TEXT
            )
            self.current_tab = tab_id
    
    def get_widget(self):
        """Return the main tab widget"""
        return self.tab_widget