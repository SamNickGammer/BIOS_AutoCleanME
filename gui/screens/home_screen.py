"""
Home screen implementation with full-screen slideshow and proper footer
"""

import tkinter as tk
from constants.app_config import AppConfig
from functions.app_functions import AppFunctions
from gui.components.modern_frame import ModernFrame
from gui.components.slideshow import Slideshow

class HomeScreen:
    def __init__(self, parent):
        self.parent = parent
        self.functions = AppFunctions()
        self.frame = None
        self.slideshow = None
        self.counter_label = None
    
    def create_screen(self):
        """Create the home screen with full-screen slideshow"""
        if self.frame:
            # Stop previous slideshow if exists
            if self.slideshow:
                self.slideshow.stop_auto_slideshow()
            self.frame.destroy()
        
        self.frame = ModernFrame(self.parent)
        
        # Main slideshow area (takes most space)
        slideshow_main = ModernFrame(self.frame)
        slideshow_main.pack(fill=tk.BOTH, expand=True)
        
        # Create slideshow container with navigation overlay
        slideshow_container = tk.Frame(slideshow_main, bg=AppConfig.PRIMARY_COLOR)
        slideshow_container.pack(fill=tk.BOTH, expand=True)
        
        # Create slideshow
        self.slideshow = Slideshow(slideshow_container)
        slideshow_frame = self.slideshow.get_frame()
        slideshow_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left navigation button (absolute positioning)
        left_btn = tk.Button(
            slideshow_container,
            text="◀",
            command=self.previous_slide,
            font=(AppConfig.FONT_FAMILY, 18, "bold"),
            bg=AppConfig.BUTTON_ACTIVE_COLOR,
            fg=AppConfig.BUTTON_ACTIVE_TEXT,
            relief=tk.FLAT,
            bd=0,
            highlightthickness=0,
            width=3,
            height=2,
            cursor='hand2'
        )
        left_btn.place(x=20, rely=0.5, anchor=tk.W)
        
        # Right navigation button (absolute positioning)
        right_btn = tk.Button(
            slideshow_container,
            text="▶",
            command=self.next_slide,
            font=(AppConfig.FONT_FAMILY, 18, "bold"),
            bg=AppConfig.BUTTON_ACTIVE_COLOR,
            fg=AppConfig.BUTTON_ACTIVE_TEXT,
            relief=tk.FLAT,
            bd=0,
            highlightthickness=0,
            width=3,
            height=2,
            cursor='hand2'
        )
        right_btn.place(x=-20, rely=0.5, anchor=tk.E, relx=1.0)
        
        # Black footer positioned higher from bottom
        footer_frame = tk.Frame(
            self.frame,
            bg="#000000",  # Black background
            height=35
        )
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        footer_frame.pack_propagate(False)
        
        # Footer content
        footer_content = tk.Frame(footer_frame, bg="#000000")
        footer_content.pack(fill=tk.BOTH, expand=True)
        
        # Counter on left
        self.counter_label = tk.Label(
            footer_content,
            text="",
            font=(AppConfig.FONT_FAMILY, AppConfig.FONT_SIZE),
            fg="#ffffff",
            bg="#000000"
        )
        self.counter_label.pack(side=tk.LEFT, padx=15, pady=8)
        
        # Credits in center
        credits_text = tk.Label(
            footer_content,
            text="💜 Made with love by Samnickgammer 🚀",
            font=(AppConfig.FONT_FAMILY, AppConfig.FONT_SIZE),
            fg="#ffffff",
            bg="#000000"
        )
        credits_text.pack(expand=True, pady=8)
        
        # Spacer to push footer up from bottom edge
        spacer_frame = tk.Frame(
            self.frame,
            bg=AppConfig.PRIMARY_COLOR,
            height=25
        )
        spacer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        spacer_frame.pack_propagate(False)
        
        # Update counter initially and set up periodic updates
        self.update_counter()
        self.schedule_counter_update()
        
        return self.frame
    
    def previous_slide(self):
        """Navigate to previous slide"""
        if self.slideshow:
            self.slideshow.previous_image()
            self.update_counter()
    
    def next_slide(self):
        """Navigate to next slide"""
        if self.slideshow:
            self.slideshow.next_image()
            self.update_counter()
    
    def update_counter(self):
        """Update the slide counter"""
        if self.slideshow and self.counter_label:
            counter_text = self.slideshow.get_current_info()
            self.counter_label.configure(text=counter_text)
    
    def schedule_counter_update(self):
        """Schedule periodic counter updates for auto-slideshow"""
        if self.frame and self.frame.winfo_exists():
            self.update_counter()
            # Schedule next update
            self.frame.after(100, self.schedule_counter_update)