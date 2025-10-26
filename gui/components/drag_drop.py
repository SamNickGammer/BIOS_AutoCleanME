"""
Drag and drop component for file selection - Light theme with working drag & drop
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import os
from constants.app_config import AppConfig
import tkinterdnd2 as tkdnd

class DragDropWidget:
    def __init__(self, parent, on_file_selected=None):
        self.parent = parent
        self.on_file_selected = on_file_selected
        self.selected_file = None
        
        self.create_drag_drop_area()
    
    def create_drag_drop_area(self):
        """Create the drag and drop area"""
        # Main container
        self.container = tk.Frame(
            self.parent,
            bg="#e8e8e8",  # Light gray background
            relief=tk.FLAT,
            bd=0
        )
        
        # Drop area frame
        self.drop_frame = tk.Frame(
            self.container,
            bg="#ffffff",  # White background
            relief=tk.RAISED,
            bd=2,
            height=200
        )
        self.drop_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.drop_frame.pack_propagate(False)
        
        # Enable drag and drop
        self.drop_frame.drop_target_register(tkdnd.DND_FILES)
        self.drop_frame.dnd_bind('<<Drop>>', self.on_drop)
        self.drop_frame.dnd_bind('<<DragEnter>>', self.on_drag_enter)
        self.drop_frame.dnd_bind('<<DragLeave>>', self.on_drag_leave)
        
        # File icon (using text for now)
        self.file_icon = tk.Label(
            self.drop_frame,
            text="📄",
            font=(AppConfig.FONT_FAMILY, 32),
            bg="#ffffff",
            fg="#666666"
        )
        self.file_icon.pack(pady=(30, 10))
        
        # Main text
        self.main_text = tk.Label(
            self.drop_frame,
            text="Drag & Drop File",
            font=(AppConfig.FONT_FAMILY, 14, "bold"),
            bg="#ffffff",
            fg="#333333"
        )
        self.main_text.pack(pady=5)
        
        # Click text
        self.click_text = tk.Label(
            self.drop_frame,
            text="Click Here",
            font=(AppConfig.FONT_FAMILY, 12),
            bg="#ffffff",
            fg="#666666"
        )
        self.click_text.pack(pady=5)
        
        # File status
        self.status_text = tk.Label(
            self.drop_frame,
            text="No file selected",
            font=(AppConfig.FONT_FAMILY, 10),
            bg="#ffffff",
            fg="#888888"
        )
        self.status_text.pack(pady=(20, 10))
        
        # Reset button (initially hidden)
        self.reset_button = tk.Button(
            self.container,
            text="Reset",
            command=self.reset_file,
            font=(AppConfig.FONT_FAMILY, AppConfig.BUTTON_FONT_SIZE),
            bg="#f44336",
            fg="#000000",  # Black text
            relief=tk.FLAT,
            bd=0,
            highlightthickness=0,
            padx=15,
            pady=5,
            cursor='hand2'
        )
        
        # Bind click event to all elements
        self.drop_frame.bind("<Button-1>", self.select_file)
        self.file_icon.bind("<Button-1>", self.select_file)
        self.main_text.bind("<Button-1>", self.select_file)
        self.click_text.bind("<Button-1>", self.select_file)
        self.status_text.bind("<Button-1>", self.select_file)
    
    def on_drag_enter(self, event):
        """Handle drag enter event"""
        self.drop_frame.configure(bg="#e3f2fd")  # Light blue highlight
        
    def on_drag_leave(self, event):
        """Handle drag leave event"""
        self.drop_frame.configure(bg="#ffffff")  # Back to white
        
    def on_drop(self, event):
        """Handle file drop event"""
        self.drop_frame.configure(bg="#ffffff")  # Reset background
        
        # Get dropped files - handle different formats
        file_data = event.data
        
        # Handle different file path formats
        if file_data.startswith('{') and file_data.endswith('}'):
            # Remove braces and split
            file_path = file_data[1:-1]
        else:
            # Split and take first file
            files = file_data.split()
            if files:
                file_path = files[0]
            else:
                return
        
        # Clean up the path
        file_path = file_path.strip().strip('"').strip("'")
        
        if file_path:
            self.process_file(file_path)
    
    def select_file(self, event=None):
        """Open file dialog to select .bin file"""
        file_path = filedialog.askopenfilename(
            title="Select BIOS File",
            filetypes=[("Binary files", "*.bin"), ("All files", "*.*")]
        )
        
        if file_path:
            self.process_file(file_path)
    
    def process_file(self, file_path):
        """Process the selected file"""
        # Check if file is .bin
        if not file_path.lower().endswith('.bin'):
            # Show error message
            error_label = tk.Label(
                self.drop_frame,
                text="❌ Error: Only .bin files are allowed!",
                font=(AppConfig.FONT_FAMILY, 10, "bold"),
                bg="#ffffff",
                fg="#f44336"
            )
            error_label.pack(pady=5)
            # Remove error after 3 seconds
            self.drop_frame.after(3000, error_label.destroy)
            return
        
        # Store file path
        self.selected_file = file_path
        
        # Get filename and truncate if too long
        filename = os.path.basename(file_path)
        if len(filename) > 15:
            display_name = filename[:12] + "..."
        else:
            display_name = filename
        
        # Update status
        self.status_text.configure(
            text=f"Selected: {display_name}",
            fg="#4caf50"  # Green color
        )
        
        # Show reset button
        self.reset_button.pack(pady=(0, 10))
        
        # Callback to parent
        if self.on_file_selected:
            self.on_file_selected(file_path, filename)
    
    def reset_file(self):
        """Reset the file selection"""
        self.selected_file = None
        self.status_text.configure(
            text="No file selected",
            fg="#888888"
        )
        self.reset_button.pack_forget()
        
        # Callback to parent
        if self.on_file_selected:
            self.on_file_selected(None, None)
    
    def get_widget(self):
        """Return the main container"""
        return self.container