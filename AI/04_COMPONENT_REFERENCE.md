# Component Reference - BIOS Utility Toolkit

## Complete Component Documentation

This document provides detailed reference for all reusable components in the application.

---

## ModernButton

**Location**: `gui/components/modern_button.py`

### Purpose

Custom styled button with hover effects, active states, and tooltip support. Used for both navigation and action buttons.

### Constructor

```python
ModernButton(
    parent,              # Parent widget
    text,                # Button text
    command,             # Callback function
    is_nav=False,        # Navigation button mode
    tooltip=None,        # Tooltip text (optional)
    bg=None,             # Background color (optional)
    fg=None,             # Foreground color (optional)
    padx=None,           # Horizontal padding (optional)
    pady=None,           # Vertical padding (optional)
    width=None           # Button width (optional)
)
```

### Methods

#### `set_active(active: bool)`

Set button active/inactive state (for navigation buttons).

```python
button.set_active(True)   # Set as active
button.set_active(False)  # Set as inactive
```

#### `on_enter(event)` (Internal)

Handle mouse enter event (hover effect).

#### `on_leave(event)` (Internal)

Handle mouse leave event (remove hover).

### Usage Examples

**Navigation Button**:

```python
from gui.components.modern_button import ModernButton

nav_btn = ModernButton(
    parent_frame,
    text="Home",
    command=lambda: self.show_screen("home"),
    is_nav=True
)
nav_btn.pack(side=tk.LEFT, padx=(0, 8))

# Set as active
nav_btn.set_active(True)
```

**Action Button**:

```python
action_btn = ModernButton(
    parent_frame,
    text="Process File",
    command=self.process_file,
    tooltip="Click to process the selected file",
    bg="#4caf50",  # Green background
    fg="#ffffff",  # White text
    padx=20,
    pady=10,
    width=15
)
action_btn.pack(pady=10)
```

**Custom Styled Button**:

```python
custom_btn = ModernButton(
    parent_frame,
    text="Delete",
    command=self.delete_file,
    bg="#f44336",  # Red background
    fg="#ffffff",  # White text
    tooltip="Delete selected file"
)
custom_btn.pack()
```

### Styling

**Navigation Mode** (`is_nav=True`):

- Default: White background, black text
- Hover: Light gray background
- Active: Dark gray background, blue text

**Action Mode** (`is_nav=False`):

- Default: Uses provided colors or AppConfig defaults
- Hover: Slightly darker shade
- Active: Same as default

### Properties

- **Cursor**: Changes to 'hand2' on hover
- **Relief**: Flat (no 3D effect)
- **Border**: 1px solid border
- **Font**: Uses AppConfig.FONT_FAMILY and BUTTON_FONT_SIZE

---

## ModernFrame

**Location**: `gui/components/modern_frame.py`

### Purpose

Themed frame container with consistent styling across the application.

### Constructor

```python
ModernFrame(
    parent,              # Parent widget
    bg=None,             # Background color (optional)
    **kwargs             # Additional tk.Frame arguments
)
```

### Usage Examples

**Basic Frame**:

```python
from gui.components.modern_frame import ModernFrame

frame = ModernFrame(parent)
frame.pack(fill=tk.BOTH, expand=True)
```

**Custom Background**:

```python
frame = ModernFrame(parent, bg="#ffffff")
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
```

**Nested Frames**:

```python
outer_frame = ModernFrame(parent)
outer_frame.pack(fill=tk.BOTH, expand=True)

inner_frame = ModernFrame(outer_frame, bg=AppConfig.SECONDARY_COLOR)
inner_frame.pack(fill=tk.X, padx=15, pady=15)
```

### Properties

- **Default Background**: AppConfig.PRIMARY_COLOR
- **Relief**: Flat
- **Border**: None

---

## DragDropWidget

**Location**: `gui/components/drag_drop.py`

### Purpose

Single file drag-and-drop widget with visual feedback and file information display.

### Constructor

```python
DragDropWidget(
    parent,                      # Parent widget
    on_file_selected_callback    # Callback function
)
```

### Callback Signature

```python
def on_file_selected(filepath: str, filename: str, reset_all: bool):
    """
    Args:
        filepath: Full path to the selected file
        filename: Just the filename (without path)
        reset_all: True if reset button was clicked, False otherwise
    """
    pass
```

### Methods

#### `get_widget()`

Returns the widget for packing.

```python
widget = drag_drop.get_widget()
widget.pack(fill=tk.BOTH, expand=True)
```

#### `reset_file()`

Clear the current file selection.

```python
drag_drop.reset_file()
```

#### `get_selected_filepath()`

Get the currently selected file path.

```python
filepath = drag_drop.get_selected_filepath()
if filepath:
    print(f"Selected: {filepath}")
```

#### `on_drop(event)` (Internal)

Handle file drop event.

### Usage Examples

**Basic Usage**:

```python
from gui.components.drag_drop import DragDropWidget

class MyScreen:
    def create_screen(self):
        self.drag_drop = DragDropWidget(
            self.frame,
            self.on_file_selected
        )
        widget = self.drag_drop.get_widget()
        widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def on_file_selected(self, filepath, filename, reset_all):
        if reset_all:
            print("Reset clicked")
            return

        print(f"File: {filename}")
        print(f"Path: {filepath}")
        self.process_file(filepath)
```

**With Validation**:

```python
def on_file_selected(self, filepath, filename, reset_all):
    if reset_all:
        self.clear_data()
        return

    # Validate file extension
    if not filename.endswith('.bin'):
        self.show_error("Please select a .bin file")
        self.drag_drop.reset_file()
        return

    # Validate file size
    import os
    size = os.path.getsize(filepath)
    if size > 10 * 1024 * 1024:  # 10MB
        self.show_error("File too large (max 10MB)")
        self.drag_drop.reset_file()
        return

    # Process valid file
    self.process_file(filepath)
```

### Visual States

- **Empty**: Shows "Drag & Drop BIOS File Here" message
- **Hover**: Border highlights when dragging file over
- **Selected**: Shows filename and file path
- **Reset Button**: Appears when file is selected

---

## DMIDragDropWidget

**Location**: `gui/components/dmi_drag_drop.py`

### Purpose

Specialized drag-and-drop widget for DMI operations with source/target labeling.

### Constructor

```python
DMIDragDropWidget(
    parent,                  # Parent widget
    label_text,              # Label text ("Source File" or "Target File")
    on_file_selected         # Callback function
)
```

### Callback Signature

```python
def on_file_selected(filepath: str, filename: str):
    """
    Args:
        filepath: Full path to the selected file
        filename: Just the filename
    """
    pass
```

### Methods

#### `get_widget()`

Returns the widget for packing.

#### `reset_file()`

Clear the current file selection.

#### `get_selected_filepath()`

Get the currently selected file path.

### Usage Examples

**Source/Target Setup**:

```python
from gui.components.dmi_drag_drop import DMIDragDropWidget

# Source file
self.source_drag_drop = DMIDragDropWidget(
    left_container,
    label_text="Source File",
    on_file_selected=self.on_source_selected
)
source_widget = self.source_drag_drop.get_widget()
source_widget.pack(fill=tk.BOTH, expand=True)

# Target file
self.target_drag_drop = DMIDragDropWidget(
    right_container,
    label_text="Target File",
    on_file_selected=self.on_target_selected
)
target_widget = self.target_drag_drop.get_widget()
target_widget.pack(fill=tk.BOTH, expand=True)
```

**Processing Both Files**:

```python
def process_dmi_copy(self):
    source = self.source_drag_drop.get_selected_filepath()
    target = self.target_drag_drop.get_selected_filepath()

    if not source:
        self.show_error("No source file selected")
        return

    if not target:
        self.show_error("No target file selected")
        return

    # Process DMI copy
    self.copy_dmi(source, target)
```

---

## StatusPanel

**Location**: `gui/components/status_panel.py`

### Purpose

Comprehensive status display with file information, console output, and action buttons.

### Constructor

```python
StatusPanel(parent)
```

### Methods

#### `get_widget()`

Returns the widget for packing.

```python
panel = status_panel.get_widget()
panel.pack(fill=tk.BOTH, expand=True)
```

#### `update_file_info(filepath, filename, reset_all)`

Update the file information display.

```python
status_panel.update_file_info(
    "/path/to/file.bin",
    "file.bin",
    False
)
```

#### `add_log(message, msg_type="normal")`

Add a log message to the status area.

**Message Types**:

- `"normal"`: Standard text
- `"error"`: Red text with ❌
- `"success"`: Green text with ✅
- `"info"`: Blue text with ℹ️
- `"warning"`: Orange text with ⚠️

```python
status_panel.add_log("Processing file...", "info")
status_panel.add_log("✅ Success!", "success")
status_panel.add_log("❌ Error occurred", "error")
```

#### `start_command_mode()`

Switch to command output mode (clears status area).

```python
status_panel.start_command_mode()
```

#### `add_command_output(text)`

Add command output text (for command mode).

```python
status_panel.add_command_output("Launching analyzer...")
status_panel.add_command_output("Scanning firmware...")
```

#### `run_analysis()`

Run ME analysis operation (built-in).

#### `run_build()`

Run build operation (built-in).

#### `run_clean()`

Run clean operation (built-in).

#### `stop_all_tasks()`

Stop all running tasks.

```python
status_panel.stop_all_tasks()
```

### Usage Examples

**Basic Setup**:

```python
from gui.components.status_panel import StatusPanel

self.status_panel = StatusPanel(right_section)
panel = self.status_panel.get_widget()
panel.pack(fill=tk.BOTH, expand=True)
```

**File Selection Integration**:

```python
def on_file_selected(self, filepath, filename, reset_all):
    self.status_panel.update_file_info(filepath, filename, reset_all)

    if not reset_all:
        self.status_panel.add_log(f"File loaded: {filename}", "success")
```

**Operation Progress**:

```python
def process_file(self):
    self.status_panel.add_log("Starting process...", "info")

    try:
        # Do work
        result = self.do_work()
        self.status_panel.add_log("✅ Process complete!", "success")
    except Exception as e:
        self.status_panel.add_log(f"❌ Error: {str(e)}", "error")
```

### Built-in Action Buttons

- **MEA**: Run ME analysis
- **BUILD**: Run build process
- **CLEAN**: Run clean process
- **STOP**: Stop all operations

---

## UnlockConsole

**Location**: `gui/components/unlock_console.py`

### Purpose

Console interface for unlock operations with file info and operation buttons.

### Constructor

```python
UnlockConsole(parent)
```

### Methods

#### `get_widget()`

Returns the widget for packing.

#### `update_file_info(filepath, filename, reset_all)`

Update file information display.

#### `add_console_message(message, msg_type="normal")`

Add message to console.

**Message Types**: Same as StatusPanel

#### `run_unlock_operation()`

Execute unlock operation (built-in).

### Usage Examples

**Basic Setup**:

```python
from gui.components.unlock_console import UnlockConsole

self.unlock_console = UnlockConsole(right_section)
console = self.unlock_console.get_widget()
console.pack(fill=tk.BOTH, expand=True)
```

**Integration**:

```python
def on_file_selected(self, filepath, filename, reset_all):
    self.unlock_console.update_file_info(filepath, filename, reset_all)
```

---

## UtilityConsole

**Location**: `gui/components/utility_console.py`

### Purpose

Console interface for utility operations.

### Constructor

```python
UtilityConsole(parent)
```

### Methods

Same as UnlockConsole:

- `get_widget()`
- `update_file_info(filepath, filename, reset_all)`
- `add_console_message(message, msg_type)`
- `run_utility_operation()`

### Usage Examples

Similar to UnlockConsole - see above.

---

## Slideshow

**Location**: `gui/components/slideshow.py`

### Purpose

Image carousel with auto-advance and manual navigation.

### Constructor

```python
Slideshow(parent)
```

### Methods

#### `get_frame()`

Returns the slideshow frame for packing.

```python
slideshow_frame = slideshow.get_frame()
slideshow_frame.pack(fill=tk.BOTH, expand=True)
```

#### `load_images()`

Load images from assets/images/ directory (called automatically).

#### `show_image(index)`

Display specific image by index.

```python
slideshow.show_image(0)  # Show first image
```

#### `next_image()`

Navigate to next image.

```python
slideshow.next_image()
```

#### `previous_image()`

Navigate to previous image.

```python
slideshow.previous_image()
```

#### `start_auto_slideshow()`

Start automatic slideshow (called automatically).

#### `stop_auto_slideshow()`

Stop automatic slideshow.

```python
slideshow.stop_auto_slideshow()
```

#### `get_current_info()`

Get current slide information.

```python
info = slideshow.get_current_info()  # Returns "Slide 1 of 5"
```

### Usage Examples

**Basic Setup**:

```python
from gui.components.slideshow import Slideshow

self.slideshow = Slideshow(slideshow_container)
frame = self.slideshow.get_frame()
frame.pack(fill=tk.BOTH, expand=True)
```

**With Navigation Buttons**:

```python
# Create slideshow
self.slideshow = Slideshow(container)
frame = self.slideshow.get_frame()
frame.pack(fill=tk.BOTH, expand=True)

# Left button
left_btn = tk.Button(
    container,
    text="◀",
    command=self.slideshow.previous_image
)
left_btn.place(x=20, rely=0.5, anchor=tk.W)

# Right button
right_btn = tk.Button(
    container,
    text="▶",
    command=self.slideshow.next_image
)
right_btn.place(x=-20, rely=0.5, anchor=tk.E, relx=1.0)
```

**With Counter Display**:

```python
# Create counter label
self.counter_label = tk.Label(footer, text="")
self.counter_label.pack()

# Update counter
def update_counter(self):
    info = self.slideshow.get_current_info()
    self.counter_label.configure(text=info)

# Schedule periodic updates
def schedule_updates(self):
    self.update_counter()
    self.frame.after(100, self.schedule_updates)
```

### Image Requirements

- **Location**: `assets/images/`
- **Format**: PNG
- **Naming**: `slide_1.png`, `slide_2.png`, etc.
- **Recommended Size**: 840x380 pixels
- **Color Mode**: RGB or RGBA

### Configuration

Edit `constants/app_config.py`:

```python
SLIDESHOW_INTERVAL = 2500      # Auto-advance interval (ms)
SLIDESHOW_WIDTH = 840          # Width in pixels
SLIDESHOW_HEIGHT = 380         # Height in pixels
SLIDESHOW_BORDER_RADIUS = 16   # Corner radius
```

---

## Component Comparison Table

| Component         | Purpose             | File Selection | Console Output | Action Buttons |
| ----------------- | ------------------- | -------------- | -------------- | -------------- |
| ModernButton      | Styled button       | ❌             | ❌             | N/A            |
| ModernFrame       | Container           | ❌             | ❌             | ❌             |
| DragDropWidget    | Single file drop    | ✅             | ❌             | ❌             |
| DMIDragDropWidget | Labeled file drop   | ✅             | ❌             | ❌             |
| StatusPanel       | Full status display | ❌             | ✅             | ✅             |
| UnlockConsole     | Unlock operations   | ❌             | ✅             | ✅             |
| UtilityConsole    | Utility operations  | ❌             | ✅             | ✅             |
| Slideshow         | Image carousel      | ❌             | ❌             | ❌             |

---

## Creating Custom Components

### Template

```python
"""
My custom component
"""

import tkinter as tk
from constants.app_config import AppConfig

class MyComponent:
    def __init__(self, parent, **kwargs):
        """
        Initialize component.

        Args:
            parent: Parent widget
            **kwargs: Additional arguments
        """
        self.parent = parent
        self.widget = self.create_widget()

    def create_widget(self):
        """Create and return the main widget"""
        # Create your widget here
        frame = tk.Frame(
            self.parent,
            bg=AppConfig.PRIMARY_COLOR
        )

        # Add child widgets
        label = tk.Label(
            frame,
            text="My Component",
            font=(AppConfig.FONT_FAMILY, AppConfig.FONT_SIZE),
            bg=AppConfig.PRIMARY_COLOR,
            fg=AppConfig.TEXT_COLOR
        )
        label.pack(pady=10)

        return frame

    def get_widget(self):
        """Return the widget for packing"""
        return self.widget

    # Add your custom methods here
    def do_something(self):
        """Perform some action"""
        pass
```

### Best Practices

1. **Always provide `get_widget()` method**
2. **Use AppConfig for all styling**
3. **Document constructor parameters**
4. **Provide clear method names**
5. **Handle errors gracefully**
6. **Support common operations (reset, clear, etc.)**
7. **Use callbacks for events**
8. **Keep components focused and single-purpose**

---

## Component Integration Patterns

### Pattern 1: Drag-Drop + Console

```python
# Left: Drag-drop
self.drag_drop = DragDropWidget(left_section, self.on_file_selected)
drag_widget = self.drag_drop.get_widget()
drag_widget.pack(fill=tk.BOTH, expand=True)

# Right: Console
self.console = UnlockConsole(right_section)
console_widget = self.console.get_widget()
console_widget.pack(fill=tk.BOTH, expand=True)

# Integration
def on_file_selected(self, filepath, filename, reset_all):
    self.console.update_file_info(filepath, filename, reset_all)
```

### Pattern 2: Dual Drag-Drop

```python
# Source
self.source = DMIDragDropWidget(left, "Source", self.on_source)
self.source.get_widget().pack(fill=tk.BOTH, expand=True)

# Target
self.target = DMIDragDropWidget(right, "Target", self.on_target)
self.target.get_widget().pack(fill=tk.BOTH, expand=True)

# Process both
def process(self):
    source = self.source.get_selected_filepath()
    target = self.target.get_selected_filepath()
    if source and target:
        self.do_work(source, target)
```

### Pattern 3: Slideshow + Navigation

```python
# Slideshow
self.slideshow = Slideshow(container)
self.slideshow.get_frame().pack(fill=tk.BOTH, expand=True)

# Navigation
left_btn = ModernButton(container, "◀", self.slideshow.previous_image)
right_btn = ModernButton(container, "▶", self.slideshow.next_image)

# Counter
self.counter = tk.Label(footer, text="")
self.update_counter()

def update_counter(self):
    self.counter.configure(text=self.slideshow.get_current_info())
    self.frame.after(100, self.update_counter)
```

---

## Troubleshooting Components

### Issue: Component not displaying

**Check**:

1. Did you call `get_widget()` or `get_frame()`?
2. Did you pack/grid/place the widget?
3. Is the parent widget visible?
4. Are dimensions set correctly?

### Issue: Drag-drop not working

**Check**:

1. Is tkinterdnd2 installed?
2. Is parent using `tkdnd.Tk()` instead of `tk.Tk()`?
3. Are file paths being parsed correctly?
4. Is the drop zone registered?

### Issue: Console not updating

**Check**:

1. Are you calling `add_log()` or `add_console_message()`?
2. Is the console in DISABLED state?
3. Are you using `frame.after()` for thread-safe updates?
4. Is the widget still alive?

### Issue: Buttons not responding

**Check**:

1. Is the command parameter set?
2. Is the button enabled (state=tk.NORMAL)?
3. Is the button visible?
4. Are there overlapping widgets?
