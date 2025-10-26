# Architecture Details - BIOS Utility Toolkit

## Directory Structure Deep Dive

### Root Level Files

#### `main.py`

- **Purpose**: Application entry point
- **Responsibilities**:
  - Import MainWindow class
  - Initialize application
  - Start main event loop
- **Code Pattern**:

```python
from gui.main_window import MainWindow

def main():
    app = MainWindow()
    app.run()
```

#### `requirements.txt`

- **Purpose**: Python package dependencies
- **Contents**:
  - pillow>=9.0.0 (Image handling)
  - tkinterdnd2>=0.3.0 (Drag-drop)
  - ttkthemes>=3.2.0 (Themes, optional)

### Constants Directory (`constants/`)

#### `app_config.py`

- **Purpose**: Centralized configuration management
- **Contains**:
  - Window dimensions (840x520)
  - Color scheme (light theme)
  - Font settings (Segoe UI)
  - Slideshow settings (2500ms interval)

**Key Configuration Class**:

```python
class AppConfig:
    # Window settings
    WINDOW_WIDTH = 840
    WINDOW_HEIGHT = 520
    WINDOW_TITLE = "Python GUI Application"

    # Colors
    PRIMARY_COLOR = "#f5f5f5"
    ACCENT_COLOR = "#0078d4"
    TEXT_COLOR = "#000000"

    # Fonts
    FONT_FAMILY = "Segoe UI"
    FONT_SIZE = 11

    # Slideshow
    SLIDESHOW_INTERVAL = 2500
```

**Usage Pattern**: Import and reference constants

```python
from constants.app_config import AppConfig
window.configure(bg=AppConfig.PRIMARY_COLOR)
```

### Functions Directory (`functions/`)

Business logic layer - completely independent of GUI.

#### `app_functions.py`

- **Purpose**: Core application utilities
- **Methods**:
  - `show_hello_world()`: Display message dialog
  - `show_custom_message(title, message)`: Custom dialogs
  - `show_error(message)`: Error dialogs
  - `show_warning(message)`: Warning dialogs
  - `ask_yes_no(title, question)`: Yes/No dialogs

#### `me_clean_functions.py`

- **Purpose**: Management Engine cleaning operations
- **Methods**:
  - `start_me_clean()`: Initiate ME cleaning
  - `check_me_status()`: Check ME status
  - `backup_me_region()`: Backup ME region
- **Note**: Currently placeholder implementations

#### `hp_dmi_functions.py`

- **Purpose**: DMI data operations
- **Methods**:
  - `read_dmi_info()`: Read DMI data
  - `write_dmi_data()`: Write DMI data
  - `backup_dmi()`: Backup DMI information
- **Note**: Currently placeholder implementations

#### `unlock_functions.py`

- **Purpose**: BIOS unlock operations
- **Methods**:
  - `start_unlock()`: Start unlock process
  - `check_lock_status()`: Check lock status
  - `bypass_security()`: Security bypass
- **Note**: Currently placeholder implementations

#### `utility_functions.py`

- **Purpose**: System utility operations
- **Methods**:
  - `show_system_info()`: Display system information
  - `check_disk_space()`: Check disk space
  - `run_diagnostics()`: Run diagnostics
- **Note**: Partially implemented with system info

### GUI Directory (`gui/`)

#### `main_window.py`

- **Purpose**: Main application window and navigation controller
- **Key Components**:

**Class Structure**:

```python
class MainWindow:
    def __init__(self):
        self.root = tkdnd.Tk()  # Main window with drag-drop
        self.functions = AppFunctions()
        self.current_screen = None
        self.active_button = None
        self.setup_window()
        self.create_widgets()
        self.show_screen("home")
```

**Key Methods**:

- `setup_window()`: Configure window properties
- `create_widgets()`: Create navigation and screens
- `show_screen(screen_id)`: Switch between screens
- `run()`: Start main event loop

**Navigation System**:

- Creates navigation buttons for each screen
- Manages active button state
- Handles screen switching with instant transitions
- Uses pack_forget() for hiding screens

**Screen Management**:

```python
self.screens = {
    "home": HomeScreen(content_area),
    "me_clean": MECleanScreen(content_area),
    "hp_dmi": HPDMIScreen(content_area),
    "unlock": UnlockScreen(content_area),
    "utility": UtilityScreen(content_area)
}
```

### GUI Components Directory (`gui/components/`)

Reusable UI widgets following component-based design.

#### `modern_button.py`

- **Purpose**: Custom styled button with hover effects
- **Features**:
  - Navigation mode (is_nav=True)
  - Active/inactive states
  - Hover effects
  - Tooltip support
  - Custom colors and padding

**Key Methods**:

```python
class ModernButton:
    def __init__(self, parent, text, command, is_nav=False, tooltip=None, **kwargs)
    def set_active(self, active)  # Set active state
    def on_enter(self, event)     # Hover enter
    def on_leave(self, event)     # Hover leave
```

#### `modern_frame.py`

- **Purpose**: Themed frame container
- **Features**:
  - Consistent styling
  - Inherits from tk.Frame
  - Uses AppConfig colors

#### `drag_drop.py`

- **Purpose**: Single file drag-and-drop widget
- **Features**:
  - Visual drop zone
  - File path display
  - Filename display
  - Reset functionality
  - Callback on file selection

**Key Methods**:

```python
class DragDropWidget:
    def __init__(self, parent, on_file_selected_callback)
    def on_drop(self, event)           # Handle file drop
    def reset_file(self)               # Clear selection
    def get_selected_filepath(self)    # Get current file
```

**Callback Signature**:

```python
def on_file_selected(filepath, filename, reset_all=False):
    # filepath: Full path to file
    # filename: Just the filename
    # reset_all: True if reset button clicked
```

#### `dmi_drag_drop.py`

- **Purpose**: DMI-specific drag-and-drop widget
- **Differences from drag_drop.py**:
  - Customized for source/target file selection
  - Different visual styling
  - Label text parameter

**Key Methods**:

```python
class DMIDragDropWidget:
    def __init__(self, parent, label_text, on_file_selected)
    def on_drop(self, event)
    def reset_file(self)
    def get_selected_filepath(self)
```

#### `status_panel.py`

- **Purpose**: Status display with console output and action buttons
- **Features**:
  - File information display
  - Console output area
  - Action buttons (MEA, BUILD, CLEAN, STOP)
  - Thread-safe console updates
  - Task cancellation support

**Key Methods**:

```python
class StatusPanel:
    def __init__(self, parent)
    def update_file_info(self, filepath, filename, reset_all)
    def add_log(self, message, msg_type)
    def start_command_mode(self)
    def add_command_output(self, text)
    def run_analysis(self)
    def run_build(self)
    def run_clean(self)
    def stop_all_tasks(self)
```

**Console Message Types**:

- `"normal"`: Standard text
- `"error"`: Red text with ❌
- `"success"`: Green text with ✅
- `"info"`: Blue text with ℹ️
- `"warning"`: Orange text with ⚠️

#### `unlock_console.py`

- **Purpose**: Console for unlock operations
- **Features**:
  - File info display
  - Operation buttons
  - Real-time console output
  - Thread-safe updates

**Key Methods**:

```python
class UnlockConsole:
    def __init__(self, parent)
    def update_file_info(self, filepath, filename, reset_all)
    def add_console_message(self, message, msg_type)
    def run_unlock_operation(self)
```

#### `utility_console.py`

- **Purpose**: Console for utility operations
- **Features**:
  - Similar to unlock_console
  - Utility-specific operations
  - System diagnostics display

**Key Methods**:

```python
class UtilityConsole:
    def __init__(self, parent)
    def update_file_info(self, filepath, filename, reset_all)
    def add_console_message(self, message, msg_type)
    def run_utility_operation(self)
```

#### `slideshow.py`

- **Purpose**: Image carousel component
- **Features**:
  - Auto-advance (2.5 seconds)
  - Manual navigation
  - Image loading from assets/images/
  - Slide counter
  - Rounded corners

**Key Methods**:

```python
class Slideshow:
    def __init__(self, parent)
    def load_images(self)
    def show_image(self, index)
    def next_image(self)
    def previous_image(self)
    def start_auto_slideshow(self)
    def stop_auto_slideshow(self)
    def get_current_info(self)  # Returns "Slide X of Y"
```

**Image Requirements**:

- Location: `assets/images/`
- Format: PNG
- Naming: `slide_1.png`, `slide_2.png`, etc.
- Recommended size: 840x380 pixels

#### `tab_widget.py`

- **Purpose**: Tab navigation widget
- **Note**: May not be actively used (ME Clean uses inline tabs)

### GUI Screens Directory (`gui/screens/`)

#### `home_screen.py`

- **Purpose**: Welcome screen with slideshow
- **Layout**:
  - Full-screen slideshow area
  - Left/right navigation buttons (absolute positioning)
  - Black footer with slide counter and credits
  - Spacer at bottom

**Key Features**:

- Auto-slideshow with 2.5s interval
- Manual navigation buttons
- Slide counter updates
- Credits: "💜 Made with love by Samnickgammer 🚀"

**Key Methods**:

```python
class HomeScreen:
    def create_screen(self)
    def previous_slide(self)
    def next_slide(self)
    def update_counter(self)
    def schedule_counter_update(self)
```

#### `me_clean_screen.py`

- **Purpose**: ME cleaning operations with three modes
- **Layout**:
  - Tab navigation (Auto/FITC/Manual)
  - Separator line
  - Content area (changes per tab)

**Auto Tab**:

- Left: Drag-drop widget (300px width)
- Right: Status panel (expandable)

**FITC Tab**:

- Left: Drag-drop widget
- Right: "Coming Soon" panel

**Manual Tab**:

- Placeholder content

**Key Methods**:

```python
class MECleanScreen:
    def create_screen(self)
    def create_tab_navigation(self)
    def initialize_tab_screens(self)
    def create_auto_screen(self)
    def create_fitc_screen(self)
    def create_manual_screen(self)
    def show_tab(self, tab_id)
    def on_file_selected(self, filepath, filename, reset_all)
```

**Tab Switching**:

- Instant switching (no recreation)
- All tabs pre-initialized
- Active button highlighting
- pack_forget() for hiding

#### `hp_dmi_screen.py`

- **Purpose**: DMI copy operations
- **Layout**:
  - Top: Source and Target drag-drop (side by side)
  - Bottom Left: Operations panel with buttons
  - Bottom Right: Status console (350px width)

**Key Features**:

- Dual file selection
- DMI Copy button
- Clear button
- Real-time console output
- Threaded operations

**Key Methods**:

```python
class HPDMIScreen:
    def create_screen(self)
    def on_source_selected(self, filepath, filename)
    def on_target_selected(self, filepath, filename)
    def add_console_message(self, message, msg_type)
    def dmi_copy(self)
    def clear_all(self)
```

#### `unlock_screen.py`

- **Purpose**: BIOS unlock operations
- **Layout**:
  - Left: Drag-drop widget (700px width)
  - Right: Unlock console (expandable)

**Key Methods**:

```python
class UnlockScreen:
    def create_screen(self)
    def on_file_selected(self, filepath, filename, reset_all)
```

#### `utility_screen.py`

- **Purpose**: System utility operations
- **Layout**:
  - Left: Drag-drop widget (700px width)
  - Right: Utility console (expandable)

**Key Methods**:

```python
class UtilityScreen:
    def create_screen(self)
    def on_file_selected(self, filepath, filename, reset_all)
```

### Assets Directory (`assets/`)

#### `assets/images/`

- **Purpose**: Store slideshow images
- **Contents**:
  - slide_1.png through slide_5.png
  - placeholder.py (empty file)

**Image Specifications**:

- Format: PNG
- Recommended dimensions: 840x380
- Color mode: RGB or RGBA
- File size: Optimized for quick loading

## Data Flow Patterns

### File Selection Flow

```
User drags file
    ↓
tkinterdnd2 captures drop event
    ↓
DragDropWidget.on_drop(event)
    ↓
Extract filepath from event
    ↓
Update widget display
    ↓
Call callback: on_file_selected(filepath, filename, False)
    ↓
Screen handles file selection
    ↓
Update console/status panel
```

### Screen Switching Flow

```
User clicks navigation button
    ↓
Button command: lambda: self.show_screen("screen_id")
    ↓
MainWindow.show_screen(screen_id)
    ↓
Hide current screen: current_screen.pack_forget()
    ↓
Reset all button states: btn.set_active(False)
    ↓
Show new screen: screens[screen_id].create_screen()
    ↓
Set active button: nav_buttons[screen_id].set_active(True)
    ↓
Force update: root.update_idletasks()
```

### Operation Execution Flow

```
User clicks action button (e.g., "MEA")
    ↓
Validate file selection
    ↓
Clear console / Start command mode
    ↓
Add initial log message
    ↓
Create worker thread
    ↓
Thread executes operation
    ↓
Thread schedules GUI updates: frame.after(delay, callback)
    ↓
GUI updates console output
    ↓
Operation completes
    ↓
Show success/error message
```

## Threading Architecture

### Main Thread Responsibilities

- GUI rendering and updates
- Event handling (clicks, drops)
- Window management
- Timer callbacks

### Worker Thread Responsibilities

- File processing
- Long-running operations
- Simulated command execution
- Data analysis

### Thread Safety Mechanisms

- **Never** update GUI directly from worker thread
- Use `frame.after(delay, callback)` to schedule GUI updates
- Pass data through closures or shared variables
- Use daemon threads for background tasks

**Example Pattern**:

```python
def run_operation(self):
    def worker():
        # Do work in background
        result = process_file()

        # Schedule GUI update
        self.frame.after(0, lambda: self.update_gui(result))

    thread = threading.Thread(target=worker, daemon=True)
    thread.start()
```

## State Management

### Application State

- Current screen ID
- Active navigation button
- Screen instances (cached)

### Screen State

- Selected file path
- Selected filename
- Current tab (for ME Clean)
- Active tab button

### Component State

- Button active/inactive
- Console content
- File selection status
- Operation running status

## Error Handling Patterns

### File Selection Errors

```python
if not filepath:
    self.add_log("❌ Error: No file selected!", "error")
    return
```

### Operation Errors

```python
try:
    result = perform_operation()
except Exception as e:
    self.add_log(f"❌ Error: {str(e)}", "error")
```

### GUI Update Errors

- Wrapped in try-except blocks
- Graceful degradation
- User-friendly error messages

## Performance Considerations

### Lazy Loading

- Screens created on first access
- Images loaded once and cached
- Components initialized when needed

### Efficient Rendering

- Use pack_forget() instead of destroy()
- Minimize widget recreation
- Batch GUI updates

### Memory Management

- Daemon threads for cleanup
- Image caching
- Widget reuse

## Extension Points

### Adding New Screens

1. Create screen class in `gui/screens/`
2. Implement `create_screen()` method
3. Add navigation button in `main_window.py`
4. Register screen in `self.screens` dict

### Adding New Components

1. Create component class in `gui/components/`
2. Implement `__init__()` and `get_widget()` methods
3. Use AppConfig for styling
4. Document callback signatures

### Adding New Functions

1. Create function class in `functions/`
2. Implement business logic methods
3. Keep GUI-independent
4. Add error handling

### Modifying Configuration

1. Edit `constants/app_config.py`
2. Add new constants to AppConfig class
3. Use throughout application
4. Document purpose and usage
