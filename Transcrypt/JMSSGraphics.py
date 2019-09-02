'''

from browser import doc
from browser import timer
from browser import html

from browser import window, load
'''

#load("howler.js")
import math

__pragma__ ('kwargs')
# Key symbol constants

# ASCII commands
KEY_BACKSPACE     = 0xff08
KEY_TAB           = 0xff09
KEY_LINEFEED      = 0xff0a
KEY_CLEAR         = 0xff0b
KEY_RETURN        = 13
KEY_ENTER         = 13      # synonym
KEY_PAUSE         = 0xff13
KEY_SCROLLLOCK    = 0xff14
KEY_SYSREQ        = 0xff15
KEY_ESCAPE        = 0xff1b
KEY_KEY_SPACE         = 0xff20

# Cursor control and motion
KEY_HOME          = 0xff50
KEY_LEFT          = 37
KEY_UP            = 38
KEY_RIGHT         = 39
KEY_DOWN          = 40
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
KEY_SPACE         = 32
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
KEY_A             = 65
KEY_B             = 66
KEY_C             = 67
KEY_D             = 68
KEY_E             = 69
KEY_F             = 70
KEY_G             = 71
KEY_H             = 72
KEY_I             = 73
KEY_J             = 74
KEY_K             = 75
KEY_L             = 76
KEY_M             = 77
KEY_N             = 78
KEY_O             = 79
KEY_P             = 80
KEY_Q             = 81
KEY_R             = 82
KEY_S             = 83
KEY_T             = 84
KEY_U             = 85
KEY_V             = 86
KEY_W             = 87
KEY_X             = 88
KEY_Y             = 89
KEY_Z             = 90
KEY_BRACELEFT     = 0x07b
KEY_BAR           = 0x07c
KEY_BRACERIGHT    = 0x07d
KEY_ASCIITILDE    = 0x07e

MOUSE_BUTTON_NONE   = 0
MOUSE_BUTTON_LEFT   = 1
MOUSE_BUTTON_RIGHT  = 2
MOUSE_BUTTON_MIDDLE = 3

class JMSSImage():
    def __init__(self, image, name = None):
        self.img = image
        self.height = image.naturalHeight
        self.width = image.naturalWidth
        self.name = name

class Graphics:
    def _keydown(self, ev):
        self.keys[ev.which] = True

    def _keyup(self, ev):
        self.keys[ev.which] = False

    def _mousemove(self, ev):
        rect = ev.target.getBoundingClientRect()        
        self.mouse_pos = (ev.clientX - rect.left, ev.clientY - rect.top)

    def _touchstart(self, ev):
        rect = ev.target.getBoundingClientRect()        
        self.mouse_pos = (ev.touches[0].clientX - rect.left, ev.touches[0].clientY - rect.top)
        self.mouse_buttons = MOUSE_BUTTON_LEFT

    def _touchmove(self, ev):
        rect = ev.target.getBoundingClientRect()        
        self.mouse_pos = (ev.touches[0].clientX - rect.left, ev.touches[0].clientY - rect.top)
        self.mouse_buttons = MOUSE_BUTTON_LEFT

    def _touchend(self, ev):
        self.mouse_buttons = MOUSE_BUTTON_NONE

    def _mouseup(self, ev):
        rect = ev.target.getBoundingClientRect()        
        self.mouse_pos = (ev.clientX - rect.left, ev.clientY - rect.top)
        
        self.mouse_buttons = MOUSE_BUTTON_NONE

    def _mousedown(self, ev):
        rect = ev.target.getBoundingClientRect()        
        self.mouse_pos = (ev.clientX - rect.left, ev.clientY - rect.top)
        
        if ev.button == 0:
            self.mouse_buttons = MOUSE_BUTTON_LEFT
        elif ev.button == 1:
            self.mouse_buttons = MOUSE_BUTTON_MIDDLE
        elif ev.button == 2:
            self.mouse_buttons = MOUSE_BUTTON_RIGHT


    def __init__(self, width, height, title = "", fps = 60):
        self.width = width
        self.height = height
        self.title = title
        self.done = False
        self.fps = fps

        self.listeners = []

        self.draw_func = None
        self.init_func = None

        #self.keys = dict([(a, False) for a in range(255)] +
        #                 [(a, False) for a in range(0xff00, 0xffff)])
        self.keys = dict([(a, False) for a in range(255)])

        self.mouse_event = None
        self.mouse_pos = None
        self.mouse_buttons = 0

        #c = html.CANVAS(width=self.width, height=self.height, id="canvas")


        #doc <= c

        #self.canvas = doc["canvas"]
        #self.ctx = self.canvas.getContext('2d')

        self.canvas = document.getElementById('canvas')
        self.canvas.setAttribute("width", self.width)
        self.canvas.setAttribute("height", self.width)
        self.ctx = self.canvas.getContext('2d')


        #doc <= html.TITLE(self.title)

        document.onkeydown = self._keydown
        document.onkeyup = self._keyup
        document.onmousemove = self._mousemove
        document.onmousedown = self._mousedown
        document.onmouseup = self._mouseup
        document.ontouchstart = self._touchstart
        document.ontouchmove = self._touchmove
        document.ontouchend = self._touchend

        '''
        self.canvas.bind("keyup", self._keyup)
        self.canvas.bind("mousemove", self._mousemove)
        self.canvas.bind("mousedown", self._mousedown)
        self.canvas.bind("mouseup", self._mouseup)
        self.canvas.bind("touchstart", self._touchstart)
        self.canvas.bind("touchmove", self._touchmove)
        self.canvas.bind("touchend", self._touchend)
        '''
        self.pixel_id = self.ctx.createImageData(1, 1)
        self.pixel_color = self.pixel_id.data


        self.soundPlayers = {}

        self.loadingResources = 0

        self.resources = {}

        self.commands = []
        self.prevTimeStamp = 0

    def reveal(self):
        return

    def run(self):
        #window.setInterval(self.draw_func, 17.0)
        window.setInterval(self.draw_func, 1/self.fps * 1000)

    def close(self):
        return

    def exit(self):
        return

    def pageshow(self, ev):
        self.init_func()

    def init(self, func):
        self.init_func = func

    def mainloop(self, func):
        self.draw_func = func

    def clear(self, r = 0, g = 0, b = 0, a = 1):
        self.ctx.fillStyle= "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(int(a * 255.0))+ ")"
        self.ctx.fillRect(0, 0, self.width, self.height)

    def setFPS(self, fps):
        self.fps = fps

    def resourceLoaded(self, e):
        self.loadingResources -= 1
        e.target.jmssImg.height = e.target.naturalHeight
        e.target.jmssImg.width = e.target.naturalWidth

    def loadImage(self, file):
        if file in self.resources:
            return self.resources[file]
        self.loadingResources += 1
        img = document.createElement("img")
        img.addEventListener('load', self.resourceLoaded, False)
        img.setAttribute("src", file)

        jmssImg = JMSSImage(img)
        img.jmssImg = jmssImg
        self.resources[file] = jmssImg

        return jmssImg

    def isKeyPressed(self, key):
        return self.keys[key]
    def isKeyDown(self, key):
        return self.isKeyPressed(key)

    def isMousePressed(self, button):
        return self.mouse_buttons == button

    def getMousePos(self):
        if self.mouse_pos is not None:
            return self.mouse_pos
        else:
            return (0, 0)

    def _convY(self, y):
        return self.height - y

    def _convColor(self, c):
        return (int(c[0] * 255.0), int(c[1] * 255.0), int(c[2] * 255.0), int(c[3] * 255.0))

    def loadSound(self, filename, streaming = False):
        howl = window.Howl
        return __new__(howl({"src": [filename]}))

    def playSound(self, sound, loop = False):
        sound.loop = loop
        sound.play()

    def pauseSound(self, sound):
        if sound in self.soundPlayers:
            self.soundPlayers[sound].pause()

    def drawText(self, text, x, y, fontName = "Arial", fontSize = 10, color = (1, 1, 1, 1), anchorX = "left", anchorY ="bottom"):
        #print(text)
        if self.loadingResources > 0:
            return
        self.ctx.fillStyle = "rgba(" + str(int(color[0] * 255.0)) + "," + str(int(color[1] * 255.0)) + "," + str(int(color[2] * 255.0)) + "," + str(int(color[3] * 255.0)) + ")"
        self.ctx.font = str(fontSize) + "pt " + fontName
        self.ctx.textBaseline = "bottom"
        self.ctx.fillText(text, x, self.height - y)

    def drawImage(self, image, x, y, width = None, height = None, rotation=0, anchorX = None, anchorY = None, opacity=None, rect=None):
        if (isinstance(image, str)):
            image = self.loadImage(image)
        if self.loadingResources > 0:
            return
        self.ctx.save()

        if width is None:
            width = image.width

        if height is None:
            height = image.height

        if opacity is not None:
            if opacity > 1.0:
                opacity = 1.0
            elif opacity < 0.0:
                opacity = 0.0
            self.ctx.globalAlpha = opacity


        if rotation != 0.0:
            # TODO: Buggy!!!
            self.ctx.save()
            self.ctx.translate(x + width/2, self._convY(y + height/2))
            self.ctx.rotate((rotation)* math.PI / 180)
            self.ctx.drawImage(image.img, -width/2, -height/2, width, height)
            self.ctx.restore()
        else:
            self.ctx.drawImage(image.img, x, self._convY(y + height), width, height)


        self.ctx.restore()

    def drawPixel(self, x, y, r = 1.0, g = 1.0, b = 1.0, a = 1.0):
        self.pixel_color[0] = int(r * 255.0)
        self.pixel_color[1] = int(g * 255.0)
        self.pixel_color[2] = int(b * 255.0)
        self.pixel_color[3] = int(a * 255.0)
        self.ctx.putImageData(self.pixel_id, x, self._convY(y))


    def drawLine(self, x1, y1, x2, y2, r = 1.0, g = 1.0, b = 1.0, a = 1.0, width = 1):
        self.ctx.beginPath()
        self.ctx.lineWidth = width
        self.ctx.strokeStyle = "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(int(a * 255.0)) + ")"
        self.ctx.moveTo(x1, self._convY(y1))
        self.ctx.lineTo(x2, self._convY(y2))
        self.ctx.stroke()

    def drawCircle(self, x, y, radius, r=1.0, g=1.0, b=1.0, a=1.0):
        self.ctx.fillStyle = "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(int(a * 255.0)) + ")"
        self.ctx.beginPath();
        self.ctx.strokeStyle = "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(
            int(b * 255.0)) + "," + str(int(a * 255.0)) + ")"

        self.ctx.arc(x, self._convY(y), radius, 0, 2 * Math.PI, True);

        self.ctx.fill();

        self.ctx.stroke()

    def drawRect(self, x1, y1, x2, y2, r = 1.0, g = 1.0, b = 1.0, a = 1.0):
        ctx = self.ctx
        ctx.fillStyle = "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(int(a * 255.0)) + ")"        
        ctx.beginPath();
        ctx.moveTo(x1, self._convY(y1));
        ctx.lineTo(x2, self._convY(y1));
        ctx.lineTo(x2, self._convY(y2));
        ctx.lineTo(x1, self._convY(y2));
        ctx.closePath();
        ctx.fill();            
