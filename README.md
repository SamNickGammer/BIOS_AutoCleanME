# BIOS Utility Toolkit

A comprehensive Python GUI application for BIOS management, ME cleaning, DMI operations, and system utilities. Built with tkinter featuring a modern, modular architecture with drag-and-drop functionality.

## 🚀 Features

### Core Modules

- **Home Screen**: Interactive slideshow with navigation
- **ME Clean**: Management Engine cleaning with Auto/FITC/Manual modes
- **HP DMI**: DMI data copy operations between source and target BIOS files
- **Unlock**: BIOS unlock operations with real-time console output
- **Utility**: System diagnostics and utility tools

### Technical Features

- Modern light-themed UI with custom components
- Drag-and-drop file handling (tkinterdnd2)
- Multi-tab navigation with instant switching
- Real-time console output and status panels
- Thread-safe operations for long-running tasks
- Modular architecture for easy expansion

## 📁 Project Structure

```
.
├── main.py                          # Application entry point
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
│
├── constants/                       # Configuration constants
│   ├── __init__.py
│   └── app_config.py               # App settings, colors, fonts, sizes
│
├── functions/                       # Business logic layer
│   ├── __init__.py
│   ├── app_functions.py            # Core application functions
│   ├── me_clean_functions.py       # ME cleaning operations
│   ├── hp_dmi_functions.py         # DMI operations
│   ├── unlock_functions.py         # Unlock operations
│   └── utility_functions.py        # System utility functions
│
├── gui/                            # GUI layer
│   ├── __init__.py
│   ├── main_window.py              # Main window and navigation
│   │
│   ├── components/                 # Reusable UI components
│   │   ├── __init__.py
│   │   ├── modern_button.py        # Custom button widget
│   │   ├── modern_frame.py         # Custom frame widget
│   │   ├── drag_drop.py            # Single file drag-drop widget
│   │   ├── dmi_drag_drop.py        # DMI-specific drag-drop widget
│   │   ├── status_panel.py         # Status display with console
│   │   ├── unlock_console.py       # Unlock operations console
│   │   ├── utility_console.py      # Utility operations console
│   │   ├── slideshow.py            # Image slideshow component
│   │   └── tab_widget.py           # Tab navigation widget
│   │
│   └── screens/                    # Application screens
│       ├── __init__.py
│       ├── home_screen.py          # Home/welcome screen
│       ├── me_clean_screen.py      # ME Clean operations
│       ├── hp_dmi_screen.py        # HP DMI operations
│       ├── unlock_screen.py        # Unlock operations
│       └── utility_screen.py       # Utility tools
│
├── assets/                         # Static assets
│   └── images/                     # Slideshow images
│       ├── slide_1.png
│       ├── slide_2.png
│       ├── slide_3.png
│       ├── slide_4.png
│       └── slide_5.png
│
└── AI/                             # AI Assistant Documentation
    ├── README.md                   # Documentation overview
    ├── 01_PROJECT_OVERVIEW.md      # High-level project understanding
    ├── 02_ARCHITECTURE_DETAILS.md  # Deep technical details
    ├── 03_DEVELOPMENT_GUIDE.md     # Practical development guide
    ├── 04_COMPONENT_REFERENCE.md   # Complete component documentation
    ├── 05_IMPLEMENTATION_TASKS.md  # Roadmap and future work
    └── 06_QUICK_START_FOR_AI.md    # Quick reference for AI assistants
```

## 🛠️ Setup and Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Operating System: Windows, macOS, or Linux

### Installation Steps

1. **Clone or download the project**

   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Install required dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   Required packages:

   - `pillow>=9.0.0` - Image handling for slideshow
   - `tkinterdnd2>=0.3.0` - Drag and drop functionality
   - `ttkthemes>=3.2.0` - Enhanced themes (optional)

3. **Verify installation**

   ```bash
   python --version  # Should be 3.7+
   pip list | grep -E "pillow|tkinterdnd2"
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

### Troubleshooting Installation

**Issue: tkinterdnd2 not working**

- On Windows: Ensure you have Visual C++ redistributables installed
- On macOS: May need to install tkinter separately: `brew install python-tk`
- On Linux: Install tkinter: `sudo apt-get install python3-tk`

**Issue: Images not loading**

- Verify that `assets/images/` directory contains PNG files
- Check file permissions

## 🎯 Usage Guide

### Home Screen

- Automatic slideshow with 2.5-second intervals
- Manual navigation using left/right arrow buttons
- Slide counter display in footer

### ME Clean Screen

Three operational modes:

- **Auto**: Automated ME cleaning process
- **FITC**: FITC-based cleaning (Coming Soon)
- **Manual**: Advanced manual operations

**Workflow:**

1. Select desired mode (Auto/FITC/Manual)
2. Drag and drop BIOS file into the designated area
3. Monitor operations in the status panel
4. Use action buttons (MEA, BUILD, CLEAN, STOP)

### HP DMI Screen

Copy DMI data between BIOS files:

1. Drag source BIOS file to "Source File" area
2. Drag target BIOS file to "Target File" area
3. Click "DMI Copy" to transfer DMI data
4. Monitor progress in status console
5. Use "Clear" to reset selections

### Unlock Screen

BIOS unlock operations:

1. Drag BIOS file into drop zone
2. Select unlock operation from console
3. Monitor real-time output
4. Use STOP button to cancel operations

### Utility Screen

System utilities and diagnostics:

1. Drag BIOS file if required
2. Select utility operation
3. View results in console panel

## ⚙️ Configuration

### Window Settings

Edit `constants/app_config.py`:

```python
WINDOW_WIDTH = 840
WINDOW_HEIGHT = 520
WINDOW_TITLE = "Your Custom Title"
```

### Theme Customization

Modify colors in `constants/app_config.py`:

```python
PRIMARY_COLOR = "#f5f5f5"      # Background
ACCENT_COLOR = "#0078d4"        # Accent color
TEXT_COLOR = "#000000"          # Text color
BUTTON_COLOR = "#ffffff"        # Button background
```

### Slideshow Settings

```python
SLIDESHOW_INTERVAL = 2500       # Auto-change interval (ms)
SLIDESHOW_WIDTH = 840           # Slideshow width
SLIDESHOW_HEIGHT = 380          # Slideshow height
```

## 🔧 Development Guide

### Adding New Screens

1. **Create screen file** in `gui/screens/`:

   ```python
   # gui/screens/my_new_screen.py
   from gui.components.modern_frame import ModernFrame

   class MyNewScreen:
       def __init__(self, parent):
           self.parent = parent
           self.frame = None

       def create_screen(self):
           self.frame = ModernFrame(self.parent)
           # Add your widgets here
           return self.frame
   ```

2. **Add navigation button** in `gui/main_window.py`:

   ```python
   # In create_widgets method
   btn = ModernButton(
       nav_buttons_frame,
       text="My Screen",
       command=lambda: self.show_screen("my_screen"),
       is_nav=True
   )
   ```

3. **Register screen** in `gui/main_window.py`:

   ```python
   from gui.screens.my_new_screen import MyNewScreen

   # In create_widgets method
   self.screens["my_screen"] = MyNewScreen(content_area)
   ```

### Adding New Functions

1. **Create function module** in `functions/`:

   ```python
   # functions/my_functions.py
   class MyFunctions:
       def __init__(self):
           pass

       def my_operation(self):
           # Your logic here
           pass
   ```

2. **Import and use** in your screen:

   ```python
   from functions.my_functions import MyFunctions

   class MyScreen:
       def __init__(self, parent):
           self.functions = MyFunctions()
   ```

### Creating Custom Components

1. **Create component file** in `gui/components/`:

   ```python
   # gui/components/my_widget.py
   import tkinter as tk
   from constants.app_config import AppConfig

   class MyWidget:
       def __init__(self, parent):
           self.parent = parent
           self.widget = self.create_widget()

       def create_widget(self):
           # Create and return your widget
           pass

       def get_widget(self):
           return self.widget
   ```

## 🏗️ Architecture

### Design Patterns

- **MVC Pattern**: Separation of GUI, business logic, and configuration
- **Component-Based**: Reusable UI components
- **Factory Pattern**: Screen creation and management
- **Observer Pattern**: Event-driven file selection and operations

### Threading Model

- Main thread: GUI operations and rendering
- Worker threads: Long-running operations (file processing, analysis)
- Thread-safe console updates using `after()` method

### File Handling

- Drag-and-drop support via tkinterdnd2
- File validation and error handling
- Path normalization for cross-platform compatibility

## 📚 Documentation

### For Developers

Comprehensive documentation is available in the `AI/` folder:

- **AI/README.md** - Documentation overview and navigation guide
- **AI/01_PROJECT_OVERVIEW.md** - High-level project understanding
- **AI/02_ARCHITECTURE_DETAILS.md** - Deep dive into code structure
- **AI/03_DEVELOPMENT_GUIDE.md** - Step-by-step development tutorials
- **AI/04_COMPONENT_REFERENCE.md** - Complete component API reference
- **AI/05_IMPLEMENTATION_TASKS.md** - Roadmap and implementation tasks
- **AI/06_QUICK_START_FOR_AI.md** - Quick reference for AI assistants

### For AI Assistants

If you're an AI assistant helping with this codebase:

1. Start with `AI/06_QUICK_START_FOR_AI.md` for quick reference
2. Read `AI/01_PROJECT_OVERVIEW.md` for project context
3. Reference other documents as needed for specific tasks

The documentation is specifically designed to help AI assistants understand the codebase structure, patterns, and best practices.

## 📝 Code Style Guidelines

- Follow PEP 8 style guide
- Use docstrings for all classes and methods
- Keep functions focused and single-purpose
- Use meaningful variable names
- Comment complex logic
- Maintain consistent indentation (4 spaces)

## 🐛 Known Issues

1. **FITC Mode**: Currently shows "Coming Soon" placeholder
2. **Manual Mode**: Placeholder implementation
3. **Thread Cancellation**: Some operations may not cancel immediately

## 🔮 Future Enhancements

- [ ] Implement FITC ME cleaning functionality
- [ ] Add manual ME cleaning operations
- [ ] Implement actual BIOS file parsing
- [ ] Add file format validation
- [ ] Create backup/restore functionality
- [ ] Add logging system
- [ ] Implement settings persistence
- [ ] Add dark theme option
- [ ] Create installer/executable

## 📄 License

[Specify your license here]

## 👤 Author

**Samnickgammer**

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📞 Support

For support and questions, please create an issue or contact the development team.

---

**Made with 💜 by Samnickgammer 🚀**
