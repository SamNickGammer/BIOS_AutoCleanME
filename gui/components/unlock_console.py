"""
Unlock console component - simplified like ME Clean Auto
"""

import tkinter as tk
from tkinter import scrolledtext
from constants.app_config import AppConfig
from gui.components.modern_button import ModernButton
import threading

class UnlockConsole:
    def __init__(self, parent):
        self.parent = parent
        self.file_info = {
            'filename': None,
            'device': 'Unknown',
            'security': 'Unknown'
        }
        self.is_running_command = False
        self.current_task_thread = None
        self.task_cancelled = False
        
        self.create_console_panel()
    
    def create_console_panel(self):
        """Create the unlock console panel (like ME Clean Status)"""
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
            text="Unlock Console",
            font=(AppConfig.FONT_FAMILY, 12, "bold"),
            bg="#e8e8e8",
            fg="#333333"
        )
        title_label.pack(pady=(10, 5))
        
        # Console display area (like ME Clean terminal)
        self.console_frame = tk.Frame(
            self.container, 
            bg="#ffffff", 
            relief=tk.RAISED, 
            bd=1
        )
        self.console_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Console text area (shows status initially, then command output)
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
                ("#f44336", "Dell ST Fix", self.dell_st_fix, "Fix Dell ST issues"),
                ("#f44336", "Dell 8FC8 Unlock", self.dell_8fc8_unlock, "Unlock Dell 8FC8 BIOS")
            ],
            # Row 2
            [
                ("#9c27b0", "HP Admin Unlock", self.hp_admin_unlock, "Unlock HP Admin password"),
                ("#8bc34a", "Endpoint Clean", self.endpoint_clean, "Fix EndPoint Security")
            ],
            # Row 3
            [
                ("#9c27b0", "Device Freeze Fix", self.device_freeze_fix, "Fix device freeze issues"),
                ("#9c27b0", "Lost Mode Fix", self.lost_mode_fix, "Fix lost mode problems")
            ],
            # Row 4
            [
                ("#9c27b0", "School MPM Fix", self.school_mpm_fix, "Fix school login issues"),
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
    
    def show_default_status(self):
        """Show the default file status information (like ME Clean)"""
        self.console_text.configure(state=tk.NORMAL)
        self.console_text.delete(1.0, tk.END)
        
        # File information
        if self.file_info['filename']:
            self.console_text.insert(tk.END, f"File: {self.file_info['filename']}\n")
        else:
            self.console_text.insert(tk.END, "No file selected\n")
        
        self.console_text.insert(tk.END, f"Device: {self.file_info['device']}\n")
        self.console_text.insert(tk.END, f"Security: {self.file_info['security']}\n\n")
        
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
            self.file_info['device'] = 'Unknown'
            self.file_info['security'] = 'Unknown'
        elif filepath:
            self.file_info['filename'] = filename
            # Simulate file analysis
            self.file_info['device'] = 'Dell/HP System'
            self.file_info['security'] = 'Locked'
        else:
            self.file_info['filename'] = None
            self.file_info['device'] = 'Unknown'
            self.file_info['security'] = 'Unknown'
        
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
    
    def run_unlock_operation(self, operation_name, messages):
        """Run an unlock operation with console output"""
        if not self.file_info['filename']:
            self.start_command_mode()
            self.add_console_output("❌ Error: No file selected!")
            return
        
        self.stop_all_tasks()
        self.start_command_mode()
        self.add_console_output(f"🔓 Starting {operation_name}...")
        
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
    def dell_st_fix(self):
        """Dell ST Fix operation"""
        messages = [
            "Initializing Dell ST Fix...",
            "Scanning BIOS structure...",
            "Identifying ST protection...",
            "Applying ST bypass...",
            "✅ Dell ST Fix completed successfully!"
        ]
        self.run_unlock_operation("Dell ST Fix", messages)
    
    def dell_8fc8_unlock(self):
        """Dell 8FC8 Unlock operation"""
        messages = [
            "Starting Dell 8FC8 unlock process...",
            "Reading BIOS protection flags...",
            "Bypassing 8FC8 security...",
            "Patching unlock regions...",
            "✅ Dell 8FC8 unlock completed!"
        ]
        self.run_unlock_operation("Dell 8FC8 Unlock", messages)
    
    def hp_admin_unlock(self):
        """HP Admin Unlock operation"""
        messages = [
            "Initiating HP Admin unlock...",
            "Scanning admin password hash...",
            "Applying unlock patches...",
            "Clearing admin restrictions...",
            "✅ HP Admin unlock successful!"
        ]
        self.run_unlock_operation("HP Admin Unlock", messages)
    
    def endpoint_clean(self):
        """Endpoint Clean operation"""
        messages = [
            "Starting EndPoint Security clean...",
            "Detecting security modules...",
            "Removing endpoint restrictions...",
            "Cleaning security traces...",
            "✅ EndPoint clean completed!"
        ]
        self.run_unlock_operation("Endpoint Clean", messages)
    
    def device_freeze_fix(self):
        """Device Freeze Fix operation"""
        messages = [
            "Analyzing device freeze issues...",
            "Checking thermal management...",
            "Fixing freeze triggers...",
            "Optimizing system stability...",
            "✅ Device freeze fix applied!"
        ]
        self.run_unlock_operation("Device Freeze Fix", messages)
    
    def lost_mode_fix(self):
        """Lost Mode Fix operation"""
        messages = [
            "Detecting lost mode status...",
            "Bypassing lost mode locks...",
            "Clearing activation flags...",
            "Restoring normal operation...",
            "✅ Lost mode fix completed!"
        ]
        self.run_unlock_operation("Lost Mode Fix", messages)
    
    def school_mpm_fix(self):
        """School MPM Fix operation"""
        messages = [
            "Starting school MPM fix...",
            "Scanning MDM profiles...",
            "Removing school restrictions...",
            "Clearing enrollment data...",
            "✅ School MPM fix successful!"
        ]
        self.run_unlock_operation("School MPM Fix", messages)
    
    def get_widget(self):
        """Return the main container"""
        return self.container