"""
Application configuration constants
"""

class AppConfig:
    # Window settings
    WINDOW_WIDTH = 840
    WINDOW_HEIGHT = 520
    WINDOW_TITLE = "Python GUI Application"
    
    # Light Theme Colors
    PRIMARY_COLOR = "#f5f5f5"        # Light gray background
    SECONDARY_COLOR = "#e8e8e8"      # Slightly darker light gray
    ACCENT_COLOR = "#0078d4"         # Modern blue accent
    ACCENT_HOVER = "#106ebe"         # Darker blue for hover
    TEXT_COLOR = "#000000"           # Black text
    BUTTON_COLOR = "#ffffff"         # White buttons
    BUTTON_HOVER_COLOR = "#f0f0f0"   # Light gray for hover
    BUTTON_ACTIVE_COLOR = "#333333"  # Dark gray for active state
    BUTTON_ACTIVE_TEXT = "#0000FF"   # White text for active buttons
    BORDER_COLOR = "#d0d0d0"         # Light border color
    
    # Font settings
    FONT_FAMILY = "Segoe UI"
    FONT_SIZE = 11
    BUTTON_FONT_SIZE = 9
    TITLE_FONT_SIZE = 14
    
    # Slideshow settings
    SLIDESHOW_INTERVAL = 2500  # 2500ms auto-change interval
    SLIDESHOW_WIDTH = 840      # Full window width
    SLIDESHOW_HEIGHT = 380     # Reduced height to allow more footer spacing
    SLIDESHOW_BORDER_RADIUS = 16  # Rounded corners