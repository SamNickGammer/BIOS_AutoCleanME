# Quick Start Guide for AI Assistants

## Purpose

This document is specifically designed for AI assistants (like ChatGPT, Claude, etc.) to quickly understand and work with this codebase. It provides a condensed overview and common tasks.

---

## Project Summary

**Name**: BIOS Utility Toolkit  
**Type**: Python GUI Application (tkinter)  
**Purpose**: BIOS management, ME cleaning, DMI operations, unlock, utilities  
**Architecture**: MVC pattern with component-based GUI  
**Python Version**: 3.7+  
**Main Dependencies**: tkinter, pillow, tkinterdnd2

---

## Quick File Reference

### Entry Point

- `main.py` - Start here, creates MainWindow and runs app

### Configuration

- `constants/app_config.py` - ALL settings (colors, sizes, fonts)

### Business Logic (GUI-independent)

- `functions/app_functions.py` - Core utilities
- `functions/me_clean_functions.py` - ME operations (placeholder)
- `functions/hp_dmi_functions.py` - DMI operations (placeholder)
- `functions/unlock_functions.py` - Unlock operations (placeholder)
- `functions/utility_functions.py` - System utilities (partial)

### GUI Framework

- `gui/main_window.py` - Main window, navigation, screen management

### Screens (Main Views)

- `gui/screens/home_screen.py` - Slideshow welcome screen
- `gui/screens/me_clean_screen.py` - ME cleaning (Auto/FITC/Manual tabs)
- `gui/screens/hp_dmi_screen.py` - DMI copy (source/target)
- `gui/screens/unlock_screen.py` - BIOS unlock
- `gui/screens/utility_screen.py` - System utilities

### Components (Reusable Widgets)

- `gui/components/modern_button.py` - Styled button
- `gui/components/modern_frame.py` - Themed frame
- `gui/components/drag_drop.py` - Single file drag-drop
- `gui/components/dmi_drag_drop.py` - Labeled drag-drop
- `gui/components/status_panel.py` - Status + console + buttons
- `gui/components/unlock_console.py` - Unlock console
- `gui/components/utility_console.py` - Utility console
- `gui/components/slideshow.py` - Image carousel

### Assets

- `assets/images/` - Slideshow images (slide_1.png to slide_5.png)

---

## Key Concepts

### 1. Screen Pattern

All screens follow this pattern:

```python
class MyScreen:
    def __init__(self, parent):
        self.parent = parent
        self.frame = None

    def create_screen(self):
        if self.frame:
            return self.frame  # Cache for fast switching

        self.frame = ModernFrame(self.parent)
        # Build UI here
        return self.frame
```

### 2. Component Pattern

All components follow this pattern:

```python
class MyComponent:
    def __init__(self, parent, callback=None):
        self.parent = parent
        self.widget = self.create_widget()

    def create_widget(self):
        # Build widget
        return widget

    def get_widget(self):
        return self.widget
```

### 3. Drag-Drop Callback

```python
def on_file_selected(filepath, filename, reset_all):
    # filepath: full path
    # filename: just filename
    # reset_all: True if reset button clicked
    pass
```

### 4. Threading Pattern

```python
def start_operation(self):
    def worker():
        # Do work in background
        result = do_work()
        # Schedule GUI update (thread-safe)
        self.frame.after(0, lambda: self.update_gui(result))

    thread = threading.Thread(target=worker, daemon=True)
    thread.start()
```

### 5. Console Output

```python
# Message types: "normal", "error", "success", "info", "warning"
status_panel.add_log("Processing...", "info")
status_panel.add_log("✅ Success!", "success")
status_panel.add_log("❌ Error!", "error")
```

---

## Common Tasks for AI

### Task 1: Add a New Screen

1. **Create screen file**: `gui/screens/my_screen.py`

```python
from gui.components.modern_frame import ModernFrame
from constants.app_config import AppConfig
import tkinter as tk

class MyScreen:
    def __init__(self, parent):
        self.parent = parent
        self.frame = None

    def create_screen(self):
        if self.frame:
            return self.frame

        self.frame = ModernFrame(self.parent)

        label = tk.Label(
            self.frame,
            text="My New Screen",
            font=(AppConfig.FONT_FAMILY, 16, "bold"),
            bg=AppConfig.PRIMARY_COLOR,
            fg=AppConfig.TEXT_COLOR
        )
        label.pack(pady=20)

        return self.frame
```

2. **Register in main_window.py**:

```python
# Add import
from gui.screens.my_screen import MyScreen

# In create_widgets(), add button:
btn = ModernButton(
    nav_buttons_frame,
    text="My Screen",
    command=lambda: self.show_screen("my_screen"),
    is_nav=True
)
btn.pack(side=tk.LEFT, padx=(0, 8))
self.nav_buttons["my_screen"] = btn

# Register screen:
self.screens["my_screen"] = MyScreen(content_area)
```

### Task 2: Add Drag-Drop to Screen

```python
from gui.components.drag_drop import DragDropWidget

class MyScreen:
    def create_screen(self):
        self.frame = ModernFrame(self.parent)

        # Create drag-drop
        self.drag_drop = DragDropWidget(self.frame, self.on_file_selected)
        widget = self.drag_drop.get_widget()
        widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        return self.frame

    def on_file_selected(self, filepath, filename, reset_all):
        if reset_all:
            print("Reset clicked")
            return

        print(f"File: {filename}")
        print(f"Path: {filepath}")
```

### Task 3: Add Console Output

```python
from gui.components.status_panel import StatusPanel

class MyScreen:
    def create_screen(self):
        self.frame = ModernFrame(self.parent)

        # Create status panel
        self.status_panel = StatusPanel(self.frame)
        panel = self.status_panel.get_widget()
        panel.pack(fill=tk.BOTH, expand=True)

        return self.frame

    def process_file(self, filepath):
        self.status_panel.add_log("Starting...", "info")
        # Do work
        self.status_panel.add_log("✅ Done!", "success")
```

### Task 4: Add Custom Button

```python
from gui.components.modern_button import ModernButton

btn = ModernButton(
    parent_frame,
    text="Click Me",
    command=self.on_click,
    tooltip="This is a tooltip",
    bg="#4caf50",  # Green
    fg="#ffffff",  # White
    padx=20,
    pady=10,
    width=15
)
btn.pack(pady=10)
```

### Task 5: Add Configuration Value

1. **Edit** `constants/app_config.py`:

```python
class AppConfig:
    # ... existing config ...

    # Add new value
    MY_NEW_COLOR = "#ff5722"
    MY_NEW_SIZE = 100
```

2. **Use** in code:

```python
from constants.app_config import AppConfig

widget.configure(bg=AppConfig.MY_NEW_COLOR)
```

### Task 6: Add Business Logic Function

1. **Create or edit** function file in `functions/`:

```python
# functions/my_functions.py
class MyFunctions:
    def __init__(self):
        pass

    def do_something(self, param):
        """Do something useful"""
        # Your logic here
        return result
```

2. **Use** in screen:

```python
from functions.my_functions import MyFunctions

class MyScreen:
    def __init__(self, parent):
        self.parent = parent
        self.functions = MyFunctions()

    def process(self):
        result = self.functions.do_something("test")
```

### Task 7: Add Threading Operation

```python
import threading
import time

class MyScreen:
    def start_long_operation(self):
        # Disable button
        self.button.configure(state=tk.DISABLED)

        # Start thread
        thread = threading.Thread(target=self.worker, daemon=True)
        thread.start()

    def worker(self):
        """Runs in background"""
        for i in range(10):
            time.sleep(1)
            # Update GUI (thread-safe)
            self.frame.after(0, lambda i=i: self.update_progress(i))

        # Done
        self.frame.after(0, self.operation_complete)

    def update_progress(self, step):
        """Runs in main thread"""
        self.status_panel.add_log(f"Step {step}", "info")

    def operation_complete(self):
        """Runs in main thread"""
        self.status_panel.add_log("✅ Done!", "success")
        self.button.configure(state=tk.NORMAL)
```

---

## Important Rules for AI

### DO:

✅ Always use `AppConfig` for colors, fonts, sizes  
✅ Return frame from `create_screen()`  
✅ Use `frame.after()` for GUI updates from threads  
✅ Check if file is selected before processing  
✅ Handle exceptions with try-except  
✅ Use meaningful variable names  
✅ Add docstrings to functions  
✅ Follow existing code patterns  
✅ Cache screens (check `if self.frame`)  
✅ Use `ModernFrame` and `ModernButton` components

### DON'T:

❌ Hardcode colors, fonts, or sizes  
❌ Update GUI directly from worker threads  
❌ Forget to return frame from `create_screen()`  
❌ Assume file is selected without checking  
❌ Let exceptions crash the app  
❌ Use single-letter variable names  
❌ Leave functions undocumented  
❌ Recreate widgets unnecessarily  
❌ Use `tk.Frame` directly (use `ModernFrame`)  
❌ Use `tk.Button` directly (use `ModernButton`)

---

## Code Style Guidelines

### Imports

```python
# Standard library
import tkinter as tk
from tkinter import messagebox
import threading
import time

# Local imports
from constants.app_config import AppConfig
from gui.components.modern_frame import ModernFrame
from gui.components.modern_button import ModernButton
from functions.my_functions import MyFunctions
```

### Class Structure

```python
class MyClass:
    """Class description"""

    def __init__(self, parent):
        """Initialize"""
        self.parent = parent
        self.frame = None

    def create_screen(self):
        """Create the screen"""
        pass

    def helper_method(self):
        """Helper method"""
        pass

    def on_event(self):
        """Event handler"""
        pass
```

### Naming Conventions

- Classes: `PascalCase` (e.g., `MyScreen`, `StatusPanel`)
- Functions/Methods: `snake_case` (e.g., `create_screen`, `on_file_selected`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `PRIMARY_COLOR`, `WINDOW_WIDTH`)
- Private methods: `_snake_case` (e.g., `_validate_file`)

### Docstrings

```python
def my_function(param1, param2):
    """
    Brief description.

    Args:
        param1 (str): Description
        param2 (int): Description

    Returns:
        bool: Description
    """
    pass
```

---

## Current Implementation Status

### ✅ Fully Working

- Application framework
- Navigation system
- All screen layouts
- All components
- Drag-and-drop
- Console output
- Threading infrastructure
- Slideshow

### ⏳ Placeholder (Needs Implementation)

- ME analysis (simulated)
- ME cleaning (simulated)
- FITC mode (shows "Coming Soon")
- Manual mode (placeholder)
- DMI copy (simulated)
- Unlock operations (simulated)
- Most utility operations (simulated)

### 🔨 Priority Tasks

1. BIOS file parsing
2. ME analysis implementation
3. ME cleaning implementation
4. DMI copy implementation
5. Unlock implementation
6. File validation
7. Logging system
8. Settings persistence

---

## Testing Checklist

When making changes, verify:

- [ ] App starts without errors
- [ ] Navigation works
- [ ] Screen displays correctly
- [ ] Drag-drop works
- [ ] Buttons respond
- [ ] Console output appears
- [ ] Threading doesn't freeze GUI
- [ ] No console errors
- [ ] Styling is consistent

---

## Common Errors and Solutions

### Error: "AttributeError: 'NoneType' object has no attribute 'pack'"

**Cause**: Forgot to return frame from `create_screen()`  
**Fix**: Add `return self.frame` at end of `create_screen()`

### Error: GUI freezes during operation

**Cause**: Long operation running in main thread  
**Fix**: Use threading pattern (see Task 7 above)

### Error: "RuntimeError: main thread is not in main loop"

**Cause**: Updating GUI from worker thread  
**Fix**: Use `self.frame.after(0, callback)` for GUI updates

### Error: File not found

**Cause**: File path not validated  
**Fix**: Check `if filepath:` before using

### Error: Widget not displaying

**Cause**: Forgot to pack/grid/place widget  
**Fix**: Add `.pack()`, `.grid()`, or `.place()` call

---

## Quick Reference: AppConfig Values

```python
# Window
WINDOW_WIDTH = 840
WINDOW_HEIGHT = 520
WINDOW_TITLE = "Python GUI Application"

# Colors
PRIMARY_COLOR = "#f5f5f5"        # Light gray background
SECONDARY_COLOR = "#e8e8e8"      # Darker gray
ACCENT_COLOR = "#0078d4"         # Blue accent
ACCENT_HOVER = "#106ebe"         # Darker blue
TEXT_COLOR = "#000000"           # Black text
BUTTON_COLOR = "#ffffff"         # White buttons
BUTTON_HOVER_COLOR = "#f0f0f0"   # Light gray hover
BUTTON_ACTIVE_COLOR = "#333333"  # Dark gray active
BUTTON_ACTIVE_TEXT = "#0000FF"   # Blue text active
BORDER_COLOR = "#d0d0d0"         # Light border

# Fonts
FONT_FAMILY = "Segoe UI"
FONT_SIZE = 11
BUTTON_FONT_SIZE = 9
TITLE_FONT_SIZE = 14

# Slideshow
SLIDESHOW_INTERVAL = 2500        # 2.5 seconds
SLIDESHOW_WIDTH = 840
SLIDESHOW_HEIGHT = 380
SLIDESHOW_BORDER_RADIUS = 16
```

---

## Quick Reference: Component Usage

### ModernButton

```python
btn = ModernButton(parent, text="Click", command=callback, is_nav=False)
btn.pack()
btn.set_active(True)  # For nav buttons
```

### ModernFrame

```python
frame = ModernFrame(parent, bg=AppConfig.PRIMARY_COLOR)
frame.pack(fill=tk.BOTH, expand=True)
```

### DragDropWidget

```python
drag_drop = DragDropWidget(parent, callback)
drag_drop.get_widget().pack()
filepath = drag_drop.get_selected_filepath()
drag_drop.reset_file()
```

### StatusPanel

```python
panel = StatusPanel(parent)
panel.get_widget().pack()
panel.update_file_info(path, name, False)
panel.add_log("Message", "info")
panel.stop_all_tasks()
```

### Slideshow

```python
slideshow = Slideshow(parent)
slideshow.get_frame().pack()
slideshow.next_image()
slideshow.previous_image()
info = slideshow.get_current_info()
```

---

## File Structure Quick Map

```
main.py                          → Entry point
constants/app_config.py          → All configuration
functions/*.py                   → Business logic
gui/main_window.py               → Navigation & screens
gui/screens/*.py                 → Main views
gui/components/*.py              → Reusable widgets
assets/images/*.png              → Slideshow images
```

---

## When User Asks To...

### "Add a new feature"

1. Determine if it's a new screen or component
2. Create appropriate file in `gui/screens/` or `gui/components/`
3. Follow existing patterns
4. Register in `main_window.py` if screen
5. Test thoroughly

### "Fix a bug"

1. Identify the file with the issue
2. Check for common errors (see above)
3. Add error handling if missing
4. Test the fix
5. Verify no side effects

### "Change styling"

1. Update `constants/app_config.py`
2. Use new values in code
3. Test visual appearance
4. Ensure consistency

### "Implement placeholder"

1. Check `05_IMPLEMENTATION_TASKS.md` for requirements
2. Create/update function file
3. Integrate with GUI
4. Add error handling
5. Test thoroughly

### "Optimize performance"

1. Identify bottleneck
2. Apply appropriate optimization (caching, threading, etc.)
3. Measure improvement
4. Ensure no functionality loss

---

## Resources

- **Full Documentation**: See other AI/\*.md files
- **Python tkinter**: https://docs.python.org/3/library/tkinter.html
- **Threading**: https://docs.python.org/3/library/threading.html
- **Pillow**: https://pillow.readthedocs.io/

---

## Final Tips for AI

1. **Read existing code first** - Understand patterns before changing
2. **Follow conventions** - Match existing code style
3. **Test incrementally** - Small changes, frequent testing
4. **Handle errors** - Always add try-except blocks
5. **Document changes** - Add comments and docstrings
6. **Ask for clarification** - If requirements unclear
7. **Provide examples** - Show how to use new code
8. **Consider edge cases** - What if file is missing? Too large?
9. **Think about UX** - Clear messages, good feedback
10. **Keep it simple** - Don't over-engineer

---

**Remember**: This is a well-structured codebase with clear patterns. Follow existing examples and you'll do great! 🚀
