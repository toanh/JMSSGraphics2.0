// Transcrypt'ed from Python, 2018-12-16 20:18:34
var math = {};
var random = {};
var time = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_random__ from './random.js';
__nest__ (random, '', __module_random__);
import * as __module_time__ from './time.js';
__nest__ (time, '', __module_time__);
import * as __module_math__ from './math.js';
__nest__ (math, '', __module_math__);
import {Graphics, JMSSImage, KEY_A, KEY_AMPERSAND, KEY_APOSTROPHE, KEY_ASCIICIRCUM, KEY_ASCIITILDE, KEY_ASTERISK, KEY_AT, KEY_B, KEY_BACKSLASH, KEY_BACKSPACE, KEY_BAR, KEY_BEGIN, KEY_BRACELEFT, KEY_BRACERIGHT, KEY_BRACKETLEFT, KEY_BRACKETRIGHT, KEY_BREAK, KEY_C, KEY_CANCEL, KEY_CAPSLOCK, KEY_CLEAR, KEY_COLON, KEY_COMMA, KEY_D, KEY_DELETE, KEY_DOLLAR, KEY_DOUBLEQUOTE, KEY_DOWN, KEY_E, KEY_END, KEY_ENTER, KEY_EQUAL, KEY_ESCAPE, KEY_EXCLAMATION, KEY_EXECUTE, KEY_F, KEY_F1, KEY_F10, KEY_F11, KEY_F12, KEY_F13, KEY_F14, KEY_F15, KEY_F16, KEY_F17, KEY_F18, KEY_F19, KEY_F2, KEY_F20, KEY_F3, KEY_F4, KEY_F5, KEY_F6, KEY_F7, KEY_F8, KEY_F9, KEY_FIND, KEY_FUNCTION, KEY_G, KEY_GRAVE, KEY_GREATER, KEY_H, KEY_HASH, KEY_HELP, KEY_HOME, KEY_I, KEY_INSERT, KEY_J, KEY_K, KEY_KEY_SPACE, KEY_L, KEY_LALT, KEY_LCOMMAND, KEY_LCTRL, KEY_LEFT, KEY_LESS, KEY_LINEFEED, KEY_LMETA, KEY_LOPTION, KEY_LSHIFT, KEY_LWINDOWS, KEY_M, KEY_MENU, KEY_MINUS, KEY_MODESWITCH, KEY_MOTION_BACKSPACE, KEY_MOTION_BEGINNING_OF_FILE, KEY_MOTION_BEGINNING_OF_LINE, KEY_MOTION_DELETE, KEY_MOTION_DOWN, KEY_MOTION_END_OF_FILE, KEY_MOTION_END_OF_LINE, KEY_MOTION_LEFT, KEY_MOTION_NEXT_PAGE, KEY_MOTION_NEXT_WORD, KEY_MOTION_PREVIOUS_PAGE, KEY_MOTION_PREVIOUS_WORD, KEY_MOTION_RIGHT, KEY_MOTION_UP, KEY_N, KEY_NUMLOCK, KEY_NUM_0, KEY_NUM_1, KEY_NUM_2, KEY_NUM_3, KEY_NUM_4, KEY_NUM_5, KEY_NUM_6, KEY_NUM_7, KEY_NUM_8, KEY_NUM_9, KEY_NUM_ADD, KEY_NUM_BEGIN, KEY_NUM_DECIMAL, KEY_NUM_DELETE, KEY_NUM_DIVIDE, KEY_NUM_DOWN, KEY_NUM_END, KEY_NUM_ENTER, KEY_NUM_EQUAL, KEY_NUM_F1, KEY_NUM_F2, KEY_NUM_F3, KEY_NUM_F4, KEY_NUM_HOME, KEY_NUM_INSERT, KEY_NUM_LEFT, KEY_NUM_MULTIPLY, KEY_NUM_NEXT, KEY_NUM_PAGE_DOWN, KEY_NUM_PAGE_UP, KEY_NUM_PRIOR, KEY_NUM_RIGHT, KEY_NUM_SEPARATOR, KEY_NUM_SPACE, KEY_NUM_SUBTRACT, KEY_NUM_TAB, KEY_NUM_UP, KEY_O, KEY_P, KEY_PAGEDOWN, KEY_PAGEUP, KEY_PARENLEFT, KEY_PARENRIGHT, KEY_PAUSE, KEY_PERCENT, KEY_PERIOD, KEY_PLUS, KEY_POUND, KEY_PRINT, KEY_Q, KEY_QUESTION, KEY_QUOTELEFT, KEY_R, KEY_RALT, KEY_RCOMMAND, KEY_RCTRL, KEY_REDO, KEY_RETURN, KEY_RIGHT, KEY_RMETA, KEY_ROPTION, KEY_RSHIFT, KEY_RWINDOWS, KEY_S, KEY_SCRIPTSWITCH, KEY_SCROLLLOCK, KEY_SELECT, KEY_SEMICOLON, KEY_SLASH, KEY_SPACE, KEY_SYSREQ, KEY_T, KEY_TAB, KEY_U, KEY_UNDERSCORE, KEY_UNDO, KEY_UP, KEY_V, KEY_W, KEY_X, KEY_Y, KEY_Z, KEY__0, KEY__1, KEY__2, KEY__3, KEY__4, KEY__5, KEY__6, KEY__7, KEY__8, KEY__9, MOUSE_BUTTON_LEFT, MOUSE_BUTTON_MIDDLE, MOUSE_BUTTON_NONE, MOUSE_BUTTON_RIGHT} from './JMSSGraphics.js';
import {Particle} from './Particle.js';
var __name__ = '__main__';
export var jmss = Graphics (__kwargtrans__ ({width: 800, height: 600, title: 'Flame', fps: 60}));
export var fire_img = jmss.loadImage ('Rocket_Fire2.png');
export var fire2_img = jmss.loadImage ('fire2.png');
export var wood = jmss.loadImage ('wood_campfire.png');
export var rain_img = jmss.loadImage ('rain.png');
export var forest = jmss.loadImage ('forest.jpeg');
export var torch_img = jmss.loadImage ('torch.png');
export var rain_sound = jmss.loadSound ('rain.wav');
jmss.playSound (rain_sound);
export var fire_sound = jmss.loadSound ('crackling-fireplace.wav');
jmss.playSound (fire_sound);
export var fire_list = list ([]);
export var fire_img_list = list ([fire_img, fire2_img]);
export var rain_list = list ([]);
export var torch_fire_list = list ([]);
export var wood_x = 368;
export var fire1_pos_x = 395;
export var fire2_pos_x = 595;
export var fire3_pos_x = 195;
export var torch_x = 780;
export var torch_y = 30;
export var max_fire_y = 140;
export var max_torchfire_y = torch_y + 140;
export var isTorchFire = false;
export var p = 0;
export var Draw = function () {
	jmss.drawImage (forest, __kwargtrans__ ({x: 0, y: 0, width: 800, height: 600}));
	jmss.drawImage (wood, __kwargtrans__ ({x: wood_x, y: 0, width: 100, height: 70}));
	jmss.drawImage (wood, __kwargtrans__ ({x: wood_x + 200, y: 0, width: 100, height: 70}));
	jmss.drawImage (wood, __kwargtrans__ ({x: wood_x - 200, y: 0, width: 100, height: 70}));
};
export var Fire1 = function () {
	p = 0;
	while (p < 5) {
		var fire = Particle ();
		fire.img_number = random.randint (0, 1);
		fire.x = random.randint (fire1_pos_x, fire1_pos_x + 13);
		fire.y = 25;
		fire.vel_x = random.randint (-(1), 1) / 2;
		fire.vel_y = random.randint (1, 4);
		fire.size = random.randint (1, 30);
		fire.opacity = 0.5;
		fire_list.append (fire);
		p++;
	}
	for (var fire of fire_list) {
		fire.y += fire.vel_y;
		fire.x += fire.vel_x;
		fire.size -= 0.2;
		fire.opacity -= 0.01;
		jmss.drawImage (fire_img_list [fire.img_number], __kwargtrans__ ({x: fire.x, y: fire.y, width: fire.size, height: fire.size, opacity: fire.opacity}));
		if (fire.y > max_fire_y) {
			fire_list.remove (fire);
		}
	}
};
export var Fire2 = function () {
	p = 0;
	while (p < 5) {
		var fire = Particle ();
		fire.img_number = random.randint (0, 1);
		fire.x = random.randint (fire2_pos_x, fire2_pos_x + 13);
		fire.y = 25;
		fire.vel_x = random.randint (-(1), 1) / 2;
		fire.vel_y = random.randint (1, 4);
		fire.size = random.randint (1, 30);
		fire.opacity = 0.5;
		fire_list.append (fire);
		p++;
	}
	for (var fire of fire_list) {
		fire.y += fire.vel_y;
		fire.x += fire.vel_x;
		fire.size -= 0.2;
		fire.opacity -= 0.01;
		jmss.drawImage (fire_img_list [fire.img_number], __kwargtrans__ ({x: fire.x, y: fire.y, width: fire.size, height: fire.size, opacity: fire.opacity}));
		if (fire.y > max_fire_y) {
			fire_list.remove (fire);
		}
	}
};
export var Fire3 = function () {
	p = 0;
	while (p < 5) {
		var fire = Particle ();
		fire.img_number = random.randint (0, 1);
		fire.x = random.randint (fire3_pos_x, fire3_pos_x + 13);
		fire.y = 25;
		fire.vel_x = random.randint (-(1), 1) / 2;
		fire.vel_y = random.randint (1, 4);
		fire.size = random.randint (1, 30);
		fire.opacity = 0.5;
		fire_list.append (fire);
		p++;
	}
	for (var fire of fire_list) {
		fire.y += fire.vel_y;
		fire.x += fire.vel_x;
		fire.size -= 0.2;
		fire.opacity -= 0.01;
		jmss.drawImage (fire_img_list [fire.img_number], __kwargtrans__ ({x: fire.x, y: fire.y, width: fire.size, height: fire.size, opacity: fire.opacity}));
		if (fire.y > max_fire_y) {
			fire_list.remove (fire);
		}
	}
};
export var Rain = function () {
	var p = 0;
	while (p < 1) {
		var rain = Particle ();
		rain.img = rain_img;
		rain.x = random.randint (0, 800);
		rain.y = 600;
		rain.vel_y = random.randint (-(15), -(10));
		rain.size = 30;
		rain.opacity = 1;
		rain_list.append (rain);
		p++;
	}
	for (var rain of rain_list) {
		rain.y += rain.vel_y;
		jmss.drawImage (rain.img, __kwargtrans__ ({x: rain.x, y: rain.y, width: rain.size, height: rain.size, opacity: rain.opacity}));
		if (rain.y < 0) {
			rain_list.remove (rain);
		}
	}
};
export var Torch = function () {
	torch_x = jmss.getMousePos () [0];
	torch_y = jmss.getMousePos () [1];
	jmss.drawImage (torch_img, __kwargtrans__ ({x: torch_x, y: torch_y, width: 60, height: 60}));
	if (torch_y < max_fire_y && torch_y > 25 && (torch_x < fire1_pos_x + 13 && torch_x > fire1_pos_x || torch_x < fire2_pos_x + 13 && torch_x > fire2_pos_x || torch_x < fire3_pos_x + 13 && torch_x > fire3_pos_x)) {
		isTorchFire = true;
	}
	if (isTorchFire == true) {
		var p = 0;
		while (p < 5) {
			var fire = Particle ();
			fire.img_number = random.randint (0, 1);
			fire.x = random.randint (torch_x, torch_x + 4);
			fire.y = torch_y + 41;
			fire.vel_x = random.randint (-(1), 1) / 4;
			fire.vel_y = random.randint (1, 4);
			fire.size = random.randint (1, 20);
			fire.opacity = 0.5;
			torch_fire_list.append (fire);
			p++;
		}
		for (var t of torch_fire_list) {
			t.y += t.vel_y;
			t.x += t.vel_x;
			t.size -= 0.2;
			t.opacity -= 0.01;
			jmss.drawImage (fire_img_list [t.img_number], __kwargtrans__ ({x: t.x, y: t.y, width: t.size, height: t.size, opacity: t.opacity}));
			var max_torchfire_y = torch_y + 140;
			if (t.y > max_torchfire_y) {
				torch_fire_list.remove (t);
			}
		}
	}
};
export var Game = jmss.mainloop (function () {
	Draw ();
	Fire1 ();
	Fire2 ();
	Fire3 ();
	Torch ();
	Rain ();
});
jmss.py_clear ();
jmss.run ();

//# sourceMappingURL=dylan.map