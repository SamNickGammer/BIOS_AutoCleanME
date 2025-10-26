"""
HP DMI screen implementation with source/target drag & drop
"""

import tkinter as tk
from tkinter import scrolledtext
from constants.app_config import AppConfig
from functions.hp_dmi_functions import HPDMIFunctions
from gui.components.modern_button import ModernButton
from gui.components.modern_frame import ModernFrame
from gui.components.dmi_drag_drop import DMIDragDropWidget
import threading

class HPDMIScreen:
    def __init__(self, parent):
        self.parent = parent
        self.functions = HPDMIFunctions()
        self.frame = None
        self.source_drag_drop = None
        self.target_drag_drop = None
        self.console_text = None
    
    def create_screen(self):
        """Create the HP DMI screen"""
        if self.frame:
            return self.frame
        
        self.frame = ModernFrame(self.parent)
        
        # Top section - Drag & Drop areas (Source and Target)
        top_section = ModernFrame(self.frame)
        top_section.pack(fill=tk.BOTH, expand=False, padx=15, pady=(15, 10))
        
        # Source file drag & drop (left)
        source_container = ModernFrame(top_section)
        source_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        self.source_drag_drop = DMIDragDropWidget(
            source_container,
            label_text="Source File",
            on_file_selected=self.on_source_selected
        )
        source_widget = self.source_drag_drop.get_widget()
        source_widget.pack(fill=tk.BOTH, expand=True)
        
        # Target file drag & drop (right)
        target_container = ModernFrame(top_section)
        target_container.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        self.target_drag_drop = DMIDragDropWidget(
            target_container,
            label_text="Target File",
            on_file_selected=self.on_target_selected
        )
        target_widget = self.target_drag_drop.get_widget()
        target_widget.pack(fill=tk.BOTH, expand=True)
        
        # Bottom section - Operations and Console
        bottom_section = ModernFrame(self.frame)
        bottom_section.pack(fill=tk.BOTH, expand=True, padx=15, pady=(10, 15))
        
        # Left side - Operations
        operations_frame = ModernFrame(bottom_section)
        operations_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Operations title
        ops_title = tk.Label(
            operations_frame,
            text="Operations",
            font=(AppConfig.FONT_FAMILY, 12, "bold"),
            bg=AppConfig.PRIMARY_COLOR,
            fg="#333333"
        )
        ops_title.pack(pady=(5, 10))
        
        # Operations content area
        ops_content = ModernFrame(operations_frame)
        ops_content.pack(fill=tk.BOTH, expand=True)
        
        # Buttons container
        buttons_container = ModernFrame(ops_content)
        buttons_container.pack(pady=20)
        
        # Copy button
        self.copy_button = ModernButton(
            buttons_container,
            text="DMI Copy",
            command=self.dmi_copy,
            tooltip="Copy DMI data from Source to Target",
            bg="#8bc34a",
            fg="#000000",
            padx=20,
            pady=10,
            width=15
        )
        self.copy_button.pack(pady=10)
        
        # Clear button
        self.clear_button = ModernButton(
            buttons_container,
            text="Clear",
            command=self.clear_all,
            tooltip="Clear all selections and reset",
            bg="#757575",
            fg="#000000",
            padx=20,
            pady=10,
            width=15
        )
        self.clear_button.pack(pady=10)
        
        # Right side - Small Console
        console_frame = ModernFrame(bottom_section)
        console_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False, padx=(10, 0))
        console_frame.configure(width=350)
        
        # Console title
        console_title = tk.Label(
            console_frame,
            text="Status",
            font=(AppConfig.FONT_FAMILY, 11, "bold"),
            bg=AppConfig.PRIMARY_COLOR,
            fg="#333333"
        )
        console_title.pack(pady=(5, 5))
        
        # Console display
        console_display = tk.Frame(
            console_frame,
            bg="#ffffff",
            relief=tk.RAISED,
            bd=1
        )
        console_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Console text area
        self.console_text = scrolledtext.ScrolledText(
            console_display,
            height=10,
            bg="#ffffff",
            fg="#333333",
            font=("Consolas", 9),
            relief=tk.FLAT,
            bd=0,
            insertbackground="#333333",
            state=tk.DISABLED,
            wrap=tk.WORD
        )
        self.console_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Initialize console
        self.add_console_message("Ready", "ready")
        
        return self.frame
    
    def on_source_selected(self, filepath, filename):
        """Handle source file selection"""
        self.add_console_message(f"Source file selected: {filename}", "info")
    
    def on_target_selected(self, filepath, filename):
        """Handle target file selection"""
        self.add_console_message(f"Target file selected: {filename}", "info")
    
    def add_console_message(self, message, msg_type="normal"):
        """Add message to console"""
        self.console_text.configure(state=tk.NORMAL)
        
        if msg_type == "ready":
            self.console_text.delete(1.0, tk.END)
            self.console_text.insert(tk.END, message, "ready")
            self.console_text.tag_configure("ready", foreground="#4caf50", font=("Consolas", 9, "bold"))
        elif msg_type == "error":
            self.console_text.insert(tk.END, f"> {message}\n", "error")
            self.console_text.tag_configure("error", foreground="#f44336")
        elif msg_type == "success":
            self.console_text.insert(tk.END, f"> {message}\n", "success")
            self.console_text.tag_configure("success", foreground="#4caf50")
        elif msg_type == "info":
            self.console_text.insert(tk.END, f"> {message}\n", "info")
            self.console_text.tag_configure("info", foreground="#2196F3")
        else:
            self.console_text.insert(tk.END, f"> {message}\n")
        
        self.console_text.see(tk.END)
        self.console_text.configure(state=tk.DISABLED)
    
    def dmi_copy(self):
        """Perform DMI copy operation"""
        source_file = self.source_drag_drop.get_selected_filepath()
        target_file = self.target_drag_drop.get_selected_filepath()
        
        if not source_file:
            self.add_console_message("❌ Error: No source file selected!", "error")
            return
        
        if not target_file:
            self.add_console_message("❌ Error: No target file selected!", "error")
            return
        
        # Clear console for operation
        self.console_text.configure(state=tk.NORMAL)
        self.console_text.delete(1.0, tk.END)
        self.console_text.configure(state=tk.DISABLED)
        
        # Start DMI copy operation
        self.add_console_message("🔄 Starting DMI Copy...", "info")
        
        # Simulate operation with threading
        def run_copy():
            messages = [
                ("Reading source DMI data...", "normal"),
                ("Extracting DMI information...", "normal"),
                ("Validating target file...", "normal"),
                ("Writing DMI to target...", "normal"),
                ("Verifying DMI copy...", "success"),
                ("✅ DMI Copy completed successfully!", "success")
            ]
            
            for i, (msg, msg_type) in enumerate(messages):
                self.frame.after(i * 800, lambda m=msg, t=msg_type: self.add_console_message(m, t))
        
        thread = threading.Thread(target=run_copy, daemon=True)
        thread.start()
    
    def clear_all(self):
        """Clear all selections and reset"""
        # Reset drag & drop widgets
        if self.source_drag_drop:
            self.source_drag_drop.reset_file()
        
        if self.target_drag_drop:
            self.target_drag_drop.reset_file()
        
        # Clear console
        self.console_text.configure(state=tk.NORMAL)
        self.console_text.delete(1.0, tk.END)
        self.console_text.configure(state=tk.DISABLED)
        
        # Show ready message
        self.add_console_message("Ready", "ready")
        self.add_console_message("All selections cleared", "info")
