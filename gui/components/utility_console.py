"""
Utility console component - similar to unlock console
"""

import tkinter as tk
from tkinter import scrolledtext
from constants.app_config import AppConfig
from gui.components.modern_button import ModernButton
import threading

class UtilityConsole:
    def __init__(self, parent):
        self.parent = parent
        self.file_info = {
            'filename': None,
            'size': 'Unknown',
            'type': 'Unknown'
        }
        self.is_running_command = False
        self.current_task_thread = None
        self.task_cancelled = False
        
        self.create_console_panel()
    
    def create_console_panel(self):
        """Create the utility console panel"""
        # Main container
        self.container = tk.Frame(
            self.parent,
            bg="#e8e8e8",  # Light gray background
            relief=tk.FLAT,
            bd=0
        )
        
        # Title
        title_label = tk.Label(
            self.container,
            text="Utility Console",
            font=(AppConfig.FONT_FAMILY, 12, "bold"),
            bg="#e8e8e8",
            fg="#333333"
        )
        title_label.pack(pady=(10, 5))
        
        # Console display area
        self.console_frame = tk.Frame(
            self.container, 
            bg="#ffffff", 
            relief=tk.RAISED, 
            bd=1
        )
        self.console_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Console text area
        self.console_text = scrolledtext.ScrolledText(
            self.console_frame,
            height=12,
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
        
        # Operations section
        ops_label = tk.Label(
            self.container,
            text="Operations",
            font=(AppConfig.FONT_FAMILY, 12, "bold"),
            bg="#e8e8e8",
            fg="#333333"
        )
        ops_label.pack(pady=(15, 5))
        
        # Operation buttons grid
        self.create_operation_buttons()
        
        # Initialize with default status
        self.show_default_status()
    
    def create_operation_buttons(self):
        """Create the grid of operation buttons"""
        # Button container
        button_container = tk.Frame(self.container, bg="#e8e8e8")
        button_container.pack(fill=tk.X, padx=10, pady=5)
        
        # Button configurations (color, text, command, tooltip)
        button_configs = [
            # Row 1
            [
                ("#f44336", "UEFI Replace", self.uefi_replace, "Replace UEFI modules in BIOS"),
                ("#9c27b0", "UEFI View", self.uefi_view, "View UEFI modules in BIOS")
            ],
            # Row 2
            [
                ("#ff9800", "RAM Disable", self.ram_disable, "Disable RAM checks in BIOS"),
                ("#8bc34a", "Sanitize BIOS", self.sanitize_bios, "Remove sensitive data from BIOS")
            ],
            # Row 3
            [
                ("#9c27b0", "ME Analyzer", self.me_analyzer, "Analyze Intel ME firmware"),
                ("#f44336", "HP Decrypt", self.hp_decrypt, "Decrypt HP BIOS files")
            ],
            # Row 4
            [
                ("", "", None, ""),  # Empty slot
                ("#757575", "Clear", self.clear_console, "Clear console and reset")
            ]
        ]
        
        # Create button grid
        for row_idx, row in enumerate(button_configs):
            row_frame = tk.Frame(button_container, bg="#e8e8e8")
            row_frame.pack(fill=tk.X, pady=2)
            
            for col_idx, (color, text, command, tooltip) in enumerate(row):
                if text:  # Only create button if text is provided
                    # Make Clear button smaller
                    if text == "Clear":
                        btn = ModernButton(
                            row_frame,
                            text=text,
                            command=command,
                            tooltip=tooltip,
                            bg=color,
                            fg="#000000",  # Black text
                            padx=10,
                            pady=8,
                            width=8
                        )
                        btn.pack(side=tk.LEFT, padx=2)
                    else:
                        btn = ModernButton(
                            row_frame,
                            text=text,
                            command=command,
                            tooltip=tooltip,
                            bg=color,
                            fg="#000000",  # Black text
                            padx=10,
                            pady=8,
                            width=15
                        )
                        btn.pack(side=tk.LEFT, padx=2, fill=tk.X, expand=True)
                else:
                    # Empty spacer
                    spacer = tk.Frame(row_frame, bg="#e8e8e8")
                    spacer.pack(side=tk.LEFT, padx=2, fill=tk.X, expand=True)
    
    def show_default_status(self):
        """Show the default file status information"""
        self.console_text.configure(state=tk.NORMAL)
        self.console_text.delete(1.0, tk.END)
        
        # File information
        if self.file_info['filename']:
            self.console_text.insert(tk.END, f"File: {self.file_info['filename']}\n")
        else:
            self.console_text.insert(tk.END, "No file selected\n")
        
        self.console_text.insert(tk.END, f"Size: {self.file_info['size']}\n")
        self.console_text.insert(tk.END, f"Type: {self.file_info['type']}\n\n")
        
        # Ready status in green
        self.console_text.insert(tk.END, "Ready", "ready")
        
        # Configure green color for "Ready"
        self.console_text.tag_configure("ready", foreground="#4caf50", font=("Consolas", 9, "bold"))
        
        self.console_text.configure(state=tk.DISABLED)
        self.is_running_command = False
    
    def update_file_info(self, filepath, filename, reset_all=False):
        """Update file information and refresh status display"""
        if reset_all:
            self.stop_all_tasks()
            self.file_info['filename'] = None
            self.file_info['size'] = 'Unknown'
            self.file_info['type'] = 'Unknown'
        elif filepath:
            self.file_info['filename'] = filename
            # Simulate file analysis
            import os
            size_bytes = os.path.getsize(filepath)
            size_mb = size_bytes / (1024 * 1024)
            self.file_info['size'] = f"{size_mb:.2f} MB"
            self.file_info['type'] = 'BIOS Binary'
        else:
            self.file_info['filename'] = None
            self.file_info['size'] = 'Unknown'
            self.file_info['type'] = 'Unknown'
        
        # Refresh the status display
        if not self.is_running_command or reset_all:
            self.show_default_status()
    
    def add_console_output(self, message):
        """Add message to console (read-only)"""
        self.console_text.configure(state=tk.NORMAL)
        self.console_text.insert(tk.END, f"> {message}\n")
        self.console_text.see(tk.END)
        self.console_text.configure(state=tk.DISABLED)
    
    def start_command_mode(self):
        """Switch to command output mode"""
        self.is_running_command = True
        self.console_text.configure(state=tk.NORMAL)
        self.console_text.delete(1.0, tk.END)
        self.console_text.configure(state=tk.DISABLED)
    
    def clear_console(self):
        """Clear console and return to default status view"""
        self.stop_all_tasks()
        self.show_default_status()
    
    def stop_all_tasks(self):
        """Stop all running tasks"""
        self.task_cancelled = True
        self.is_running_command = False
        
        if self.current_task_thread and self.current_task_thread.is_alive():
            self.task_cancelled = True
        
        self.current_task_thread = None
    
    def run_utility_operation(self, operation_name, messages):
        """Run a utility operation with console output"""
        if not self.file_info['filename']:
            self.start_command_mode()
            self.add_console_output("❌ Error: No file selected!")
            return
        
        self.stop_all_tasks()
        self.start_command_mode()
        self.add_console_output(f"🔧 Starting {operation_name}...")
        
        self.simulate_command_output(messages, operation_name)
    
    def simulate_command_output(self, messages, task_name):
        """Simulate real-time command output"""
        def output_messages():
            self.task_cancelled = False
            for i, msg in enumerate(messages):
                if self.task_cancelled:
                    self.parent.after(0, lambda: self.add_console_output(f"❌ {task_name} cancelled by user"))
                    break
                
                self.parent.after(i * 800, lambda m=msg: self.add_console_output(m) if not self.task_cancelled else None)
        
        self.current_task_thread = threading.Thread(target=output_messages, daemon=True)
        self.current_task_thread.start()
    
    # Operation button handlers
    def uefi_replace(self):
        """UEFI Replace operation"""
        messages = [
            "Initializing UEFI Replace...",
            "Scanning BIOS structure...",
            "Identifying UEFI modules...",
            "Replacing UEFI modules...",
            "✅ UEFI Replace completed successfully!"
        ]
        self.run_utility_operation("UEFI Replace", messages)
    
    def uefi_view(self):
        """UEFI View operation"""
        messages = [
            "Starting UEFI View...",
            "Reading BIOS structure...",
            "Extracting UEFI modules...",
            "Listing UEFI components...",
            "✅ UEFI View completed!"
        ]
        self.run_utility_operation("UEFI View", messages)
    
    def ram_disable(self):
        """RAM Disable operation"""
        messages = [
            "Initiating RAM Disable...",
            "Locating RAM check routines...",
            "Patching RAM verification...",
            "Disabling RAM checks...",
            "✅ RAM Disable successful!"
        ]
        self.run_utility_operation("RAM Disable", messages)
    
    def sanitize_bios(self):
        """Sanitize BIOS operation"""
        messages = [
            "Starting BIOS Sanitization...",
            "Scanning for sensitive data...",
            "Removing serial numbers...",
            "Clearing identifiers...",
            "✅ BIOS Sanitization completed!"
        ]
        self.run_utility_operation("Sanitize BIOS", messages)
    
    def me_analyzer(self):
        """ME Analyzer operation"""
        messages = [
            "Analyzing Intel ME firmware...",
            "Extracting ME region...",
            "Checking ME version...",
            "Analyzing ME modules...",
            "✅ ME Analysis completed!"
        ]
        self.run_utility_operation("ME Analyzer", messages)
    
    def hp_decrypt(self):
        """HP Decrypt operation"""
        messages = [
            "Starting HP BIOS decryption...",
            "Detecting encryption type...",
            "Applying decryption keys...",
            "Decrypting BIOS data...",
            "✅ HP Decrypt completed!"
        ]
        self.run_utility_operation("HP Decrypt", messages)
    
    def get_widget(self):
        """Return the main container"""
        return self.container
