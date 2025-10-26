# Python GUI Application

A clean, organized Python GUI application using tkinter with modular structure.

## Project Structure

```
├── main.py              # Entry point
├── gui/                 # GUI components
│   ├── __init__.py
│   └── main_window.py   # Main window implementation
├── functions/           # Business logic and functions
│   ├── __init__.py
│   └── app_functions.py # Application functions
├── constants/           # Configuration and constants
│   ├── __init__.py
│   └── app_config.py    # App settings, colors, sizes
├── requirements.txt     # Dependencies
└── README.md           # This file
```

## Features

- Clean separation of GUI, functions, and constants
- Configurable window size (840x520)
- Dark theme with customizable colors
- Hello World button example
- Modular design for easy expansion

## Setup and Installation

1. Make sure you have Python 3.6+ installed
2. Clone or download this project
3. Run the application:

```bash
python main.py
```

## Customization

- **Window settings**: Edit `constants/app_config.py`
- **Colors and theme**: Modify color constants in `app_config.py`
- **Add new functions**: Add methods to `functions/app_functions.py`
- **GUI modifications**: Edit `gui/main_window.py`

## Adding New Features

1. Add business logic to `functions/app_functions.py`
2. Add GUI elements in `gui/main_window.py`
3. Configure constants in `constants/app_config.py`
