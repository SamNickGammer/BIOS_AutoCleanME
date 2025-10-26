"""
Status panel component with integrated terminal-style command output
"""

import tkinter as tk
from tkinter import scrolledtext
from constants.app_config import AppConfig
import threading

class StatusPanel:
    def __init__(self, parent):
        self.parent = parent
        self.file_info = {
            'filename': None,
            'generation': 'Unknown',
            'file_system': 'Unknown',
            'status': 'Ready'
        }
        self.is_running_command = False
        self.current_task_thread = None
        self.task_cancelled = False
        
        self.create_status_panel()
    
    def create_status_panel(self):
        """Create the status panel with integrated terminal view"""
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
            text="ME Clean Status",
            font=(AppConfig.FONT_FAMILY, 12, "bold"),
            bg="#e8e8e8",
            fg="#333333"
        )
        title_label.pack(pady=(10, 5))
        
        # Status display area (terminal-style)
        self.status_frame = tk.Frame(
            self.container, 
            bg="#ffffff", 
            relief=tk.RAISED, 
            bd=1
        )
        self.status_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Terminal-style text area (initially shows file info, then command output)
        self.status_text = scrolledtext.ScrolledText(
            self.status_frame,
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
        self.status_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Operations section
        ops_label = tk.Label(
            self.container,
            text="Operations",
            font=(AppConfig.FONT_FAMILY, 12, "bold"),
            bg="#e8e8e8",
            fg="#333333"
        )
        ops_label.pack(pady=(15, 5))
        
        # Operation buttons
        button_frame = tk.Frame(self.container, bg="#e8e8e8")
        button_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Build button
        self.build_button = tk.Button(
            button_frame,
            text="BUILD (ME Clean)",
            command=self.run_build,
            font=(AppConfig.FONT_FAMILY, AppConfig.BUTTON_FONT_SIZE),
            bg="#2196f3",
            fg="#000000",
            relief=tk.FLAT,
            bd=0,
            highlightthickness=0,
            padx=15,
            pady=8,
            cursor='hand2'
        )
        self.build_button.pack(side=tk.LEFT, padx=(0, 5))
        
        # ME Analysis button
        self.analysis_button = tk.Button(
            button_frame,
            text="MEA Analysis",
            command=self.run_analysis,
            font=(AppConfig.FONT_FAMILY, AppConfig.BUTTON_FONT_SIZE),
            bg="#ff9800",
            fg="#000000",
            relief=tk.FLAT,
            bd=0,
            highlightthickness=0,
            padx=15,
            pady=8,
            cursor='hand2'
        )
        self.analysis_button.pack(side=tk.LEFT, padx=5)
        
        # Clear button
        self.clear_button = tk.Button(
            button_frame,
            text="Clear",
            command=self.clear_status,
            font=(AppConfig.FONT_FAMILY, AppConfig.BUTTON_FONT_SIZE),
            bg="#757575",
            fg="#000000",
            relief=tk.FLAT,
            bd=0,
            highlightthickness=0,
            padx=15,
            pady=8,
            cursor='hand2'
        )
        self.clear_button.pack(side=tk.RIGHT)
        
        # Initialize with default status
        self.show_default_status()
    
    def show_default_status(self):
        """Show the default file status information"""
        self.status_text.configure(state=tk.NORMAL)
        self.status_text.delete(1.0, tk.END)
        
        # File information
        if self.file_info['filename']:
            self.status_text.insert(tk.END, f"File: {self.file_info['filename']}\n")
        else:
            self.status_text.insert(tk.END, "No file selected\n")
        
        self.status_text.insert(tk.END, f"Generation: {self.file_info['generation']}\n")
        self.status_text.insert(tk.END, f"File System: {self.file_info['file_system']}\n\n")
        
        # Ready status in green
        self.status_text.insert(tk.END, "Ready", "ready")
        
        # Configure green color for "Ready"
        self.status_text.tag_configure("ready", foreground="#4caf50", font=("Consolas", 9, "bold"))
        
        self.status_text.configure(state=tk.DISABLED)
        self.is_running_command = False
    
    def update_file_info(self, filepath, filename, reset_all=False):
        """Update file information and refresh status display"""
        if reset_all:
            # Master reset - stop all tasks and clear everything
            self.stop_all_tasks()
            self.file_info['filename'] = None
            self.file_info['generation'] = 'Unknown'
            self.file_info['file_system'] = 'Unknown'
        elif filepath:
            self.file_info['filename'] = filename
            # Simulate file analysis
            self.file_info['generation'] = 'ME 11.x'
            self.file_info['file_system'] = 'UEFI'
        else:
            self.file_info['filename'] = None
            self.file_info['generation'] = 'Unknown'
            self.file_info['file_system'] = 'Unknown'
        
        # Refresh the status display
        if not self.is_running_command or reset_all:
            self.show_default_status()
    
    def add_command_output(self, message):
        """Add command output to the status area"""
        self.status_text.configure(state=tk.NORMAL)
        self.status_text.insert(tk.END, f"> {message}\n")
        self.status_text.see(tk.END)
        self.status_text.configure(state=tk.DISABLED)
    
    def start_command_mode(self):
        """Switch to command output mode"""
        self.is_running_command = True
        self.status_text.configure(state=tk.NORMAL)
        self.status_text.delete(1.0, tk.END)
        self.status_text.configure(state=tk.DISABLED)
    
    def clear_status(self):
        """Clear status and return to default file information view"""
        self.stop_all_tasks()
        self.show_default_status()
    
    def stop_all_tasks(self):
        """Stop all running tasks and reset to ready state"""
        # Cancel any running tasks
        self.task_cancelled = True
        self.is_running_command = False
        
        # If there's a running thread, mark it for cancellation
        if self.current_task_thread and self.current_task_thread.is_alive():
            self.task_cancelled = True
        
        # Reset task state
        self.current_task_thread = None
    
    def run_build(self):
        """Run build command with output in status area"""
        if not self.file_info['filename']:
            self.start_command_mode()
            self.add_command_output("❌ Error: No file selected!")
            return
        
        # Stop any existing tasks
        self.stop_all_tasks()
        
        # Switch to command mode
        self.start_command_mode()
        self.add_command_output("🔨 Starting BUILD (ME Clean) process...")
        self.add_command_output("Initializing ME cleaning tools...")
        
        # Simulate command execution
        self.simulate_command_output([
            "Loading BIOS file...",
            "Analyzing ME region...",
            "Cleaning ME components...",
            "Rebuilding BIOS structure...",
            "✅ BUILD completed successfully!"
        ], "BUILD")
    
    def run_analysis(self):
        """Run ME analysis with output in status area"""
        if not self.file_info['filename']:
            self.start_command_mode()
            self.add_command_output("❌ Error: No file selected!")
            return
        
        # Stop any existing tasks
        self.stop_all_tasks()
        
        # Switch to command mode
        self.start_command_mode()
        self.add_command_output("🔍 Starting MEA Analysis...")
        
        # Simulate command execution
        self.simulate_command_output([
            "Launching ME Analyzer...",
            "Scanning ME firmware...",
            "Extracting ME modules...",
            "Generating analysis report...",
            "✅ Analysis completed successfully!"
        ], "ANALYSIS")
    
    def simulate_command_output(self, messages, task_name):
        """Simulate real-time command output with cancellation support"""
        def output_messages():
            self.task_cancelled = False
            for i, msg in enumerate(messages):
                if self.task_cancelled:
                    # Task was cancelled, show cancellation message
                    self.parent.after(0, lambda: self.add_command_output(f"❌ {task_name} task cancelled by user"))
                    break
                
                # Schedule the message output
                self.parent.after(i * 1000, lambda m=msg: self.add_command_output(m) if not self.task_cancelled else None)
        
        # Start the task thread
        self.current_task_thread = threading.Thread(target=output_messages, daemon=True)
        self.current_task_thread.start()
    
    def get_widget(self):
        """Return the main container"""
        return self.container