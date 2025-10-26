"""
Main window GUI implementation using tkinter with modern design
"""

import tkinter as tk
from constants.app_config import AppConfig
from functions.app_functions import AppFunctions
from gui.styles import ModernButton, ModernFrame
from gui.screens.home_screen import HomeScreen
from gui.screens.me_clean_screen import MECleanScreen
from gui.screens.unlock_screen import UnlockScreen
from gui.screens.utility_screen import UtilityScreen
from gui.screens.hp_dmi_screen import HPDMIScreen

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.functions = AppFunctions()
        self.current_screen = None
        self.active_button = None
        self.setup_window()
        self.create_widgets()
        self.show_screen("home")  # Show home screen by default
    
    def setup_window(self):
        """Configure the main window"""
        self.root.title(AppConfig.WINDOW_TITLE)
        self.root.geometry(f"{AppConfig.WINDOW_WIDTH}x{AppConfig.WINDOW_HEIGHT}")
        self.root.configure(bg=AppConfig.PRIMARY_COLOR)
        self.root.resizable(False, False)  # Fixed size for better design control
        
        # Center the window
        self.root.eval('tk::PlaceWindow . center')
    
    def create_widgets(self):
        """Create and place GUI widgets with modern design"""
        # Main container
        main_container = ModernFrame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Navigation section
        nav_section = ModernFrame(main_container, bg=AppConfig.PRIMARY_COLOR)
        nav_section.pack(fill=tk.X, padx=15, pady=(15, 0))
        
        # Navigation buttons container
        nav_buttons_frame = ModernFrame(nav_section, bg=AppConfig.PRIMARY_COLOR)
        nav_buttons_frame.pack(anchor=tk.W)
        
        # Navigation buttons
        self.nav_buttons = {}
        buttons_config = [
            ("home", "Home"),
            ("me_clean", "ME Clean"),
            ("unlock", "Unlock"),
            ("utility", "Utility"),
            ("hp_dmi", "HP DMI")
        ]
        
        for i, (screen_id, text) in enumerate(buttons_config):
            btn = ModernButton(
                nav_buttons_frame,
                text=text,
                command=lambda s=screen_id: self.show_screen(s),
                is_nav=True
            )
            btn.pack(side=tk.LEFT, padx=(0, 8))
            self.nav_buttons[screen_id] = btn
        
        # Separator line (subtle)
        separator = tk.Frame(
            main_container,
            height=1,
            bg=AppConfig.BORDER_COLOR,
            relief=tk.FLAT
        )
        separator.pack(fill=tk.X, padx=15, pady=(12, 0))

        # Content area
        self.content_frame = ModernFrame(main_container)
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Initialize screens
        self.screens = {
            "home": HomeScreen(self.content_frame),
            "me_clean": MECleanScreen(self.content_frame),
            "unlock": UnlockScreen(self.content_frame),
            "utility": UtilityScreen(self.content_frame),
            "hp_dmi": HPDMIScreen(self.content_frame)
        }
    
    def show_screen(self, screen_id):
        """Switch to the specified screen with modern transitions"""
        # Hide current screen
        if self.current_screen:
            self.current_screen.pack_forget()
        
        # Reset ALL buttons to inactive first
        for btn_id, btn in self.nav_buttons.items():
            btn.set_active(False)
        
        # Show new screen
        self.current_screen = self.screens[screen_id].create_screen()
        self.current_screen.pack(fill=tk.BOTH, expand=True)
        
        # Set active button
        self.active_button = self.nav_buttons[screen_id]
        self.active_button.set_active(True)
        
        # Force update the display
        self.root.update_idletasks()
    
    def run(self):
        """Start the GUI application"""
        self.root.mainloop()