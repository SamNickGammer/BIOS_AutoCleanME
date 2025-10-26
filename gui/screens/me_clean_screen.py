"""
ME Clean screen implementation with instant tab switching like main navigation
"""

import tkinter as tk
from constants.app_config import AppConfig
from functions.me_clean_functions import MECleanFunctions
from gui.components.modern_frame import ModernFrame
from gui.components.drag_drop import DragDropWidget
from gui.components.status_panel import StatusPanel

class MECleanScreen:
    def __init__(self, parent):
        self.parent = parent
        self.functions = MECleanFunctions()
        self.frame = None
        self.current_tab = None
        self.active_tab_button = None
        self.tab_buttons = {}
        self.tab_screens = {}
        self.content_frame = None
        self.status_panel = None
    
    def create_screen(self):
        """Create the ME Clean screen with instant tab switching"""
        if self.frame:
            return self.frame  # Return existing frame for fast switching
        
        self.frame = ModernFrame(self.parent)
        
        # Tab navigation bar (like main navigation)
        self.create_tab_navigation()
        
        # Content area for tab screens
        self.content_frame = ModernFrame(self.frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Initialize all tab screens immediately
        self.initialize_tab_screens()
        
        # Show default tab (Auto)
        self.show_tab("auto")
        
        return self.frame
    
    def create_tab_navigation(self):
        """Create the tab navigation bar"""
        # Tab navigation frame
        nav_frame = tk.Frame(
            self.frame,
            bg=AppConfig.SECONDARY_COLOR,
            height=40
        )
        nav_frame.pack(fill=tk.X, padx=10, pady=(10, 0))
        nav_frame.pack_propagate(False)
        
        # Tab buttons
        tab_configs = [
            ("auto", "Auto"),
            ("fitc", "FITC"),
            ("manual", "Manual")
        ]
        
        for tab_id, title in tab_configs:
            btn = tk.Button(
                nav_frame,
                text=title,
                command=lambda t=tab_id: self.show_tab(t),
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
            btn.pack(side=tk.LEFT, padx=2, pady=5)
            self.tab_buttons[tab_id] = btn
    
    def initialize_tab_screens(self):
        """Initialize all tab screens immediately for instant switching"""
        # Auto tab screen
        self.tab_screens["auto"] = self.create_auto_screen()
        
        # FITC tab screen
        self.tab_screens["fitc"] = self.create_fitc_screen()
        
        # Manual tab screen
        self.tab_screens["manual"] = self.create_manual_screen()
    
    def create_auto_screen(self):
        """Create the AUTO tab screen"""
        auto_frame = ModernFrame(self.content_frame)
        
        # Main content area (horizontal layout)
        content_area = ModernFrame(auto_frame)
        content_area.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Left section - Drag & Drop
        left_section = ModernFrame(content_area)
        left_section.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Section title
        left_title = tk.Label(
            left_section,
            text="ME Clean Auto - Drop BIOS File Here",
            font=(AppConfig.FONT_FAMILY, 12, "bold"),
            bg=AppConfig.PRIMARY_COLOR,
            fg="#4A90E2"
        )
        left_title.pack(pady=(0, 10))
        
        # Drag & Drop widget
        self.drag_drop = DragDropWidget(left_section, self.on_file_selected)
        drag_drop_widget = self.drag_drop.get_widget()
        drag_drop_widget.pack(fill=tk.BOTH, expand=True)
        
        # Right section - Status Panel
        right_section = ModernFrame(content_area)
        right_section.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        # Status panel
        self.status_panel = StatusPanel(right_section)
        status_widget = self.status_panel.get_widget()
        status_widget.pack(fill=tk.BOTH, expand=True)
        
        return auto_frame
    
    def create_fitc_screen(self):
        """Create the FITC tab screen"""
        fitc_frame = ModernFrame(self.content_frame)
        
        # FITC content
        fitc_label = tk.Label(
            fitc_frame,
            text="🔧 FITC Tab",
            font=(AppConfig.FONT_FAMILY, 16, "bold"),
            bg=AppConfig.PRIMARY_COLOR,
            fg="#FF9800"
        )
        fitc_label.pack(pady=50)
        
        fitc_desc = tk.Label(
            fitc_frame,
            text="FITC (Flash Image Tool Configuration) functionality will be implemented here.",
            font=(AppConfig.FONT_FAMILY, AppConfig.FONT_SIZE),
            bg=AppConfig.PRIMARY_COLOR,
            fg="#666666",
            wraplength=400
        )
        fitc_desc.pack(pady=20)
        
        return fitc_frame
    
    def create_manual_screen(self):
        """Create the Manual tab screen"""
        manual_frame = ModernFrame(self.content_frame)
        
        # Manual content
        manual_label = tk.Label(
            manual_frame,
            text="⚙️ Manual Tab",
            font=(AppConfig.FONT_FAMILY, 16, "bold"),
            bg=AppConfig.PRIMARY_COLOR,
            fg="#9C27B0"
        )
        manual_label.pack(pady=50)
        
        manual_desc = tk.Label(
            manual_frame,
            text="Manual ME cleaning operations and advanced settings will be available here.",
            font=(AppConfig.FONT_FAMILY, AppConfig.FONT_SIZE),
            bg=AppConfig.PRIMARY_COLOR,
            fg="#666666",
            wraplength=400
        )
        manual_desc.pack(pady=20)
        
        return manual_frame
    
    def show_tab(self, tab_id):
        """Switch to specified tab with loading animation"""
        # Show loading screen
        self.show_loading()
        
        # Schedule the actual tab switch after a brief delay
        self.frame.after(200, lambda: self.switch_tab_content(tab_id))
    
    def show_loading(self):
        """Show a small loading screen"""
        # Hide current tab
        if self.current_tab and self.current_tab in self.tab_screens:
            self.tab_screens[self.current_tab].pack_forget()
        
        # Create loading frame
        self.loading_frame = tk.Frame(
            self.content_frame,
            bg=AppConfig.PRIMARY_COLOR
        )
        self.loading_frame.pack(fill=tk.BOTH, expand=True)
        
        # Loading spinner (using text animation)
        self.loading_label = tk.Label(
            self.loading_frame,
            text="⏳ Loading...",
            font=(AppConfig.FONT_FAMILY, 14),
            bg=AppConfig.PRIMARY_COLOR,
            fg="#666666"
        )
        self.loading_label.pack(expand=True)
        
        # Animate loading text
        self.animate_loading()
    
    def animate_loading(self):
        """Animate the loading text"""
        current_text = self.loading_label.cget("text")
        if "..." in current_text:
            dots = current_text.count(".")
            if dots >= 3:
                new_text = "⏳ Loading"
            else:
                new_text = current_text + "."
        else:
            new_text = "⏳ Loading."
        
        self.loading_label.configure(text=new_text)
    
    def switch_tab_content(self, tab_id):
        """Actually switch the tab content"""
        # Hide loading screen
        if hasattr(self, 'loading_frame'):
            self.loading_frame.destroy()
        
        # Reset previous button style
        if self.current_tab and self.current_tab in self.tab_buttons:
            self.tab_buttons[self.current_tab].configure(
                bg="#ffffff",
                fg="#333333"
            )
        
        # Show new tab
        if tab_id in self.tab_screens:
            self.tab_screens[tab_id].pack(fill=tk.BOTH, expand=True)
            # Highlight active button with AppConfig color
            self.tab_buttons[tab_id].configure(
                bg=AppConfig.BUTTON_ACTIVE_COLOR,  # Dark background
                fg=AppConfig.BUTTON_ACTIVE_TEXT    # Blue text
            )
            self.current_tab = tab_id
    
    def on_file_selected(self, filepath, filename):
        """Handle file selection from drag & drop"""
        if self.status_panel:
            self.status_panel.update_file_info(filepath, filename)