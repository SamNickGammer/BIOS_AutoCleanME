"""
Modern UI styles and components
"""

import tkinter as tk
from constants.app_config import AppConfig

class ModernButton(tk.Button):
    """Modern styled button with hover effects"""
    
    def __init__(self, parent, text="", command=None, is_nav=False, **kwargs):
        # Default modern button style
        default_style = {
            'font': (AppConfig.FONT_FAMILY, AppConfig.BUTTON_FONT_SIZE, 'normal'),
            'bg': AppConfig.BUTTON_COLOR,
            'fg': AppConfig.TEXT_COLOR,
            'relief': tk.FLAT,
            'bd': 1,
            'highlightthickness': 0,
            'cursor': 'hand2',
            'borderwidth': 1,
            'highlightbackground': AppConfig.BORDER_COLOR
        }
        
        # Navigation button specific styling
        if is_nav:
            default_style.update({
                'padx': 12,
                'pady': 6,
                'width': 10
            })
        else:
            default_style.update({
                'padx': 15,
                'pady': 8
            })
        
        # Merge with any custom kwargs
        default_style.update(kwargs)
        
        super().__init__(parent, text=text, command=command, **default_style)
        
        # Store original colors
        self.default_bg = default_style['bg']
        self.default_fg = default_style['fg']
        self.hover_bg = AppConfig.BUTTON_HOVER_COLOR
        self.hover_fg = AppConfig.TEXT_COLOR
        self.is_active = False
        
        # Bind hover events
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
    
    def _on_enter(self, event):
        """Handle mouse enter (hover)"""
        if not self.is_active:
            self.configure(bg=self.hover_bg, fg=self.hover_fg)
        # If active, don't change colors on hover
    
    def _on_leave(self, event):
        """Handle mouse leave"""
        if not self.is_active:
            self.configure(bg=self.default_bg, fg=self.default_fg)
        else:
            # Ensure active button stays active colored
            self.configure(
                bg=AppConfig.BUTTON_ACTIVE_COLOR,
                fg=AppConfig.BUTTON_ACTIVE_TEXT
            )
    
    def set_active(self, active=True):
        """Set button as active/inactive"""
        self.is_active = active
        if active:
            # Force the active styling
            self.configure(
                bg=AppConfig.BUTTON_ACTIVE_COLOR,
                fg=AppConfig.BUTTON_ACTIVE_TEXT,
                relief=tk.FLAT
            )
            # Update the stored colors so hover doesn't override
            self.current_bg = AppConfig.BUTTON_ACTIVE_COLOR
            self.current_fg = AppConfig.BUTTON_ACTIVE_TEXT
        else:
            # Reset to default styling
            self.configure(
                bg=self.default_bg,
                fg=self.default_fg,
                relief=tk.FLAT
            )
            self.current_bg = self.default_bg
            self.current_fg = self.default_fg

class ModernFrame(tk.Frame):
    """Modern styled frame"""
    
    def __init__(self, parent, **kwargs):
        default_style = {
            'bg': AppConfig.PRIMARY_COLOR,
            'relief': tk.FLAT,
            'bd': 0
        }
        default_style.update(kwargs)
        super().__init__(parent, **default_style)