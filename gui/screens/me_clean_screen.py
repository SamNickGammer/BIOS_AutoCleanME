"""
ME Clean screen implementation with instant tab switching using top navigation style
"""

import tkinter as tk
from constants.app_config import AppConfig
from functions.me_clean_functions import MECleanFunctions
from gui.components.modern_frame import ModernFrame
from gui.components.modern_button import ModernButton
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
        
        # Tab navigation bar (using same style as top navigation)
        self.create_tab_navigation()
        
        # Separator line (like main navigation)
        separator = tk.Frame(
            self.frame,
            height=1,
            bg=AppConfig.BORDER_COLOR,
            relief=tk.FLAT
        )
        separator.pack(fill=tk.X, padx=15, pady=(12, 0))
        
        # Content area for tab screens
        self.content_frame = ModernFrame(self.frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Initialize all tab screens immediately
        self.initialize_tab_screens()
        
        # Show default tab (Auto)
        self.show_tab("auto")
        
        return self.frame
    
    def create_tab_navigation(self):
        """Create the tab navigation bar using same style as top navigation"""
        # Navigation section
        nav_section = ModernFrame(self.frame, bg=AppConfig.PRIMARY_COLOR)
        nav_section.pack(fill=tk.X, padx=15, pady=(15, 0))
        
        # Navigation buttons container
        nav_buttons_frame = ModernFrame(nav_section, bg=AppConfig.PRIMARY_COLOR)
        nav_buttons_frame.pack(anchor=tk.W)
        
        # Tab buttons (using same style as top navigation)
        tab_configs = [
            ("auto", "Auto"),
            ("fitc", "FITC"),
            ("manual", "Manual")
        ]
        
        for tab_id, title in tab_configs:
            btn = ModernButton(
                nav_buttons_frame,
                text=title,
                command=lambda t=tab_id: self.show_tab(t),
                is_nav=True
            )
            btn.pack(side=tk.LEFT, padx=(0, 8))
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
        
        # Title
        # title_label = tk.Label(
        #     auto_frame,
        #     text="🔧 ME Clean Auto",
        #     font=(AppConfig.FONT_FAMILY, 16, "bold"),
        #     bg=AppConfig.PRIMARY_COLOR,
        #     fg="#4A90E2"
        # )
        # title_label.pack(pady=(0, 20))
        
        # Main content area (horizontal layout)
        content_area = ModernFrame(auto_frame)
        content_area.pack(fill=tk.BOTH, expand=True)
        
        # Left section - Drag & Drop
        left_section = ModernFrame(content_area)
        left_section.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Section title
        left_title = tk.Label(
            left_section,
            text="🔧 ME Clean Auto - Drop BIOS File Here",
            font=(AppConfig.FONT_FAMILY, 12, "bold"),
            bg=AppConfig.PRIMARY_COLOR,
            fg="#333333"
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
        
        # Title
        title_label = tk.Label(
            fitc_frame,
            text="🔧 FITC Configuration",
            font=(AppConfig.FONT_FAMILY, 16, "bold"),
            bg=AppConfig.PRIMARY_COLOR,
            fg="#FF9800"
        )
        title_label.pack(pady=(20, 10))
        
        # Description
        desc_label = tk.Label(
            fitc_frame,
            text="Flash Image Tool Configuration",
            font=(AppConfig.FONT_FAMILY, 12),
            bg=AppConfig.PRIMARY_COLOR,
            fg="#666666"
        )
        desc_label.pack(pady=(0, 30))
        
        # Content area
        content_area = ModernFrame(fitc_frame)
        content_area.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Placeholder content
        placeholder_label = tk.Label(
            content_area,
            text="FITC functionality will be implemented here.\n\nThis section will include:\n• Flash configuration tools\n• Image manipulation options\n• Advanced BIOS settings",
            font=(AppConfig.FONT_FAMILY, AppConfig.FONT_SIZE),
            bg=AppConfig.PRIMARY_COLOR,
            fg="#666666",
            justify=tk.LEFT
        )
        placeholder_label.pack(pady=50)
        
        return fitc_frame
    
    def create_manual_screen(self):
        """Create the Manual tab screen"""
        manual_frame = ModernFrame(self.content_frame)
        
        # Title
        title_label = tk.Label(
            manual_frame,
            text="⚙️ Manual Operations",
            font=(AppConfig.FONT_FAMILY, 16, "bold"),
            bg=AppConfig.PRIMARY_COLOR,
            fg="#9C27B0"
        )
        title_label.pack(pady=(20, 10))
        
        # Description
        desc_label = tk.Label(
            manual_frame,
            text="Advanced Manual ME Cleaning",
            font=(AppConfig.FONT_FAMILY, 12),
            bg=AppConfig.PRIMARY_COLOR,
            fg="#666666"
        )
        desc_label.pack(pady=(0, 30))
        
        # Content area
        content_area = ModernFrame(manual_frame)
        content_area.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Placeholder content
        placeholder_label = tk.Label(
            content_area,
            text="Manual ME cleaning operations will be available here.\n\nThis section will include:\n• Custom cleaning parameters\n• Advanced ME region tools\n• Expert configuration options",
            font=(AppConfig.FONT_FAMILY, AppConfig.FONT_SIZE),
            bg=AppConfig.PRIMARY_COLOR,
            fg="#666666",
            justify=tk.LEFT
        )
        placeholder_label.pack(pady=50)
        
        return manual_frame
    
    def show_tab(self, tab_id):
        """Switch to specified tab instantly (like main navigation)"""
        # Hide current tab
        if self.current_tab and self.current_tab in self.tab_screens:
            self.tab_screens[self.current_tab].pack_forget()
        
        # Reset ALL buttons to inactive first
        for btn_id, btn in self.tab_buttons.items():
            btn.set_active(False)
        
        # Show new tab
        if tab_id in self.tab_screens:
            self.tab_screens[tab_id].pack(fill=tk.BOTH, expand=True)
            
            # Set active button
            self.active_tab_button = self.tab_buttons[tab_id]
            self.active_tab_button.set_active(True)
            self.current_tab = tab_id
        
        # Force update the display
        self.frame.update_idletasks()
    
    def on_file_selected(self, filepath, filename, reset_all=False):
        """Handle file selection from drag & drop"""
        if self.status_panel:
            self.status_panel.update_file_info(filepath, filename, reset_all)