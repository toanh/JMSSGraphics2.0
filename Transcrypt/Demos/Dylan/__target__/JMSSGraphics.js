// Transcrypt'ed from Python, 2018-12-16 20:18:35
var math = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_math__ from './math.js';
__nest__ (math, '', __module_math__);
var __name__ = 'JMSSGraphics';
export var KEY_BACKSPACE = 65288;
export var KEY_TAB = 65289;
export var KEY_LINEFEED = 65290;
export var KEY_CLEAR = 65291;
export var KEY_RETURN = 13;
export var KEY_ENTER = 13;
export var KEY_PAUSE = 65299;
export var KEY_SCROLLLOCK = 65300;
export var KEY_SYSREQ = 65301;
export var KEY_ESCAPE = 65307;
export var KEY_KEY_SPACE = 65312;
export var KEY_HOME = 65360;
export var KEY_LEFT = 37;
export var KEY_UP = 38;
export var KEY_RIGHT = 39;
export var KEY_DOWN = 40;
export var KEY_PAGEUP = 65365;
export var KEY_PAGEDOWN = 65366;
export var KEY_END = 65367;
export var KEY_BEGIN = 65368;
export var KEY_DELETE = 65535;
export var KEY_SELECT = 65376;
export var KEY_PRINT = 65377;
export var KEY_EXECUTE = 65378;
export var KEY_INSERT = 65379;
export var KEY_UNDO = 65381;
export var KEY_REDO = 65382;
export var KEY_MENU = 65383;
export var KEY_FIND = 65384;
export var KEY_CANCEL = 65385;
export var KEY_HELP = 65386;
export var KEY_BREAK = 65387;
export var KEY_MODESWITCH = 65406;
export var KEY_SCRIPTSWITCH = 65406;
export var KEY_FUNCTION = 65490;
export var KEY_MOTION_UP = KEY_UP;
export var KEY_MOTION_RIGHT = KEY_RIGHT;
export var KEY_MOTION_DOWN = KEY_DOWN;
export var KEY_MOTION_LEFT = KEY_LEFT;
export var KEY_MOTION_NEXT_WORD = 1;
export var KEY_MOTION_PREVIOUS_WORD = 2;
export var KEY_MOTION_BEGINNING_OF_LINE = 3;
export var KEY_MOTION_END_OF_LINE = 4;
export var KEY_MOTION_NEXT_PAGE = KEY_PAGEDOWN;
export var KEY_MOTION_PREVIOUS_PAGE = KEY_PAGEUP;
export var KEY_MOTION_BEGINNING_OF_FILE = 5;
export var KEY_MOTION_END_OF_FILE = 6;
export var KEY_MOTION_BACKSPACE = KEY_BACKSPACE;
export var KEY_MOTION_DELETE = KEY_DELETE;
export var KEY_NUMLOCK = 65407;
export var KEY_NUM_SPACE = 65408;
export var KEY_NUM_TAB = 65417;
export var KEY_NUM_ENTER = 65421;
export var KEY_NUM_F1 = 65425;
export var KEY_NUM_F2 = 65426;
export var KEY_NUM_F3 = 65427;
export var KEY_NUM_F4 = 65428;
export var KEY_NUM_HOME = 65429;
export var KEY_NUM_LEFT = 65430;
export var KEY_NUM_UP = 65431;
export var KEY_NUM_RIGHT = 65432;
export var KEY_NUM_DOWN = 65433;
export var KEY_NUM_PRIOR = 65434;
export var KEY_NUM_PAGE_UP = 65434;
export var KEY_NUM_NEXT = 65435;
export var KEY_NUM_PAGE_DOWN = 65435;
export var KEY_NUM_END = 65436;
export var KEY_NUM_BEGIN = 65437;
export var KEY_NUM_INSERT = 65438;
export var KEY_NUM_DELETE = 65439;
export var KEY_NUM_EQUAL = 65469;
export var KEY_NUM_MULTIPLY = 65450;
export var KEY_NUM_ADD = 65451;
export var KEY_NUM_SEPARATOR = 65452;
export var KEY_NUM_SUBTRACT = 65453;
export var KEY_NUM_DECIMAL = 65454;
export var KEY_NUM_DIVIDE = 65455;
export var KEY_NUM_0 = 65456;
export var KEY_NUM_1 = 65457;
export var KEY_NUM_2 = 65458;
export var KEY_NUM_3 = 65459;
export var KEY_NUM_4 = 65460;
export var KEY_NUM_5 = 65461;
export var KEY_NUM_6 = 65462;
export var KEY_NUM_7 = 65463;
export var KEY_NUM_8 = 65464;
export var KEY_NUM_9 = 65465;
export var KEY_F1 = 65470;
export var KEY_F2 = 65471;
export var KEY_F3 = 65472;
export var KEY_F4 = 65473;
export var KEY_F5 = 65474;
export var KEY_F6 = 65475;
export var KEY_F7 = 65476;
export var KEY_F8 = 65477;
export var KEY_F9 = 65478;
export var KEY_F10 = 65479;
export var KEY_F11 = 65480;
export var KEY_F12 = 65481;
export var KEY_F13 = 65482;
export var KEY_F14 = 65483;
export var KEY_F15 = 65484;
export var KEY_F16 = 65485;
export var KEY_F17 = 65486;
export var KEY_F18 = 65487;
export var KEY_F19 = 65488;
export var KEY_F20 = 65489;
export var KEY_LSHIFT = 65505;
export var KEY_RSHIFT = 65506;
export var KEY_LCTRL = 65507;
export var KEY_RCTRL = 65508;
export var KEY_CAPSLOCK = 65509;
export var KEY_LMETA = 65511;
export var KEY_RMETA = 65512;
export var KEY_LALT = 65513;
export var KEY_RALT = 65514;
export var KEY_LWINDOWS = 65515;
export var KEY_RWINDOWS = 65516;
export var KEY_LCOMMAND = 65517;
export var KEY_RCOMMAND = 65518;
export var KEY_LOPTION = 65519;
export var KEY_ROPTION = 65520;
export var KEY_SPACE = 32;
export var KEY_EXCLAMATION = 33;
export var KEY_DOUBLEQUOTE = 34;
export var KEY_HASH = 35;
export var KEY_POUND = 35;
export var KEY_DOLLAR = 36;
export var KEY_PERCENT = 37;
export var KEY_AMPERSAND = 38;
export var KEY_APOSTROPHE = 39;
export var KEY_PARENLEFT = 40;
export var KEY_PARENRIGHT = 41;
export var KEY_ASTERISK = 42;
export var KEY_PLUS = 43;
export var KEY_COMMA = 44;
export var KEY_MINUS = 45;
export var KEY_PERIOD = 46;
export var KEY_SLASH = 47;
export var KEY__0 = 48;
export var KEY__1 = 49;
export var KEY__2 = 50;
export var KEY__3 = 51;
export var KEY__4 = 52;
export var KEY__5 = 53;
export var KEY__6 = 54;
export var KEY__7 = 55;
export var KEY__8 = 56;
export var KEY__9 = 57;
export var KEY_COLON = 58;
export var KEY_SEMICOLON = 59;
export var KEY_LESS = 60;
export var KEY_EQUAL = 61;
export var KEY_GREATER = 62;
export var KEY_QUESTION = 63;
export var KEY_AT = 64;
export var KEY_BRACKETLEFT = 91;
export var KEY_BACKSLASH = 92;
export var KEY_BRACKETRIGHT = 93;
export var KEY_ASCIICIRCUM = 94;
export var KEY_UNDERSCORE = 95;
export var KEY_GRAVE = 96;
export var KEY_QUOTELEFT = 96;
export var KEY_A = 65;
export var KEY_B = 66;
export var KEY_C = 67;
export var KEY_D = 68;
export var KEY_E = 69;
export var KEY_F = 70;
export var KEY_G = 71;
export var KEY_H = 72;
export var KEY_I = 73;
export var KEY_J = 74;
export var KEY_K = 75;
export var KEY_L = 76;
export var KEY_M = 77;
export var KEY_N = 78;
export var KEY_O = 79;
export var KEY_P = 80;
export var KEY_Q = 81;
export var KEY_R = 82;
export var KEY_S = 83;
export var KEY_T = 84;
export var KEY_U = 85;
export var KEY_V = 86;
export var KEY_W = 87;
export var KEY_X = 88;
export var KEY_Y = 89;
export var KEY_Z = 90;
export var KEY_BRACELEFT = 123;
export var KEY_BAR = 124;
export var KEY_BRACERIGHT = 125;
export var KEY_ASCIITILDE = 126;
export var MOUSE_BUTTON_NONE = 0;
export var MOUSE_BUTTON_LEFT = 1;
export var MOUSE_BUTTON_RIGHT = 2;
export var MOUSE_BUTTON_MIDDLE = 3;
export var JMSSImage =  __class__ ('JMSSImage', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, image, py_name) {
		if (typeof py_name == 'undefined' || (py_name != null && py_name.hasOwnProperty ("__kwargtrans__"))) {;
			var py_name = null;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'image': var image = __allkwargs0__ [__attrib0__]; break;
						case 'py_name': var py_name = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.img = image;
		self.height = image.naturalHeight;
		self.width = image.naturalWidth;
		self.py_name = py_name;
	});}
});
export var Graphics =  __class__ ('Graphics', [object], {
	__module__: __name__,
	get _keydown () {return __get__ (this, function (self, ev) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'ev': var ev = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.py_keys [ev.which] = true;
	});},
	get _keyup () {return __get__ (this, function (self, ev) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'ev': var ev = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.py_keys [ev.which] = false;
	});},
	get _mousemove () {return __get__ (this, function (self, ev) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'ev': var ev = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		var rect = ev.target.getBoundingClientRect ();
		self.mouse_pos = tuple ([ev.clientX - rect.left, ev.clientY - rect.top]);
	});},
	get _touchstart () {return __get__ (this, function (self, ev) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'ev': var ev = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		var rect = ev.target.getBoundingClientRect ();
		self.mouse_pos = tuple ([ev.touches [0].clientX - rect.left, ev.touches [0].clientY - rect.top]);
		self.mouse_buttons = MOUSE_BUTTON_LEFT;
	});},
	get _touchmove () {return __get__ (this, function (self, ev) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'ev': var ev = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		var rect = ev.target.getBoundingClientRect ();
		self.mouse_pos = tuple ([ev.touches [0].clientX - rect.left, ev.touches [0].clientY - rect.top]);
		self.mouse_buttons = MOUSE_BUTTON_LEFT;
	});},
	get _touchend () {return __get__ (this, function (self, ev) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'ev': var ev = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.mouse_buttons = MOUSE_BUTTON_NONE;
	});},
	get _mouseup () {return __get__ (this, function (self, ev) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'ev': var ev = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		var rect = ev.target.getBoundingClientRect ();
		self.mouse_pos = tuple ([ev.clientX - rect.left, ev.clientY - rect.top]);
		self.mouse_buttons = MOUSE_BUTTON_NONE;
	});},
	get _mousedown () {return __get__ (this, function (self, ev) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'ev': var ev = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		var rect = ev.target.getBoundingClientRect ();
		self.mouse_pos = tuple ([ev.clientX - rect.left, ev.clientY - rect.top]);
		if (ev.button == 0) {
			self.mouse_buttons = MOUSE_BUTTON_LEFT;
		}
		else if (ev.button == 1) {
			self.mouse_buttons = MOUSE_BUTTON_MIDDLE;
		}
		else if (ev.button == 2) {
			self.mouse_buttons = MOUSE_BUTTON_RIGHT;
		}
	});},
	get __init__ () {return __get__ (this, function (self, width, height, title, fps) {
		if (typeof title == 'undefined' || (title != null && title.hasOwnProperty ("__kwargtrans__"))) {;
			var title = '';
		};
		if (typeof fps == 'undefined' || (fps != null && fps.hasOwnProperty ("__kwargtrans__"))) {;
			var fps = 60;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'width': var width = __allkwargs0__ [__attrib0__]; break;
						case 'height': var height = __allkwargs0__ [__attrib0__]; break;
						case 'title': var title = __allkwargs0__ [__attrib0__]; break;
						case 'fps': var fps = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.width = width;
		self.height = height;
		self.title = title;
		self.done = false;
		self.fps = fps;
		self.listeners = list ([]);
		self.draw_func = null;
		self.init_func = null;
		self.py_keys = dict ((function () {
			var __accu0__ = [];
			for (var a = 0; a < 255; a++) {
				__accu0__.append (tuple ([a, false]));
			}
			return __accu0__;
		}) ());
		self.mouse_event = null;
		self.mouse_pos = null;
		self.mouse_buttons = 0;
		self.canvas = document.getElementById ('canvas');
		self.canvas.setAttribute ('width', self.width);
		self.canvas.setAttribute ('height', self.width);
		self.ctx = self.canvas.getContext ('2d');
		document.onkeydown = self._keydown;
		document.onkeyup = self._keyup;
		self.soundPlayers = dict ({});
		self.loadingResources = 0;
		self.resources = dict ({});
		self.commands = list ([]);
		self.prevTimeStamp = 0;
	});},
	get reveal () {return __get__ (this, function (self) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		return ;
	});},
	get run () {return __get__ (this, function (self) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		window.setInterval (self.draw_func, 17.0);
	});},
	get exit () {return __get__ (this, function (self) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		return ;
	});},
	get pageshow () {return __get__ (this, function (self, ev) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'ev': var ev = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.init_func ();
	});},
	get init () {return __get__ (this, function (self, func) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'func': var func = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.init_func = func;
	});},
	get mainloop () {return __get__ (this, function (self, func) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'func': var func = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.draw_func = func;
	});},
	get py_clear () {return __get__ (this, function (self, r, g, b, a) {
		if (typeof r == 'undefined' || (r != null && r.hasOwnProperty ("__kwargtrans__"))) {;
			var r = 0;
		};
		if (typeof g == 'undefined' || (g != null && g.hasOwnProperty ("__kwargtrans__"))) {;
			var g = 0;
		};
		if (typeof b == 'undefined' || (b != null && b.hasOwnProperty ("__kwargtrans__"))) {;
			var b = 0;
		};
		if (typeof a == 'undefined' || (a != null && a.hasOwnProperty ("__kwargtrans__"))) {;
			var a = 1;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'r': var r = __allkwargs0__ [__attrib0__]; break;
						case 'g': var g = __allkwargs0__ [__attrib0__]; break;
						case 'b': var b = __allkwargs0__ [__attrib0__]; break;
						case 'a': var a = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.ctx.fillStyle = ((((((('rgba(' + str (int (r * 255.0))) + ',') + str (int (g * 255.0))) + ',') + str (int (b * 255.0))) + ',') + str (int (a * 255.0))) + ')';
		self.ctx.fillRect (0, 0, self.width, self.height);
	});},
	get setFPS () {return __get__ (this, function (self, fps) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'fps': var fps = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.fps = fps;
	});},
	get resourceLoaded () {return __get__ (this, function (self, e) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'e': var e = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.loadingResources--;
		e.target.jmssImg.height = e.target.naturalHeight;
		e.target.jmssImg.width = e.target.naturalWidth;
	});},
	get loadImage () {return __get__ (this, function (self, file) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'file': var file = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		if (__in__ (file, self.resources)) {
			return self.resources [file];
		}
		self.loadingResources++;
		var img = document.createElement ('img');
		img.addEventListener ('load', self.resourceLoaded, false);
		img.setAttribute ('src', file);
		var jmssImg = JMSSImage (img);
		img.jmssImg = jmssImg;
		self.resources [file] = jmssImg;
		return jmssImg;
	});},
	get isKeyPressed () {return __get__ (this, function (self, key) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'key': var key = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		return self.py_keys [key];
	});},
	get isMousePressed () {return __get__ (this, function (self, button) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'button': var button = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		return self.mouse_buttons == button;
	});},
	get getMousePos () {return __get__ (this, function (self) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		if (self.mouse_pos !== null) {
			return self.mouse_pos;
		}
		else {
			return tuple ([0, 0]);
		}
	});},
	get _convY () {return __get__ (this, function (self, y) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'y': var y = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		return self.height - y;
	});},
	get _convColor () {return __get__ (this, function (self, c) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'c': var c = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		return tuple ([int (c [0] * 255.0), int (c [1] * 255.0), int (c [2] * 255.0), int (c [3] * 255.0)]);
	});},
	get loadSound () {return __get__ (this, function (self, filename, streaming) {
		if (typeof streaming == 'undefined' || (streaming != null && streaming.hasOwnProperty ("__kwargtrans__"))) {;
			var streaming = false;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'filename': var filename = __allkwargs0__ [__attrib0__]; break;
						case 'streaming': var streaming = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		var howl = window.Howl;
		return new howl (dict ({'src': list ([filename])}));
	});},
	get playSound () {return __get__ (this, function (self, sound, loop) {
		if (typeof loop == 'undefined' || (loop != null && loop.hasOwnProperty ("__kwargtrans__"))) {;
			var loop = false;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'sound': var sound = __allkwargs0__ [__attrib0__]; break;
						case 'loop': var loop = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		sound.loop = loop;
		sound.play ();
	});},
	get pauseSound () {return __get__ (this, function (self, sound) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'sound': var sound = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		if (__in__ (sound, self.soundPlayers)) {
			self.soundPlayers [sound].pause ();
		}
	});},
	get drawText () {return __get__ (this, function (self, text, x, y, fontName, fontSize, color, anchorX, anchorY) {
		if (typeof fontName == 'undefined' || (fontName != null && fontName.hasOwnProperty ("__kwargtrans__"))) {;
			var fontName = 'Arial';
		};
		if (typeof fontSize == 'undefined' || (fontSize != null && fontSize.hasOwnProperty ("__kwargtrans__"))) {;
			var fontSize = 10;
		};
		if (typeof color == 'undefined' || (color != null && color.hasOwnProperty ("__kwargtrans__"))) {;
			var color = tuple ([1, 1, 1, 1]);
		};
		if (typeof anchorX == 'undefined' || (anchorX != null && anchorX.hasOwnProperty ("__kwargtrans__"))) {;
			var anchorX = 'left';
		};
		if (typeof anchorY == 'undefined' || (anchorY != null && anchorY.hasOwnProperty ("__kwargtrans__"))) {;
			var anchorY = 'bottom';
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'text': var text = __allkwargs0__ [__attrib0__]; break;
						case 'x': var x = __allkwargs0__ [__attrib0__]; break;
						case 'y': var y = __allkwargs0__ [__attrib0__]; break;
						case 'fontName': var fontName = __allkwargs0__ [__attrib0__]; break;
						case 'fontSize': var fontSize = __allkwargs0__ [__attrib0__]; break;
						case 'color': var color = __allkwargs0__ [__attrib0__]; break;
						case 'anchorX': var anchorX = __allkwargs0__ [__attrib0__]; break;
						case 'anchorY': var anchorY = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		if (self.loadingResources > 0) {
			return ;
		}
		self.ctx.fillStyle = ((((((('rgba(' + str (int (color [0] * 255.0))) + ',') + str (int (color [1] * 255.0))) + ',') + str (int (color [2] * 255.0))) + ',') + str (int (color [3] * 255.0))) + ')';
		self.ctx.font = (str (fontSize) + 'pt ') + fontName;
		self.ctx.textBaseline = 'bottom';
		self.ctx.fillText (text, x, self.height - y);
	});},
	get drawImage () {return __get__ (this, function (self, image, x, y, width, height, rotation, anchorX, anchorY, opacity, rect) {
		if (typeof width == 'undefined' || (width != null && width.hasOwnProperty ("__kwargtrans__"))) {;
			var width = null;
		};
		if (typeof height == 'undefined' || (height != null && height.hasOwnProperty ("__kwargtrans__"))) {;
			var height = null;
		};
		if (typeof rotation == 'undefined' || (rotation != null && rotation.hasOwnProperty ("__kwargtrans__"))) {;
			var rotation = 0;
		};
		if (typeof anchorX == 'undefined' || (anchorX != null && anchorX.hasOwnProperty ("__kwargtrans__"))) {;
			var anchorX = null;
		};
		if (typeof anchorY == 'undefined' || (anchorY != null && anchorY.hasOwnProperty ("__kwargtrans__"))) {;
			var anchorY = null;
		};
		if (typeof opacity == 'undefined' || (opacity != null && opacity.hasOwnProperty ("__kwargtrans__"))) {;
			var opacity = null;
		};
		if (typeof rect == 'undefined' || (rect != null && rect.hasOwnProperty ("__kwargtrans__"))) {;
			var rect = null;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'image': var image = __allkwargs0__ [__attrib0__]; break;
						case 'x': var x = __allkwargs0__ [__attrib0__]; break;
						case 'y': var y = __allkwargs0__ [__attrib0__]; break;
						case 'width': var width = __allkwargs0__ [__attrib0__]; break;
						case 'height': var height = __allkwargs0__ [__attrib0__]; break;
						case 'rotation': var rotation = __allkwargs0__ [__attrib0__]; break;
						case 'anchorX': var anchorX = __allkwargs0__ [__attrib0__]; break;
						case 'anchorY': var anchorY = __allkwargs0__ [__attrib0__]; break;
						case 'opacity': var opacity = __allkwargs0__ [__attrib0__]; break;
						case 'rect': var rect = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		if (isinstance (image, str)) {
			var image = self.loadImage (image);
		}
		if (self.loadingResources > 0) {
			return ;
		}
		self.ctx.save ();
		if (opacity !== null) {
			self.ctx.globalAlpha = opacity;
			self.ctx.drawImage (image.img, x, self._convY (y + image.height));
			self.ctx.restore ();
		}
		else {
			self.ctx.drawImage (image.img, x, self._convY (y + image.height));
		}
	});},
	get drawCircle () {return __get__ (this, function (self, color, pos, radius, width) {
		if (typeof width == 'undefined' || (width != null && width.hasOwnProperty ("__kwargtrans__"))) {;
			var width = 0;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'color': var color = __allkwargs0__ [__attrib0__]; break;
						case 'pos': var pos = __allkwargs0__ [__attrib0__]; break;
						case 'radius': var radius = __allkwargs0__ [__attrib0__]; break;
						case 'width': var width = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		// pass;
	});},
	get drawPixel () {return __get__ (this, function (self, pos, color) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'pos': var pos = __allkwargs0__ [__attrib0__]; break;
						case 'color': var color = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		// pass;
	});},
	get drawLine () {return __get__ (this, function (self, x1, y1, x2, y2, r, g, b, a, width) {
		if (typeof r == 'undefined' || (r != null && r.hasOwnProperty ("__kwargtrans__"))) {;
			var r = 1.0;
		};
		if (typeof g == 'undefined' || (g != null && g.hasOwnProperty ("__kwargtrans__"))) {;
			var g = 1.0;
		};
		if (typeof b == 'undefined' || (b != null && b.hasOwnProperty ("__kwargtrans__"))) {;
			var b = 1.0;
		};
		if (typeof a == 'undefined' || (a != null && a.hasOwnProperty ("__kwargtrans__"))) {;
			var a = 1.0;
		};
		if (typeof width == 'undefined' || (width != null && width.hasOwnProperty ("__kwargtrans__"))) {;
			var width = 1;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'x1': var x1 = __allkwargs0__ [__attrib0__]; break;
						case 'y1': var y1 = __allkwargs0__ [__attrib0__]; break;
						case 'x2': var x2 = __allkwargs0__ [__attrib0__]; break;
						case 'y2': var y2 = __allkwargs0__ [__attrib0__]; break;
						case 'r': var r = __allkwargs0__ [__attrib0__]; break;
						case 'g': var g = __allkwargs0__ [__attrib0__]; break;
						case 'b': var b = __allkwargs0__ [__attrib0__]; break;
						case 'a': var a = __allkwargs0__ [__attrib0__]; break;
						case 'width': var width = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		self.ctx.beginPath ();
		self.ctx.lineWidth = width;
		self.ctx.strokeStyle = ((((((('rgba(' + str (int (r * 255.0))) + ',') + str (int (g * 255.0))) + ',') + str (int (b * 255.0))) + ',') + str (int (a * 255.0))) + ')';
		self.ctx.moveTo (x1, self._convY (y1));
		self.ctx.lineTo (x2, self._convY (y2));
		self.ctx.stroke ();
	});},
	get drawRect () {return __get__ (this, function (self, x1, y1, x2, y2, r, g, b, a) {
		if (typeof r == 'undefined' || (r != null && r.hasOwnProperty ("__kwargtrans__"))) {;
			var r = 1.0;
		};
		if (typeof g == 'undefined' || (g != null && g.hasOwnProperty ("__kwargtrans__"))) {;
			var g = 1.0;
		};
		if (typeof b == 'undefined' || (b != null && b.hasOwnProperty ("__kwargtrans__"))) {;
			var b = 1.0;
		};
		if (typeof a == 'undefined' || (a != null && a.hasOwnProperty ("__kwargtrans__"))) {;
			var a = 1.0;
		};
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'self': var self = __allkwargs0__ [__attrib0__]; break;
						case 'x1': var x1 = __allkwargs0__ [__attrib0__]; break;
						case 'y1': var y1 = __allkwargs0__ [__attrib0__]; break;
						case 'x2': var x2 = __allkwargs0__ [__attrib0__]; break;
						case 'y2': var y2 = __allkwargs0__ [__attrib0__]; break;
						case 'r': var r = __allkwargs0__ [__attrib0__]; break;
						case 'g': var g = __allkwargs0__ [__attrib0__]; break;
						case 'b': var b = __allkwargs0__ [__attrib0__]; break;
						case 'a': var a = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		var ctx = self.ctx;
		ctx.fillStyle = ((((((('rgba(' + str (int (r * 255.0))) + ',') + str (int (g * 255.0))) + ',') + str (int (b * 255.0))) + ',') + str (int (a * 255.0))) + ')';
		ctx.beginPath ();
		ctx.moveTo (x1, y1);
		ctx.lineTo (x2, y1);
		ctx.lineTo (x2, y2);
		ctx.lineTo (x1, y2);
		ctx.closePath ();
		ctx.fill ();
	});}
});

//# sourceMappingURL=JMSSGraphics.map