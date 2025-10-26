import tkinter as tk
from constants.app_config import AppConfig

class ToolTip:
    """Tooltip widget for showing descriptions on hover"""
    
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)
    
    def show_tooltip(self, event=None):
        """Display the tooltip"""
        if self.tooltip_window or not self.text:
            return
        
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 5
        
        self.tooltip_window = tk.Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)
        self.tooltip_window.wm_geometry(f"+{x}+{y}")
        
        label = tk.Label(
            self.tooltip_window,
            text=self.text,
            background="#333333",
            foreground="#ffffff",
            relief=tk.SOLID,
            borderwidth=1,
            font=(AppConfig.FONT_FAMILY, 9),
            padx=8,
            pady=4
        )
        label.pack()
    
    def hide_tooltip(self, event=None):
        """Hide the tooltip"""
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None

class ModernButton(tk.Button):
    """Modern styled button with hover effects"""
    
    def __init__(self, parent, text="", command=None, is_nav=False, tooltip=None, **kwargs):
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
        
        # Add tooltip if provided
        if tooltip:
            self.tooltip = ToolTip(self, tooltip)
        else:
            self.tooltip = None
    
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
