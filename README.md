# ANSI Codes

A Python module to handle ANSI escape codes for terminal control, providing features for cursor movement, text formatting, and color manipulation.

## Features

- Move the cursor to specific positions or manipulate its location.
- Change text appearance (bold, italic, underline, etc.).
- Apply 16, 256, and true color (24-bit) to text and backgrounds.
- Clear parts of the terminal (lines, screen, etc.).

## Installation

You can install the package using pip:

```bash
pip install ansi_codes
```

# Usage
```py
from ansi_codes import Cursor, Color, Font, Erase

Cursor.home()
Erase.all()
Color.c16('brightred')
Font.bold()
print("Hello, World!")

Color.reset()

```

### Cursor

The `Cursor` class moves the terminal cursor around:
```py
Cursor.moveRight(10)
Cursor.moveDown(5)
```

### Font
The `Font` class formats terminal text:
```py
Font.underline()
print("This text is underlined.")
Font.underline(False)
```

### Color
The `Color` class sets colors in the terminal:
```py
Color.c16('green')       # 16-color
Color.c256(82)           # 256-color
Color.c24bit(255, 0, 0)  # TrueColor (24-bit)
```

### Erase
The `Erase` class clears parts of the terminal:
```py
Erase.all()            
Erase.currentLine()    
```

## Contributions
Contributions are welcome!
