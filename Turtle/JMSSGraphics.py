# JMSSGraphics v2.01

import turtle
import math

# ASCII commands
KEY_BACKSPACE     = 0xff08
KEY_TAB           = 0xff09
KEY_LINEFEED      = 0xff0a
KEY_CLEAR         = 0xff0b
KEY_RETURN        = 0xff0d
KEY_ENTER         = 0xff0d      # synonym
KEY_PAUSE         = 0xff13
KEY_SCROLLLOCK    = 0xff14
KEY_SYSREQ        = 0xff15
KEY_ESCAPE        = 0xff1b
KEY_SPACE         = 0xff20

# Cursor control and motion
KEY_HOME          = 0xff50
KEY_LEFT          = 0xff51
KEY_UP            = 0xff52
KEY_RIGHT         = 0xff53
KEY_DOWN          = 0xff54
KEY_PAGEUP        = 0xff55
KEY_PAGEDOWN      = 0xff56
KEY_END           = 0xff57
KEY_BEGIN         = 0xff58

# Misc functions
KEY_DELETE        = 0xffff
KEY_SELECT        = 0xff60
KEY_PRINT         = 0xff61
KEY_EXECUTE       = 0xff62
KEY_INSERT        = 0xff63
KEY_UNDO          = 0xff65
KEY_REDO          = 0xff66
KEY_MENU          = 0xff67
KEY_FIND          = 0xff68
KEY_CANCEL        = 0xff69
KEY_HELP          = 0xff6a
KEY_BREAK         = 0xff6b
KEY_MODESWITCH    = 0xff7e
KEY_SCRIPTSWITCH  = 0xff7e
KEY_FUNCTION      = 0xffd2

# Text motion constants: these are allowed to clash with key constants
KEY_MOTION_UP                = KEY_UP
KEY_MOTION_RIGHT             = KEY_RIGHT
KEY_MOTION_DOWN              = KEY_DOWN
KEY_MOTION_LEFT              = KEY_LEFT
KEY_MOTION_NEXT_WORD         = 1
KEY_MOTION_PREVIOUS_WORD     = 2
KEY_MOTION_BEGINNING_OF_LINE = 3
KEY_MOTION_END_OF_LINE       = 4
KEY_MOTION_NEXT_PAGE         = KEY_PAGEDOWN
KEY_MOTION_PREVIOUS_PAGE     = KEY_PAGEUP
KEY_MOTION_BEGINNING_OF_FILE = 5
KEY_MOTION_END_OF_FILE       = 6
KEY_MOTION_BACKSPACE         = KEY_BACKSPACE
KEY_MOTION_DELETE            = KEY_DELETE

# Number pad
KEY_NUMLOCK       = 0xff7f
KEY_NUM_SPACE     = 0xff80
KEY_NUM_TAB       = 0xff89
KEY_NUM_ENTER     = 0xff8d
KEY_NUM_F1        = 0xff91
KEY_NUM_F2        = 0xff92
KEY_NUM_F3        = 0xff93
KEY_NUM_F4        = 0xff94
KEY_NUM_HOME      = 0xff95
KEY_NUM_LEFT      = 0xff96
KEY_NUM_UP        = 0xff97
KEY_NUM_RIGHT     = 0xff98
KEY_NUM_DOWN      = 0xff99
KEY_NUM_PRIOR     = 0xff9a
KEY_NUM_PAGE_UP   = 0xff9a
KEY_NUM_NEXT      = 0xff9b
KEY_NUM_PAGE_DOWN = 0xff9b
KEY_NUM_END       = 0xff9c
KEY_NUM_BEGIN     = 0xff9d
KEY_NUM_INSERT    = 0xff9e
KEY_NUM_DELETE    = 0xff9f
KEY_NUM_EQUAL     = 0xffbd
KEY_NUM_MULTIPLY  = 0xffaa
KEY_NUM_ADD       = 0xffab
KEY_NUM_SEPARATOR = 0xffac
KEY_NUM_SUBTRACT  = 0xffad
KEY_NUM_DECIMAL   = 0xffae
KEY_NUM_DIVIDE    = 0xffaf

KEY_NUM_0         = 0xffb0
KEY_NUM_1         = 0xffb1
KEY_NUM_2         = 0xffb2
KEY_NUM_3         = 0xffb3
KEY_NUM_4         = 0xffb4
KEY_NUM_5         = 0xffb5
KEY_NUM_6         = 0xffb6
KEY_NUM_7         = 0xffb7
KEY_NUM_8         = 0xffb8
KEY_NUM_9         = 0xffb9

# Function keys
KEY_F1            = 0xffbe
KEY_F2            = 0xffbf
KEY_F3            = 0xffc0
KEY_F4            = 0xffc1
KEY_F5            = 0xffc2
KEY_F6            = 0xffc3
KEY_F7            = 0xffc4
KEY_F8            = 0xffc5
KEY_F9            = 0xffc6
KEY_F10           = 0xffc7
KEY_F11           = 0xffc8
KEY_F12           = 0xffc9
KEY_F13           = 0xffca
KEY_F14           = 0xffcb
KEY_F15           = 0xffcc
KEY_F16           = 0xffcd
KEY_F17           = 0xffce
KEY_F18           = 0xffcf
KEY_F19           = 0xffd0
KEY_F20           = 0xffd1

# Modifiers
KEY_LSHIFT        = 0xffe1
KEY_RSHIFT        = 0xffe2
KEY_LCTRL         = 0xffe3
KEY_RCTRL         = 0xffe4
KEY_CAPSLOCK      = 0xffe5
KEY_LMETA         = 0xffe7
KEY_RMETA         = 0xffe8
KEY_LALT          = 0xffe9
KEY_RALT          = 0xffea
KEY_LWINDOWS      = 0xffeb
KEY_RWINDOWS      = 0xffec
KEY_LCOMMAND      = 0xffed
KEY_RCOMMAND      = 0xffee
KEY_LOPTION       = 0xffef
KEY_ROPTION       = 0xfff0

# Latin-1
KEY_SPACE         = 0x020
KEY_EXCLAMATION   = 0x021
KEY_DOUBLEQUOTE   = 0x022
KEY_HASH          = 0x023
KEY_POUND         = 0x023  # synonym
KEY_DOLLAR        = 0x024
KEY_PERCENT       = 0x025
KEY_AMPERSAND     = 0x026
KEY_APOSTROPHE    = 0x027
KEY_PARENLEFT     = 0x028
KEY_PARENRIGHT    = 0x029
KEY_ASTERISK      = 0x02a
KEY_PLUS          = 0x02b
KEY_COMMA         = 0x02c
KEY_MINUS         = 0x02d
KEY_PERIOD        = 0x02e
KEY_SLASH         = 0x02f
KEY__0            = 0x030
KEY__1            = 0x031
KEY__2            = 0x032
KEY__3            = 0x033
KEY__4            = 0x034
KEY__5            = 0x035
KEY__6            = 0x036
KEY__7            = 0x037
KEY__8            = 0x038
KEY__9            = 0x039
KEY_COLON         = 0x03a
KEY_SEMICOLON     = 0x03b
KEY_LESS          = 0x03c
KEY_EQUAL         = 0x03d
KEY_GREATER       = 0x03e
KEY_QUESTION      = 0x03f
KEY_AT            = 0x040
KEY_BRACKETLEFT   = 0x05b
KEY_BACKSLASH     = 0x05c
KEY_BRACKETRIGHT  = 0x05d
KEY_ASCIICIRCUM   = 0x05e
KEY_UNDERSCORE    = 0x05f
KEY_GRAVE         = 0x060
KEY_QUOTELEFT     = 0x060
KEY_A             = 0x061
KEY_B             = 0x062
KEY_C             = 0x063
KEY_D             = 0x064
KEY_E             = 0x065
KEY_F             = 0x066
KEY_G             = 0x067
KEY_H             = 0x068
KEY_I             = 0x069
KEY_J             = 0x06a
KEY_K             = 0x06b
KEY_L             = 0x06c
KEY_M             = 0x06d
KEY_N             = 0x06e
KEY_O             = 0x06f
KEY_P             = 0x070
KEY_Q             = 0x071
KEY_R             = 0x072
KEY_S             = 0x073
KEY_T             = 0x074
KEY_U             = 0x075
KEY_V             = 0x076
KEY_W             = 0x077
KEY_X             = 0x078
KEY_Y             = 0x079
KEY_Z             = 0x07a
KEY_BRACELEFT     = 0x07b
KEY_BAR           = 0x07c
KEY_BRACERIGHT    = 0x07d
KEY_ASCIITILDE    = 0x07e

MOUSE_BUTTON_NONE   = 0
MOUSE_BUTTON_LEFT   = 1
MOUSE_BUTTON_RIGHT  = 2
MOUSE_BUTTON_MIDDLE = 3

from tkinter import PhotoImage
import tkinter as tk
import time

"""
A simple graphics wrapper around PyGame.
It redefines the coordinate system to be like the Secondary School level cartesian axes.
It also exposes a simple turtle object that can be manipulated like the LOGO turtle for
basic line drawing.
"""
class Graphics:
    """
    Constructor:
        Arguments:
            width - the width of the window in pixels
            height - the height of the window in pixels
            title - the title to show in the window
            fps - how many frames per second to run the main update loop
        Returns:   None
    """
    def __init__(self, width, height, title = "", mainloop = None, fps = 60, fullscreen = False, autorun = True):
        self.width = width
        self.height = height
        self.done = False
        self.fps = fps

        self.listeners = []

        self.root = tk.Tk()
        self.root.title(title)

        self.root.protocol("WM_DELETE_WINDOW", self.close_window)

        canvas = tk.Canvas(master=self.root, width=width, height=height)

        canvas.pack()

        self.t = turtle.RawTurtle(canvas)
        self.screen = self.t.getscreen()

        self.draw_func = mainloop

        self.keys = dict([(a, False) for a in range(255)] +
                         [(a, False) for a in range(0xff00, 0xffff)])

        self.images = {}

        self.screen.onkeypress(self._onKeyPressed_Down, "Down")
        self.screen.onkeypress(self._onKeyPressed_Up, "Up")
        self.screen.onkeypress(self._onKeyPressed_Left, "Left")
        self.screen.onkeypress(self._onKeyPressed_Right, "Right")

        self.screen.onkeyrelease(self._onKeyReleased_Down, "Down")
        self.screen.onkeyrelease(self._onKeyReleased_Up, "Up")
        self.screen.onkeyrelease(self._onKeyReleased_Left, "Left")
        self.screen.onkeyrelease(self._onKeyReleased_Right, "Right")

        self.screen.onkeypress(self._onKeyPressed_W, "w")
        self.screen.onkeyrelease(self._onKeyReleased_W, "w")

        self.screen.onkeypress(self._onKeyPressed_S, "s")
        self.screen.onkeyrelease(self._onKeyReleased_S, "s")

        self.screen.onkeypress(self._onKeyPressed_A, "a")
        self.screen.onkeyrelease(self._onKeyReleased_A, "a")

        self.screen.onkeypress(self._onKeyPressed_D, "d")
        self.screen.onkeyrelease(self._onKeyReleased_D, "d")

        self.screen.listen()

        self.commands = []

        self.time_elapsed = 0
        self.time = time.perf_counter()
            

    def close_window(self):
        self.done = True
        self.draw_func = None
        self.root.destroy()
      

    """
    Returns the PyGame screen canvas - for direct PyGame manipulation
        Arguments: None
        Returns:   None
    """

    def getScreen(self):
        return self.screen

    """
    Sets the FPS (frames per second) for the update loop
        Arguments:
            fps - the number of frames per second
        Returns:   None
    """

    def setFPS(self, fps):
        self.fps = fps

    """
    Adds an event listener that will get triggered in the main loop based on received pygame events
    (e.g. keyboard or mouse events)
        Arguments:
            listener - An eventhandler function which takes a event as an argument
        Returns:
            None
    """

    def addEventListener(self, listener):
        self.listeners.append(listener)

    def _convX(self, x):
        return x - self.width / 2

    def _convY(self, y):
        return y - self.height / 2

    def _convXY(self, x, y):
        return [self._convX(x), self._convY(y)]

    """
    The main update loop that gets run FPS times per second
        Arguments:
            mainloop - The main loop function with optional arguments
        Returns:
            None
    """

    def init(self, func):
        self.init_func = func

    def code(self, func):
        self.draw_func = func

    def run(self):
        pass
    """
    Loads an image from disk and returns it as an object to be used in the drawImage() function
        Arguments:
            file - the filename of the image. Please include the extension.
        Returns:
            The image object
    """


    """
    Clears the screen with an optional colour.
        Arguments:
            color - (optional) the background colour. Color format is RGB: (255,255,255). Default is black.
        Returns:
            The image object
    """

    def clear(self, r = 0, g = 0, b = 0, a = 1):
        kwargs = {"r":r, "g":g, "b":b, "a":a}
        self.commands.append([self._clear, kwargs])

    def reveal(self):
        
        try:
            current_time = time.perf_counter()
            self.time_elapsed = current_time - self.time
            self.time = current_time
            
            self.t.ht()
            
            self.screen.tracer(0, 0)
            for command in self.commands:
                command[0](**command[1])
            self.screen.update()
            self.commands = []
            return True
        except tk.TclError as e: #:
            
            return False
        
    def _clear(self, r = 0, g = 0, b = 0, a = 1):
        self.screen.bgcolor([r, g, b])
        self.t.clear()

    """
    Gets the current mouse position
        Arguments:
            None
        Returns:
            The mouse coordinates as a (x,y) tuple
    """

    def getMousePos(self):
        return self._invconv(pygame.mouse.get_pos())

    def loadImage(self, file):
        try:
            image = PhotoImage(file=file)

            self.screen.register_shape(file, turtle.Shape("image", image))

            self.images[file] = image
            return file
        except Exception as e:
            print(e)
            return None

    """
    Draws an image on the screen. The image must first be loaded in using loadImage().
        Arguments:
            image - the image object. (Obtained from loadImage())
            pos - a (x, y) tuple specifying the coordinates of the TOP LEFT HAND CORNER of the image.
            rotation - (optional) the angle of rotation to be applied to the image
            pivot - (optional) the pivot point of the rotation. Centre by default
            alpha - (optional) controls how transparent the image is. 0 is fully transparent. 255 is fully opaque.
            scale - (optional) a (width, height) tuple specifying how the image is to be stretches or squashed
            rect - (optional) a (x, y, width, height) rectangle specifying a sub-window of the original image to draw
                   (useful for spritesheets and animations etc.)
        Returns:
            None
    """

    def drawImage(self, image, x, y, width = None, height = None, rotation=0, anchorX = None, anchorY = None, opacity=None, rect=None):
        kwargs = {"image":image, \
                  "x":x, \
                  "y":y}
        self.commands.append([self._drawImage, kwargs])
        
    def _drawImage(self, image, x, y, width = None, height = None, rotation=0, anchorX = None, anchorY = None, opacity=None, rect=None):
        try:
            self.t.shape(image)
        except turtle.TurtleGraphicsError as e:
            self.t.shape(self.loadImage(image))
        finally:
            self.t.pu()
            self.t.setpos(self._convXY(x + int(self.images[image].width()/2),y + int(self.images[image].height()/2)))
            self.t.pd()
            self.t.stamp()
            
    def drawText(self, text, x, y, fontName = "Arial", fontSize = 10, color = (1, 1, 1, 1), anchorX = "left", anchorY ="bottom"):
        kwargs = {"text":text, \
                  "x":x, \
                  "y":y, \
                  "fontName": fontName,
                  "fontSize": fontSize,
                  "color": color}
        self.commands.append([self._drawText, kwargs])
        
    def _drawText(self, text, x, y, fontName = "Arial", fontSize = 10, color = (1, 1, 1, 1), anchorX = "left", anchorY ="bottom"):
        self.t.pu()
        self.t.color([color[0], color[1], color[2]])
        self.t.setpos(self._convXY(x, y))
        self.t.pd()
        self.t.write(text, move=False, align="left", font=(fontName, fontSize, "normal"))
        self.t.pu()

    """
    Draws a circle on the screen.
        Arguments:
            color - the circle's colour. Color format is RGB: (255,255,255)
            pos - a (x, y) tuple specifying the coordinates of the centre of the circle.
            radius - the radius of the circle in pixels
            width - the width of the outline of the circle. For a filled circle, set this to 0
        Returns:
            None
    """

    def drawCircle(self, color, pos, radius, width=0):
        turtle.pu()
        turtle.setpos(pos)
        turtle.pd()
        turtle.color(self._convCol(color))
        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()

    """
    Draws a pixel on the screen.
        Arguments:
            color - the pixel's colour. Color format is RGB: (255,255,255)
            pos - a (x, y) tuple specifying the coordinates of the pixel.
        Returns:
            None
    """

    def drawPixel(self, color, pos):
        self.screen.set_at(self._conv(pos), color)

    def isKeyPressed(self, key):
        return self.keys[key]

    def _onKeyPressed_Up(self):
        self.keys[KEY_UP] = True
    def _onKeyPressed_Down(self):
        self.keys[KEY_DOWN] = True
    def _onKeyPressed_Left(self):
        self.keys[KEY_LEFT] = True
    def _onKeyPressed_Right(self):
        self.keys[KEY_RIGHT] = True

    def _onKeyReleased_Up(self):
        self.keys[KEY_UP] = False
    def _onKeyReleased_Down(self):
        self.keys[KEY_DOWN] = False
    def _onKeyReleased_Left(self):
        self.keys[KEY_LEFT] = False
    def _onKeyReleased_Right(self):
        self.keys[KEY_RIGHT] = False


    def _onKeyPressed_W(self):
        self.keys[KEY_W] = True
    def _onKeyReleased_W(self):
        self.keys[KEY_W] = False

    def _onKeyPressed_S(self):
        self.keys[KEY_S] = True
    def _onKeyReleased_S(self):
        self.keys[KEY_S] = False

    def _onKeyPressed_A(self):
        self.keys[KEY_A] = True
    def _onKeyReleased_A(self):
        self.keys[KEY_A] = False

    def _onKeyPressed_D(self):
        self.keys[KEY_D] = True
    def _onKeyReleased_D(self):
        self.keys[KEY_D] = False

#######################################################################
"""
This module is released under the Python Software Foundation license, which
can be found at http://www.python.org/  It requires Python 2.3 or later.

Richie Hindle, _richie@entrian.com_

Version 1.0, released 1st April 2004.
Tweaked by Toan Huynh 8th December, 2018.
"""


import sys, token, tokenize

class MissingLabelError(Exception):
    """'goto' without matching 'label'."""
    pass

# Source filenames -> line numbers of plain gotos -> target label names.
_plainGotoCache = {}

# Source filenames -> line numbers of computed gotos -> identifier names.
_computedGotoCache = {}

# Source filenames -> line numbers of labels -> label names.
_labelCache = {}

# Source filenames -> label names -> line numbers of those labels.
_labelNameCache = {}

# Source filenames -> comefrom label names -> line numbers of those comefroms.
_comefromNameCache = {}

def _addToCaches(moduleFilename):
    """Finds the labels and gotos in a module and adds them to the caches."""

    # The token patterns that denote gotos and labels.
    plainGotoPattern = [(token.NAME, 'goto'), (token.OP, '.')]
    computedGotoPattern = [(token.NAME, 'goto'), (token.OP, '*')]
    labelPattern = [(token.NAME, 'label'), (token.OP, '.')]
    comefromPattern = [(token.NAME, 'comefrom'), (token.OP, '.')]

    # Initialise this module's cache entries.
    _plainGotoCache[moduleFilename] = {}
    _computedGotoCache[moduleFilename] = {}
    _labelCache[moduleFilename] = {}
    _labelNameCache[moduleFilename] = {}
    _comefromNameCache[moduleFilename] = {}

    # Tokenize the module; 'window' is the last two (type, string) pairs.
    window = [(None, ''), (None, '')]
    for tokenType, tokenString, (startRow, startCol), (endRow, endCol), line \
            in tokenize.generate_tokens(open(moduleFilename, 'r').readline):
        # Plain goto: "goto .x"
        if window == plainGotoPattern:
            _plainGotoCache[moduleFilename][startRow] = tokenString

        # Computed goto: "goto *identifier"  XXX Allow expressions.
        elif window == computedGotoPattern:
            _computedGotoCache[moduleFilename][startRow] = tokenString

        # Comefrom: "comefrom .x"  XXX Non-determinism via multiple comefroms.
        if window == comefromPattern:
            _comefromNameCache[moduleFilename][tokenString] = startRow

        # Label: "label .x"  XXX Computed labels.
        elif window == labelPattern:
            _labelCache[moduleFilename][startRow] = tokenString
            _labelNameCache[moduleFilename][tokenString] = startRow

        # Move the token window back by one.
        window = [window[1], (tokenType, tokenString)]

    #print(_labelNameCache)

def _trace(frame, event, arg):
    # If this is the first time we've seen this source file, cache it.
    filename = frame.f_code.co_filename
    if filename[0] == "<":
        return
    if filename not in _plainGotoCache:
        _addToCaches(filename)

    # Is there a goto on this line?
    targetLabel = _plainGotoCache[filename].get(frame.f_lineno)
    if not targetLabel:
        # No plain goto.  Is there a computed goto?
        identifier = _computedGotoCache[filename].get(frame.f_lineno)
        if identifier:
            # If eval explodes, just let the exception propagate.
            targetLabel = eval(identifier, frame.f_globals, frame.f_locals)

    # Jump to the label's line.
    if targetLabel:
        try:
            targetLine = _labelNameCache[filename][targetLabel]
        except KeyError:
            raise (MissingLabelError, "Missing label: %s" % targetLabel)
        frame.f_lineno = targetLine

    # Is there a label on this line with a corresponding comefrom?
    label = _labelCache[filename].get(frame.f_lineno)
    if label:
        targetComefromLine = _comefromNameCache[filename].get(label)
        if targetComefromLine:
            frame.f_lineno = targetComefromLine

    return _trace

# Install the trace function, including all preceding frames.
sys.settrace(_trace)
frame = sys._getframe().f_back
while frame:
    frame.f_trace = _trace
    frame = frame.f_back

# Define the so-called keywords for importing: 'goto', 'label' and 'comefrom'.
class _Label:
    """Allows arbitrary x.y attribute lookups."""
    def __getattr__(self, name):
        return None

goto = None
label = _Label()
comefrom = _Label()

