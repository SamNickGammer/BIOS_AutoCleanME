# Developer Quick Start Guide

## 🚀 Get Running in 5 Minutes

### Step 1: Prerequisites Check

```bash
# Check Python version (need 3.7+)
python --version

# If not installed, download from python.org
```

### Step 2: Clone and Setup

```bash
# Navigate to project directory
cd bios-utility-toolkit

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python main.py
```

**That's it!** The application should launch with the home screen.

---

## 📖 Understanding the Codebase

### Quick Tour (5 minutes)

1. **Entry Point**: `main.py`

   - Simple entry point that launches the GUI

2. **Main Window**: `gui/main_window.py`

   - Creates the window
   - Sets up navigation
   - Manages screens

3. **Configuration**: `constants/app_config.py`

   - All colors, sizes, fonts
   - Change settings here

4. **Screens**: `gui/screens/`

   - Each screen is a separate file
   - Look at `home_screen.py` for a simple example

5. **Components**: `gui/components/`

   - Reusable UI elements
   - Look at `modern_button.py` for an example

6. **Functions**: `functions/`
   - Business logic separate from UI
   - Currently placeholder implementations

---

## 🎯 Your First Task: Add a Simple Screen

### Task: Create a "About" Screen

**Time**: 10 minutes

**Step 1**: Create the screen file

```bash
# Create new file
touch gui/screens/about_screen.py
```

**Step 2**: Add this code to `gui/screens/about_screen.py`:

```python
"""
About screen implementation
"""

import tkinter as tk
from constants.app_config import AppConfig
from gui.components.modern_frame import ModernFrame

class AboutScreen:
    def __init__(self, parent):
        self.parent = parent
        self.frame = None

    def create_screen(self):
        """Create the about screen"""
        if self.frame:
            return self.frame

        self.frame = ModernFrame(self.parent)

        # Title
        title = tk.Label(
            self.frame,
            text="About BIOS Utility Toolkit",
            font=(AppConfig.FONT_FAMILY, 18, "bold"),
            bg=AppConfig.PRIMARY_COLOR,
            fg=AppConfig.TEXT_COLOR
        )
        title.pack(pady=30)

        # Version info
        version = tk.Label(
            self.frame,
            text="Version 1.0.0",
            font=(AppConfig.FONT_FAMILY, 12),
            bg=AppConfig.PRIMARY_COLOR,
            fg=AppConfig.TEXT_COLOR
        )
        version.pack(pady=10)

        # Description
        description = tk.Label(
            self.frame,
            text="A comprehensive BIOS management toolkit\nfor ME cleaning, DMI operations, and more.",
            font=(AppConfig.FONT_FAMILY, 11),
            bg=AppConfig.PRIMARY_COLOR,
            fg=AppConfig.TEXT_COLOR,
            justify=tk.CENTER
        )
        description.pack(pady=20)

        # Credits
        credits = tk.Label(
            self.frame,
            text="Made with 💜 by Samnickgammer 🚀",
            font=(AppConfig.FONT_FAMILY, 11),
            bg=AppConfig.PRIMARY_COLOR,
            fg=AppConfig.ACCENT_COLOR
        )
        credits.pack(pady=30)

        return self.frame
```

**Step 3**: Register the screen in `gui/main_window.py`

Add import at the top:

```python
from gui.screens.about_screen import AboutScreen
```

In the `create_widgets()` method, add navigation button (after other buttons):

```python
# About button
btn = ModernButton(
    nav_buttons_frame,
    text="About",
    command=lambda: self.show_screen("about"),
    is_nav=True
)
btn.pack(side=tk.LEFT, padx=(0, 8))
self.nav_buttons["about"] = btn
```

Register the screen (after other screens):

```python
self.screens["about"] = AboutScreen(content_area)
```

**Step 4**: Test it!

```bash
python main.py
```

Click the "About" button - you should see your new screen!

**Congratulations!** 🎉 You just added a new screen to the application.

---

## 🔧 Common Development Tasks

### Change Window Size

Edit `constants/app_config.py`:

```python
WINDOW_WIDTH = 1024  # Change from 840
WINDOW_HEIGHT = 768  # Change from 520
```

### Change Colors

Edit `constants/app_config.py`:

```python
PRIMARY_COLOR = "#ffffff"  # White background
ACCENT_COLOR = "#ff5722"   # Orange accent
```

### Add a Button to a Screen

```python
from gui.components.modern_button import ModernButton

# In your screen's create_screen method:
btn = ModernButton(
    self.frame,
    text="Click Me",
    command=self.on_button_click
)
btn.pack(pady=10)

def on_button_click(self):
    print("Button clicked!")
```

### Add Console Output

```python
# In a screen with console (like ME Clean):
self.status_panel.add_log("My message", "info")

# Message types: "info", "error", "success", "normal"
```

### Run Operation in Thread

```python
import threading

def run_operation(self):
    def worker():
        # Long operation here
        result = do_something()

        # Update UI on main thread
        self.frame.after(0, lambda: self.show_result(result))

    thread = threading.Thread(target=worker, daemon=True)
    thread.start()
```

---

## 📚 Next Steps

### Learn More

1. **Read the AI Instructions**: Check `AI_INSTRUCTIONS/00_START_HERE.md`
2. **Study Existing Screens**: Look at `gui/screens/me_clean_screen.py`
3. **Understand Components**: Check `gui/components/drag_drop.py`

### Try These Tasks

1. ✅ Add a new screen (you just did this!)
2. ⬜ Add a button to your screen
3. ⬜ Create a custom component
4. ⬜ Implement a function in `functions/`
5. ⬜ Add drag-and-drop to your screen

### Explore the Code

- **Simple Screen**: `gui/screens/home_screen.py`
- **Complex Screen**: `gui/screens/me_clean_screen.py`
- **Simple Component**: `gui/components/modern_button.py`
- **Complex Component**: `gui/components/status_panel.py`

---

## 🐛 Troubleshooting

### Application won't start

```bash
# Check Python version
python --version  # Should be 3.7+

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Import errors

```bash
# Make sure virtual environment is activated
# You should see (venv) in your terminal prompt

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### tkinter not found (Linux)

```bash
sudo apt-get install python3-tk
```

### Drag-and-drop not working

- Make sure you're using `tkinterdnd2.Tk` not `tk.Tk`
- Check that tkinterdnd2 is installed: `pip list | grep tkinterdnd2`

---

## 💡 Tips

1. **Use AppConfig**: Never hardcode colors or sizes
2. **Follow Patterns**: Look at existing code for examples
3. **Test Often**: Run the app after each change
4. **Read Docs**: Check `AI_INSTRUCTIONS/` folder
5. **Ask Questions**: Create issues or ask the team

---

## 🎓 Learning Resources

### In This Repository

- `README.md` - Project overview and setup
- `AI_INSTRUCTIONS/` - Comprehensive documentation
- `gui/screens/` - Screen examples
- `gui/components/` - Component examples

### External Resources

- [Python tkinter docs](https://docs.python.org/3/library/tkinter.html)
- [tkinterdnd2 docs](https://github.com/pmgagne/tkinterdnd2)
- [PEP 8 Style Guide](https://pep8.org/)

---

## 🤝 Getting Help

### Documentation

1. Check `AI_INSTRUCTIONS/00_START_HERE.md`
2. Look for similar code in existing files
3. Read the relevant guide in `AI_INSTRUCTIONS/`

### Community

1. Create an issue on GitHub
2. Ask the development team
3. Check existing issues for solutions

---

## ✅ Checklist for New Developers

- [ ] Python 3.7+ installed
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] Application runs successfully
- [ ] Read `README.md`
- [ ] Read `AI_INSTRUCTIONS/00_START_HERE.md`
- [ ] Completed "Your First Task"
- [ ] Explored existing screens
- [ ] Understand the architecture
- [ ] Ready to contribute!

---

**Welcome to the team! Happy coding! 🚀**

**Made with 💜 by Samnickgammer**
