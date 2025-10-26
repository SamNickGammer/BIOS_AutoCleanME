# Development Guide - BIOS Utility Toolkit

## Getting Started as a Developer

### Prerequisites Checklist

- [ ] Python 3.7 or higher installed
- [ ] pip package manager available
- [ ] Git installed (for version control)
- [ ] Code editor (VS Code, PyCharm, etc.)
- [ ] Basic understanding of Python and tkinter

### Initial Setup

1. **Clone the repository**

```bash
git clone <repository-url>
cd <project-directory>
```

2. **Create virtual environment (recommended)**

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Verify installation**

```bash
python main.py
```

### Project Structure Understanding

Before making changes, familiarize yourself with:

- `constants/app_config.py` - All configuration values
- `gui/main_window.py` - Navigation and screen management
- `gui/screens/` - Individual screen implementations
- `gui/components/` - Reusable UI components
- `functions/` - Business logic (separate from GUI)

## Development Workflow

### 1. Understanding the Codebase

#### Start with main.py

```python
# Entry point - very simple
from gui.main_window import MainWindow

def main():
    app = MainWindow()  # Creates window
    app.run()           # Starts event loop
```

#### Explore MainWindow

- Located in `gui/main_window.py`
- Manages navigation and screen switching
- Creates all screens on initialization
- Handles button states

#### Study a Simple Screen

Start with `home_screen.py`:

- Simple slideshow implementation
- Good example of component usage
- Shows timer-based updates

#### Examine Components

Look at `modern_button.py`:

- Shows hover effects
- Active/inactive states
- Callback patterns

### 2. Making Your First Change

#### Example: Change Window Title

1. **Open** `constants/app_config.py`
2. **Find** `WINDOW_TITLE = "Python GUI Application"`
3. **Change** to your desired title
4. **Save** and run `python main.py`
5. **Verify** the change appears

#### Example: Add a New Color

1. **Open** `constants/app_config.py`
2. **Add** new color constant:

```python
SUCCESS_COLOR = "#4caf50"  # Green for success messages
```

3. **Use** in your code:

```python
from constants.app_config import AppConfig
label.configure(fg=AppConfig.SUCCESS_COLOR)
```

### 3. Adding a New Screen

#### Step-by-Step Process

**Step 1: Create Screen File**

Create `gui/screens/my_new_screen.py`:

```python
"""
My New Screen implementation
"""

import tkinter as tk
from constants.app_config import AppConfig
from functions.my_functions import MyFunctions
from gui.components.modern_frame import ModernFrame
from gui.components.modern_button import ModernButton

class MyNewScreen:
    def __init__(self, parent):
        self.parent = parent
        self.functions = MyFunctions()
        self.frame = None

    def create_screen(self):
        """Create the screen"""
        if self.frame:
            return self.frame  # Return existing frame

        self.frame = ModernFrame(self.parent)

        # Add your widgets here
        title = tk.Label(
            self.frame,
            text="My New Screen",
            font=(AppConfig.FONT_FAMILY, 16, "bold"),
            bg=AppConfig.PRIMARY_COLOR,
            fg=AppConfig.TEXT_COLOR
        )
        title.pack(pady=20)

        # Add a button
        btn = ModernButton(
            self.frame,
            text="Click Me",
            command=self.on_button_click
        )
        btn.pack(pady=10)

        return self.frame

    def on_button_click(self):
        """Handle button click"""
        print("Button clicked!")
```

**Step 2: Create Function Module**

Create `functions/my_functions.py`:

```python
"""
My custom functions
"""

class MyFunctions:
    def __init__(self):
        pass

    def do_something(self):
        """Perform some operation"""
        print("Doing something...")
        return "Success"
```

**Step 3: Register in MainWindow**

Edit `gui/main_window.py`:

1. **Import your screen**:

```python
from gui.screens.my_new_screen import MyNewScreen
```

2. **Add navigation button** in `create_widgets()`:

```python
# After existing buttons
btn_my_screen = ModernButton(
    nav_buttons_frame,
    text="My Screen",
    command=lambda: self.show_screen("my_screen"),
    is_nav=True
)
btn_my_screen.pack(side=tk.LEFT, padx=(0, 8))
self.nav_buttons["my_screen"] = btn_my_screen
```

3. **Register screen** in `create_widgets()`:

```python
# After existing screens
self.screens["my_screen"] = MyNewScreen(content_area)
```

**Step 4: Test**

```bash
python main.py
```

Click "My Screen" button to see your new screen!

### 4. Adding a New Component

#### Example: Creating a Custom Label Component

Create `gui/components/custom_label.py`:

```python
"""
Custom styled label component
"""

import tkinter as tk
from constants.app_config import AppConfig

class CustomLabel:
    def __init__(self, parent, text, style="normal"):
        self.parent = parent
        self.text = text
        self.style = style
        self.label = self.create_label()

    def create_label(self):
        """Create the label widget"""
        if self.style == "title":
            font = (AppConfig.FONT_FAMILY, AppConfig.TITLE_FONT_SIZE, "bold")
            fg = AppConfig.ACCENT_COLOR
        elif self.style == "error":
            font = (AppConfig.FONT_FAMILY, AppConfig.FONT_SIZE)
            fg = "#f44336"  # Red
        else:
            font = (AppConfig.FONT_FAMILY, AppConfig.FONT_SIZE)
            fg = AppConfig.TEXT_COLOR

        label = tk.Label(
            self.parent,
            text=self.text,
            font=font,
            fg=fg,
            bg=AppConfig.PRIMARY_COLOR
        )
        return label

    def get_widget(self):
        """Return the label widget"""
        return self.label

    def set_text(self, text):
        """Update label text"""
        self.label.configure(text=text)
```

**Usage**:

```python
from gui.components.custom_label import CustomLabel

# Create title label
title = CustomLabel(parent, "My Title", style="title")
title.get_widget().pack(pady=10)

# Create error label
error = CustomLabel(parent, "Error occurred!", style="error")
error.get_widget().pack(pady=5)
```

### 5. Working with Drag-and-Drop

#### Using Existing DragDropWidget

```python
from gui.components.drag_drop import DragDropWidget

class MyScreen:
    def create_screen(self):
        # Create drag-drop widget
        self.drag_drop = DragDropWidget(
            self.frame,
            self.on_file_selected  # Callback function
        )
        widget = self.drag_drop.get_widget()
        widget.pack(fill=tk.BOTH, expand=True)

    def on_file_selected(self, filepath, filename, reset_all):
        """Handle file selection"""
        if reset_all:
            print("Reset button clicked")
            return

        print(f"File selected: {filename}")
        print(f"Full path: {filepath}")

        # Process the file
        self.process_file(filepath)
```

#### Creating Custom Drag-Drop Widget

```python
import tkinter as tk
from tkinterdnd2 import DND_FILES

class MyDragDrop:
    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback
        self.widget = self.create_widget()

    def create_widget(self):
        frame = tk.Frame(self.parent, bg="#ffffff")

        # Drop zone
        drop_zone = tk.Label(
            frame,
            text="Drop file here",
            bg="#f0f0f0",
            relief=tk.RAISED,
            bd=2
        )
        drop_zone.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Register drop target
        drop_zone.drop_target_register(DND_FILES)
        drop_zone.dnd_bind('<<Drop>>', self.on_drop)

        return frame

    def on_drop(self, event):
        filepath = event.data.strip('{}')
        filename = filepath.split('/')[-1]
        self.callback(filepath, filename)

    def get_widget(self):
        return self.widget
```

### 6. Adding Console Output

#### Using StatusPanel

```python
from gui.components.status_panel import StatusPanel

class MyScreen:
    def create_screen(self):
        # Create status panel
        self.status_panel = StatusPanel(self.frame)
        panel = self.status_panel.get_widget()
        panel.pack(fill=tk.BOTH, expand=True)

    def process_file(self, filepath):
        # Update file info
        filename = filepath.split('/')[-1]
        self.status_panel.update_file_info(filepath, filename, False)

        # Add log messages
        self.status_panel.add_log("Processing file...", "info")
        self.status_panel.add_log("✅ Success!", "success")
        self.status_panel.add_log("❌ Error occurred", "error")
```

#### Creating Custom Console

```python
from tkinter import scrolledtext

class MyConsole:
    def __init__(self, parent):
        self.parent = parent
        self.console = self.create_console()

    def create_console(self):
        console = scrolledtext.ScrolledText(
            self.parent,
            height=15,
            bg="#ffffff",
            fg="#333333",
            font=("Consolas", 9),
            state=tk.DISABLED,
            wrap=tk.WORD
        )
        return console

    def add_message(self, message, color="#333333"):
        self.console.configure(state=tk.NORMAL)
        self.console.insert(tk.END, f"{message}\n")
        self.console.see(tk.END)
        self.console.configure(state=tk.DISABLED)

    def clear(self):
        self.console.configure(state=tk.NORMAL)
        self.console.delete(1.0, tk.END)
        self.console.configure(state=tk.DISABLED)
```

### 7. Threading for Long Operations

#### Basic Threading Pattern

```python
import threading

class MyScreen:
    def run_long_operation(self):
        """Start a long-running operation"""
        # Disable buttons
        self.button.configure(state=tk.DISABLED)

        # Start worker thread
        thread = threading.Thread(
            target=self.worker_function,
            daemon=True
        )
        thread.start()

    def worker_function(self):
        """Runs in background thread"""
        # Do long operation
        for i in range(10):
            time.sleep(1)

            # Schedule GUI update (thread-safe)
            self.frame.after(
                0,
                lambda i=i: self.update_progress(i)
            )

        # Operation complete
        self.frame.after(0, self.operation_complete)

    def update_progress(self, step):
        """Update GUI (runs in main thread)"""
        self.status_panel.add_log(f"Step {step} complete", "info")

    def operation_complete(self):
        """Called when operation finishes"""
        self.status_panel.add_log("✅ All done!", "success")
        self.button.configure(state=tk.NORMAL)
```

#### Thread with Cancellation

```python
class MyScreen:
    def __init__(self, parent):
        self.parent = parent
        self.cancel_flag = False
        self.current_thread = None

    def start_operation(self):
        self.cancel_flag = False
        self.current_thread = threading.Thread(
            target=self.worker,
            daemon=True
        )
        self.current_thread.start()

    def worker(self):
        for i in range(100):
            if self.cancel_flag:
                self.frame.after(0, lambda: self.add_log("Cancelled"))
                return

            # Do work
            time.sleep(0.1)
            self.frame.after(0, lambda i=i: self.update(i))

    def cancel_operation(self):
        self.cancel_flag = True
```

### 8. Styling Guidelines

#### Using AppConfig

Always use AppConfig for styling:

```python
from constants.app_config import AppConfig

# Good
label = tk.Label(
    parent,
    bg=AppConfig.PRIMARY_COLOR,
    fg=AppConfig.TEXT_COLOR,
    font=(AppConfig.FONT_FAMILY, AppConfig.FONT_SIZE)
)

# Bad - hardcoded values
label = tk.Label(
    parent,
    bg="#f5f5f5",
    fg="#000000",
    font=("Segoe UI", 11)
)
```

#### Consistent Spacing

```python
# Padding guidelines
widget.pack(padx=15, pady=15)  # Standard padding
widget.pack(padx=10, pady=10)  # Compact padding
widget.pack(padx=20, pady=20)  # Generous padding
```

#### Color Usage

```python
# Primary background for main areas
frame.configure(bg=AppConfig.PRIMARY_COLOR)

# Secondary background for panels
panel.configure(bg=AppConfig.SECONDARY_COLOR)

# Accent color for highlights
label.configure(fg=AppConfig.ACCENT_COLOR)

# Text color for content
text.configure(fg=AppConfig.TEXT_COLOR)
```

### 9. Testing Your Changes

#### Manual Testing Checklist

- [ ] Application starts without errors
- [ ] All navigation buttons work
- [ ] Screen displays correctly
- [ ] Drag-and-drop functions properly
- [ ] Buttons respond to clicks
- [ ] Console output appears correctly
- [ ] Threading doesn't freeze GUI
- [ ] No error messages in console
- [ ] Window resizes properly (if applicable)
- [ ] Colors match theme

#### Testing Specific Features

**Test Drag-and-Drop**:

1. Drag a file onto the drop zone
2. Verify file path displays correctly
3. Verify filename displays correctly
4. Test reset button
5. Try dragging multiple files

**Test Console Output**:

1. Add various message types
2. Verify colors are correct
3. Check scrolling works
4. Test clearing console
5. Verify timestamps (if applicable)

**Test Threading**:

1. Start long operation
2. Verify GUI remains responsive
3. Test cancel button
4. Check console updates appear
5. Verify completion message

### 10. Debugging Tips

#### Print Debugging

```python
def on_file_selected(self, filepath, filename, reset_all):
    print(f"DEBUG: filepath={filepath}")
    print(f"DEBUG: filename={filename}")
    print(f"DEBUG: reset_all={reset_all}")

    # Your code here
```

#### Logging to Console

```python
import sys

def debug_log(message):
    print(f"[DEBUG] {message}", file=sys.stderr)

debug_log("Screen created")
debug_log(f"File selected: {filename}")
```

#### Try-Except for Error Handling

```python
def risky_operation(self):
    try:
        # Your code
        result = process_file(filepath)
        self.add_log("✅ Success!", "success")
    except FileNotFoundError:
        self.add_log("❌ File not found", "error")
    except Exception as e:
        self.add_log(f"❌ Error: {str(e)}", "error")
        import traceback
        traceback.print_exc()  # Print full error to console
```

#### GUI Debugging

```python
# Check if widget exists
if self.frame and self.frame.winfo_exists():
    print("Frame exists")
else:
    print("Frame destroyed or doesn't exist")

# Check widget dimensions
print(f"Width: {self.frame.winfo_width()}")
print(f"Height: {self.frame.winfo_height()}")

# Check parent
print(f"Parent: {self.frame.winfo_parent()}")
```

### 11. Common Pitfalls and Solutions

#### Pitfall: GUI Updates from Thread

**Wrong**:

```python
def worker():
    # This will crash!
    self.label.configure(text="Done")
```

**Correct**:

```python
def worker():
    # Schedule GUI update
    self.frame.after(0, lambda: self.label.configure(text="Done"))
```

#### Pitfall: Forgetting to Return Frame

**Wrong**:

```python
def create_screen(self):
    self.frame = ModernFrame(self.parent)
    # Forgot to return!
```

**Correct**:

```python
def create_screen(self):
    self.frame = ModernFrame(self.parent)
    return self.frame
```

#### Pitfall: Hardcoded Values

**Wrong**:

```python
label = tk.Label(parent, bg="#f5f5f5", font=("Segoe UI", 11))
```

**Correct**:

```python
label = tk.Label(
    parent,
    bg=AppConfig.PRIMARY_COLOR,
    font=(AppConfig.FONT_FAMILY, AppConfig.FONT_SIZE)
)
```

#### Pitfall: Not Checking File Selection

**Wrong**:

```python
def process_file(self):
    filepath = self.drag_drop.get_selected_filepath()
    # This might be None!
    with open(filepath, 'r') as f:
        content = f.read()
```

**Correct**:

```python
def process_file(self):
    filepath = self.drag_drop.get_selected_filepath()
    if not filepath:
        self.add_log("❌ No file selected", "error")
        return

    try:
        with open(filepath, 'r') as f:
            content = f.read()
    except Exception as e:
        self.add_log(f"❌ Error: {str(e)}", "error")
```

### 12. Code Organization Best Practices

#### File Organization

```
gui/screens/my_screen.py
    ↓
Imports at top
    ↓
Class definition
    ↓
__init__ method
    ↓
create_screen method
    ↓
Helper methods (alphabetically)
    ↓
Event handlers (on_* methods)
```

#### Method Naming Conventions

```python
# Public methods (called from outside)
def create_screen(self):
    pass

def update_file_info(self, filepath, filename):
    pass

# Event handlers
def on_file_selected(self, filepath, filename, reset_all):
    pass

def on_button_click(self):
    pass

# Private/helper methods (internal use)
def _validate_file(self, filepath):
    pass

def _update_display(self):
    pass
```

#### Documentation

```python
def my_function(self, param1, param2):
    """
    Brief description of what the function does.

    Args:
        param1 (str): Description of param1
        param2 (int): Description of param2

    Returns:
        bool: True if successful, False otherwise

    Example:
        result = self.my_function("test", 42)
    """
    # Implementation
    pass
```

### 13. Version Control Best Practices

#### Commit Messages

```bash
# Good commit messages
git commit -m "Add new utility screen for system diagnostics"
git commit -m "Fix drag-drop issue on macOS"
git commit -m "Update color scheme to match design"

# Bad commit messages
git commit -m "Update"
git commit -m "Fix bug"
git commit -m "Changes"
```

#### Branching Strategy

```bash
# Create feature branch
git checkout -b feature/new-screen

# Make changes and commit
git add .
git commit -m "Add new screen implementation"

# Push to remote
git push origin feature/new-screen

# Merge to main (after review)
git checkout main
git merge feature/new-screen
```

### 14. Performance Optimization

#### Lazy Loading

```python
class MyScreen:
    def __init__(self, parent):
        self.parent = parent
        self.frame = None
        self.heavy_component = None  # Don't create yet

    def create_screen(self):
        if self.frame:
            return self.frame  # Return cached frame

        self.frame = ModernFrame(self.parent)

        # Create heavy component only when needed
        if not self.heavy_component:
            self.heavy_component = HeavyComponent(self.frame)

        return self.frame
```

#### Image Optimization

```python
from PIL import Image

def optimize_image(self, image_path):
    """Optimize image for display"""
    img = Image.open(image_path)

    # Resize if too large
    max_size = (840, 380)
    img.thumbnail(max_size, Image.LANCZOS)

    # Convert to RGB if needed
    if img.mode != 'RGB':
        img = img.convert('RGB')

    return img
```

#### Widget Reuse

```python
# Good - reuse widgets
def show_tab(self, tab_id):
    self.current_tab.pack_forget()  # Hide
    self.tabs[tab_id].pack()        # Show

# Bad - recreate widgets
def show_tab(self, tab_id):
    self.current_tab.destroy()      # Destroy
    self.current_tab = self.create_tab(tab_id)  # Recreate
```

## Next Steps

1. **Read the code**: Start with simple files and work your way up
2. **Make small changes**: Test frequently
3. **Follow patterns**: Use existing code as examples
4. **Ask questions**: Comment your code with questions
5. **Document changes**: Keep README and docs updated
6. **Test thoroughly**: Manual testing is important
7. **Commit often**: Small, focused commits

## Resources

- **Python tkinter docs**: https://docs.python.org/3/library/tkinter.html
- **tkinterdnd2 docs**: https://github.com/pmgagne/tkinterdnd2
- **Pillow docs**: https://pillow.readthedocs.io/
- **Python threading**: https://docs.python.org/3/library/threading.html

## Getting Help

When stuck:

1. Check existing similar code in the project
2. Read the error message carefully
3. Print debug information
4. Test in isolation
5. Ask for help with specific error messages
