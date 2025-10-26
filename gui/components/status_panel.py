"""
Status panel component for showing logs and file information - Light theme
"""

import tkinter as tk
from tkinter import scrolledtext
from constants.app_config import AppConfig
import threading
import subprocess
import queue

class StatusPanel:
    def __init__(self, parent):
        self.parent = parent
        self.file_info = {
            'filename': None,
            'generation': 'Unknown',
            'file_system': 'Unknown',
            'status': 'Ready'
        }
        self.command_queue = queue.Queue()
        
        self.create_status_panel()
    
    def create_status_panel(self):
        """Create the status panel"""
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
        
        # File info section
        info_frame = tk.Frame(self.container, bg="#ffffff", relief=tk.RAISED, bd=1)
        info_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # File status
        self.file_status_label = tk.Label(
            info_frame,
            text="No file selected",
            font=(AppConfig.FONT_FAMILY, 10),
            bg="#ffffff",
            fg="#666666"
        )
        self.file_status_label.pack(anchor=tk.W, padx=10, pady=5)
        
        # Generation info
        self.generation_label = tk.Label(
            info_frame,
            text="Generation: Unknown",
            font=(AppConfig.FONT_FAMILY, 10),
            bg="#ffffff",
            fg="#666666"
        )
        self.generation_label.pack(anchor=tk.W, padx=10, pady=2)
        
        # File system info
        self.filesystem_label = tk.Label(
            info_frame,
            text="File System: Unknown",
            font=(AppConfig.FONT_FAMILY, 10),
            bg="#ffffff",
            fg="#666666"
        )
        self.filesystem_label.pack(anchor=tk.W, padx=10, pady=2)
        
        # Ready status
        self.ready_label = tk.Label(
            info_frame,
            text="Ready",
            font=(AppConfig.FONT_FAMILY, 12, "bold"),
            bg="#ffffff",
            fg="#4caf50"  # Green color
        )
        self.ready_label.pack(anchor=tk.W, padx=10, pady=(10, 10))
        
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
            fg="#000000",  # Black text
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
            fg="#000000",  # Black text
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
            command=self.clear_log,
            font=(AppConfig.FONT_FAMILY, AppConfig.BUTTON_FONT_SIZE),
            bg="#757575",
            fg="#000000",  # Black text
            relief=tk.FLAT,
            bd=0,
            highlightthickness=0,
            padx=15,
            pady=8,
            cursor='hand2'
        )
        self.clear_button.pack(side=tk.RIGHT)
        
        # Log area
        log_label = tk.Label(
            self.container,
            text="Command Output:",
            font=(AppConfig.FONT_FAMILY, 10, "bold"),
            bg="#e8e8e8",
            fg="#333333"
        )
        log_label.pack(anchor=tk.W, padx=10, pady=(10, 2))
        
        # Scrolled text for logs (READ-ONLY)
        self.log_text = scrolledtext.ScrolledText(
            self.container,
            height=8,
            bg="#ffffff",
            fg="#333333",  # Dark text on white background
            font=("Consolas", 9),
            relief=tk.RAISED,
            bd=1,
            insertbackground="#333333",
            state=tk.DISABLED,  # Make it read-only
            wrap=tk.WORD
        )
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        # Initial log message
        self.add_log("System ready. Select a .bin file to begin.")
    
    def update_file_info(self, filepath, filename):
        """Update file information display"""
        if filepath:
            self.file_info['filename'] = filename
            self.file_status_label.configure(
                text=f"File: {filename}",
                fg="#4caf50"
            )
            # Simulate file analysis
            self.generation_label.configure(text="Generation: ME 11.x")
            self.filesystem_label.configure(text="File System: UEFI")
            self.add_log(f"File loaded: {filename}")
            self.add_log("File analysis complete. Ready for operations.")
        else:
            self.file_status_label.configure(
                text="No file selected",
                fg="#666666"
            )
            self.generation_label.configure(text="Generation: Unknown")
            self.filesystem_label.configure(text="File System: Unknown")
            self.add_log("File selection cleared.")
    
    def add_log(self, message):
        """Add message to log (read-only)"""
        self.log_text.configure(state=tk.NORMAL)  # Temporarily enable editing
        self.log_text.insert(tk.END, f"> {message}\n")
        self.log_text.see(tk.END)
        self.log_text.configure(state=tk.DISABLED)  # Make read-only again
    
    def clear_log(self):
        """Clear the log"""
        self.log_text.configure(state=tk.NORMAL)
        self.log_text.delete(1.0, tk.END)
        self.add_log("Log cleared.")
    
    def run_build(self):
        """Run build command"""
        if not self.file_info['filename']:
            self.add_log("❌ Error: No file selected!")
            return
        
        self.add_log("🔨 Starting BUILD (ME Clean) process...")
        self.add_log("Initializing ME cleaning tools...")
        # Simulate command execution
        self.simulate_command_output([
            "Loading BIOS file...",
            "Analyzing ME region...",
            "Cleaning ME components...",
            "Rebuilding BIOS structure...",
            "✅ BUILD completed successfully!"
        ])
    
    def run_analysis(self):
        """Run ME analysis"""
        if not self.file_info['filename']:
            self.add_log("❌ Error: No file selected!")
            return
        
        self.add_log("🔍 Starting MEA Analysis...")
        # Simulate command execution
        self.simulate_command_output([
            "Launching ME Analyzer...",
            "Scanning ME firmware...",
            "Extracting ME modules...",
            "Generating analysis report...",
            "✅ Analysis completed successfully!"
        ])
    
    def simulate_command_output(self, messages):
        """Simulate real-time command output"""
        def output_messages():
            for i, msg in enumerate(messages):
                self.parent.after(i * 1000, lambda m=msg: self.add_log(m))
        
        threading.Thread(target=output_messages, daemon=True).start()
    
    def get_widget(self):
        """Return the main container"""
        return self.container