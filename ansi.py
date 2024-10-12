# ANSI Codes by Gallium-Gonzollium
# Reference: https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#screen-modes

print_enabled = True

def prn(*args, **kwargs):
    """ 
    Helper function that prints code / returns it as a string based on the global print_enabled flag.
    """
    output = ''.join(map(str, args))
    
    if print_enabled:
        kwargs.setdefault('end', '')
        print(output, **kwargs)
    
    return output

def enablePrint():
    """
    Enables printing using prn(). Functions will return the output.
    """
    global print_enabled
    print_enabled = True

def disablePrint():
    """
    Disables printing using prn(). Functions will just return the output instead of printing.
    """
    global print_enabled
    print_enabled = False

def ansi(*args, start='[', end='m'):
    """
    Constructs an ANSI escape sequence based on the given parameters, prints it, and returns the resulting string.
    
    Args:
        *args: The ANSI code numbers.
        start (str): Starting character for the sequence (default is '[').
        end (str): Ending character for the sequence (default is 'm').
        
    Returns:
        str: The ANSI escape sequence.
    """
    output = f"\033{start}{';'.join(map(str, args))}{end}"
    prn(output)
    return output

@staticmethod
def reset(): ansi(0)

class Cursor: # ANSI cursor movement, determines where to draw the next text character
    """
    Provides methods for moving the terminal cursor to specific locations or adjusting its position.
    """
    @staticmethod
    def home():                     return prn('\033[H')
    @staticmethod
    def position(row: int, column: int, new=False):
        prn(f"\033[{row};{column}{'f'if new else'H'}")
    @staticmethod
    def column(column: int):        return ansi(column,  end='G')
    
    @staticmethod
    def moveUp   (rows=1):          return ansi(rows,    end='A')
    @staticmethod
    def moveDown (rows=1):          return ansi(rows,    end='B')
    @staticmethod
    def moveRight(columns=1):       return ansi(columns, end='C')
    @staticmethod
    def moveLeft (columns=1):       return ansi(columns, end='D')
    
    @staticmethod
    def startDown(rows=1):          return ansi(rows,    end='E')
    @staticmethod
    def startUp  (rows=1):          return ansi(rows,    end='F')
    
    @staticmethod
    def requestPosition():          return ansi(end='6n')
    @staticmethod
    def savePosition(alt=False):    return prn(f"\033{'[s'if alt else'7'}")
    @staticmethod
    def restorePosition(alt=False): return prn(f"\033{'[u'if alt else'8'}")
    
    @staticmethod
    def scrollUp():                 return prn(f'\033M')
    
    @staticmethod
    def hide():                     return ansi(end='?25l')
    @staticmethod
    def show():                     return ansi(end='?25h')

class Erase:
    """
    Provides methods for clearing different parts of the terminal lines and the screen.
    """
    @staticmethod
    def toEndOfPage(alt=False):     return ansi(end=(''if alt else'0')+'J')
    @staticmethod
    def toStartOfPage():            return ansi(end='1J')
    @staticmethod
    def all():                      return ansi(end='2J')
    @staticmethod
    def savedLines():               return ansi(end='3J')
    @staticmethod
    def toEndOfLine(alt=False):     return ansi(end=(''if alt else'0')+'K')
    @staticmethod
    def toStartOfLine():            return ansi(end='1K')
    @staticmethod
    def currentLine():              return ansi(end='2K')

class Color:
    """
    Provides methods for applying ANSI colors to text and backgrounds.
    """
    @staticmethod
    def c16(colorName: str, bg=False):
        colors = {
            'black':         30,
            'red':           31,
            'green':         32,
            'yellow':        33, 
            'blue':          34,
            'magenta':       35,
            'cyan':          36,
            'white':         37,
            'brightblack':   90,
            'brightred':     91,
            'brightgreen':   92,
            'brightyellow':  93,
            'brightblue':    94,
            'brightmagenta': 95,
            'brightcyan':    96,
            'brightwhite':   97
        }
        colorCode = colors.get(colorName.lower())
        if not colorCode:
            raise ValueError(f"Invalid color name: '{colorName}'")
        return ansi(colorCode + (10 if bg else 0))


    @staticmethod
    def default(bg=False):        return ansi(49 if bg else 39)
    
    @staticmethod
    def c256(id: int, bg=False):
        if not (0 <= id <= 255):
            raise ValueError(f"Invalid 256-color code: {id}")
        return ansi(48 if bg else 38, 5, id)

    @staticmethod
    def c24bit(red: int, green: int, blue: int, bg=False):
        if 0 <= red <= 255  and  0 <= green <= 255  and  0 <= blue <= 255:
            return ansi(48 if bg else 38, 2, red, green, blue)
        else: raise ValueError(f"Color R={red} G={green} B={blue} not in range: 0 <= color <= 255")

class Font:
    """
    Provides methods for changing text appearance using ANSI formatting.
    """
    @staticmethod
    def bold(on=True):            return ansi(1  if on else 22)
    @staticmethod
    def dim(on=True):             return ansi(2  if on else 22)
    @staticmethod
    def italic(on=True):          return ansi(3  if on else 23)
    @staticmethod
    def underline(on=True):       return ansi(4  if on else 24)
    @staticmethod
    def doubleUnderline(on=True): return ansi(21 if on else 24)  # Not very supported!
    @staticmethod
    def blink(on=True):           return ansi(5  if on else 25)
    @staticmethod
    def reverse(on=True):         return ansi(7  if on else 27)
    @staticmethod
    def hidden(on=True):          return ansi(8  if on else 28)
    @staticmethod
    def strikethrough(on=True):   return ansi(9  if on else 29)

class Screen:
    """
    Provides methods to control the terminal's screen buffer and modes.
    """
    @staticmethod
    def save():                   return ansi(end='?47h')
    @staticmethod
    def restore():                return ansi(end='?47l')
    
    @staticmethod
    def enableAltBuffer():        return ansi(end='?1049h')
    @staticmethod
    def disableAltBuffer():       return ansi(end='?1049l')

    # https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#screen-modes
    @staticmethod
    def mode(id: int, reset=False):
        return ansi(f'={id}', end=('l'if reset else'h'))
