"""
DMI Drag and drop component - shows full file path
"""

import tkinter as tk
from tkinter import filedialog
import os
from constants.app_config import AppConfig
import tkinterdnd2 as tkdnd

class DMIDragDropWidget:
    def __init__(self, parent, label_text="Drop File Here", on_file_selected=None):
        self.parent = parent
        self.label_text = label_text
        self.on_file_selected = on_file_selected
        self.selected_file = None
        self.selected_filepath = None
        
        self.create_drag_drop_area()
    
    def create_drag_drop_area(self):
        """Create the drag and drop area"""
        # Main container
        self.container = tk.Frame(
            self.parent,
            bg="#e8e8e8",
            relief=tk.FLAT,
            bd=0
        )
        
        # Title label
        title_label = tk.Label(
            self.container,
            text=self.label_text,
            font=(AppConfig.FONT_FAMILY, 11, "bold"),
            bg="#e8e8e8",
            fg="#333333"
        )
        title_label.pack(pady=(5, 5))
        
        # Drop area frame
        self.drop_frame = tk.Frame(
            self.container,
            bg="#ffffff",
            relief=tk.RAISED,
            bd=2,
            height=150
        )
        self.drop_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        self.drop_frame.pack_propagate(False)
        
        # Enable drag and drop
        self.drop_frame.drop_target_register(tkdnd.DND_FILES)
        self.drop_frame.dnd_bind('<<Drop>>', self.on_drop)
        self.drop_frame.dnd_bind('<<DragEnter>>', self.on_drag_enter)
        self.drop_frame.dnd_bind('<<DragLeave>>', self.on_drag_leave)
        
        # File icon
        self.file_icon = tk.Label(
            self.drop_frame,
            text="📄",
            font=(AppConfig.FONT_FAMILY, 24),
            bg="#ffffff",
            fg="#666666"
        )
        self.file_icon.pack(pady=(15, 5))
        
        # File selected text
        self.file_text = tk.Label(
            self.drop_frame,
            text="No file selected",
            font=(AppConfig.FONT_FAMILY, 10),
            bg="#ffffff",
            fg="#888888",
            wraplength=280,
            justify=tk.CENTER
        )
        self.file_text.pack(pady=5)
        
        # Full path text
        self.path_text = tk.Label(
            self.drop_frame,
            text="",
            font=(AppConfig.FONT_FAMILY, 8),
            bg="#ffffff",
            fg="#666666",
            wraplength=280,
            justify=tk.CENTER
        )
        self.path_text.pack(pady=(5, 10))
        
        # Click here text
        self.click_text = tk.Label(
            self.drop_frame,
            text="Click to browse",
            font=(AppConfig.FONT_FAMILY, 9),
            bg="#ffffff",
            fg="#4A90E2",
            cursor="hand2"
        )
        self.click_text.pack(pady=(0, 10))
        
        # Bind click event to all elements
        self.drop_frame.bind("<Button-1>", self.select_file)
        self.file_icon.bind("<Button-1>", self.select_file)
        self.file_text.bind("<Button-1>", self.select_file)
        self.path_text.bind("<Button-1>", self.select_file)
        self.click_text.bind("<Button-1>", self.select_file)
    
    def on_drag_enter(self, event):
        """Handle drag enter event"""
        self.drop_frame.configure(bg="#e3f2fd")
        
    def on_drag_leave(self, event):
        """Handle drag leave event"""
        self.drop_frame.configure(bg="#ffffff")
        
    def on_drop(self, event):
        """Handle file drop event"""
        self.drop_frame.configure(bg="#ffffff")
        
        # Get dropped files
        file_data = event.data
        
        # Handle different file path formats
        if file_data.startswith('{') and file_data.endswith('}'):
            file_path = file_data[1:-1]
        else:
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
            self.file_text.configure(
                text="❌ Error: Only .bin files allowed!",
                fg="#f44336"
            )
            self.path_text.configure(text="")
            return
        
        # Store file path
        self.selected_file = os.path.basename(file_path)
        self.selected_filepath = file_path
        
        # Update display
        self.file_icon.configure(
            text="📄✅",
            fg="#4caf50"
        )
        
        self.file_text.configure(
            text=f"File selected: {self.selected_file}",
            fg="#4caf50"
        )
        
        # Show full path
        self.path_text.configure(
            text=file_path,
            fg="#666666"
        )
        
        # Callback to parent
        if self.on_file_selected:
            self.on_file_selected(file_path, self.selected_file)
    
    def reset_file(self):
        """Reset file selection"""
        self.selected_file = None
        self.selected_filepath = None
        
        self.file_icon.configure(
            text="📄",
            fg="#666666"
        )
        
        self.file_text.configure(
            text="No file selected",
            fg="#888888"
        )
        
        self.path_text.configure(text="")
    
    def get_selected_filepath(self):
        """Return the selected file path"""
        return self.selected_filepath
    
    def get_widget(self):
        """Return the main container"""
        return self.container
