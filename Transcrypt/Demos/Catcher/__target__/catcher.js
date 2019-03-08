// Transcrypt'ed from Python, 2018-12-17 22:43:42
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {_array, _bitmask1, _bitmask2, _bitmask3, _fill_array, _index, _random_integer, choice, randint, random, seed, shuffle} from './random.js';
import {IsColliding} from './collision.js';
import {Graphics, JMSSImage, KEY_A, KEY_AMPERSAND, KEY_APOSTROPHE, KEY_ASCIICIRCUM, KEY_ASCIITILDE, KEY_ASTERISK, KEY_AT, KEY_B, KEY_BACKSLASH, KEY_BACKSPACE, KEY_BAR, KEY_BEGIN, KEY_BRACELEFT, KEY_BRACERIGHT, KEY_BRACKETLEFT, KEY_BRACKETRIGHT, KEY_BREAK, KEY_C, KEY_CANCEL, KEY_CAPSLOCK, KEY_CLEAR, KEY_COLON, KEY_COMMA, KEY_D, KEY_DELETE, KEY_DOLLAR, KEY_DOUBLEQUOTE, KEY_DOWN, KEY_E, KEY_END, KEY_ENTER, KEY_EQUAL, KEY_ESCAPE, KEY_EXCLAMATION, KEY_EXECUTE, KEY_F, KEY_F1, KEY_F10, KEY_F11, KEY_F12, KEY_F13, KEY_F14, KEY_F15, KEY_F16, KEY_F17, KEY_F18, KEY_F19, KEY_F2, KEY_F20, KEY_F3, KEY_F4, KEY_F5, KEY_F6, KEY_F7, KEY_F8, KEY_F9, KEY_FIND, KEY_FUNCTION, KEY_G, KEY_GRAVE, KEY_GREATER, KEY_H, KEY_HASH, KEY_HELP, KEY_HOME, KEY_I, KEY_INSERT, KEY_J, KEY_K, KEY_KEY_SPACE, KEY_L, KEY_LALT, KEY_LCOMMAND, KEY_LCTRL, KEY_LEFT, KEY_LESS, KEY_LINEFEED, KEY_LMETA, KEY_LOPTION, KEY_LSHIFT, KEY_LWINDOWS, KEY_M, KEY_MENU, KEY_MINUS, KEY_MODESWITCH, KEY_MOTION_BACKSPACE, KEY_MOTION_BEGINNING_OF_FILE, KEY_MOTION_BEGINNING_OF_LINE, KEY_MOTION_DELETE, KEY_MOTION_DOWN, KEY_MOTION_END_OF_FILE, KEY_MOTION_END_OF_LINE, KEY_MOTION_LEFT, KEY_MOTION_NEXT_PAGE, KEY_MOTION_NEXT_WORD, KEY_MOTION_PREVIOUS_PAGE, KEY_MOTION_PREVIOUS_WORD, KEY_MOTION_RIGHT, KEY_MOTION_UP, KEY_N, KEY_NUMLOCK, KEY_NUM_0, KEY_NUM_1, KEY_NUM_2, KEY_NUM_3, KEY_NUM_4, KEY_NUM_5, KEY_NUM_6, KEY_NUM_7, KEY_NUM_8, KEY_NUM_9, KEY_NUM_ADD, KEY_NUM_BEGIN, KEY_NUM_DECIMAL, KEY_NUM_DELETE, KEY_NUM_DIVIDE, KEY_NUM_DOWN, KEY_NUM_END, KEY_NUM_ENTER, KEY_NUM_EQUAL, KEY_NUM_F1, KEY_NUM_F2, KEY_NUM_F3, KEY_NUM_F4, KEY_NUM_HOME, KEY_NUM_INSERT, KEY_NUM_LEFT, KEY_NUM_MULTIPLY, KEY_NUM_NEXT, KEY_NUM_PAGE_DOWN, KEY_NUM_PAGE_UP, KEY_NUM_PRIOR, KEY_NUM_RIGHT, KEY_NUM_SEPARATOR, KEY_NUM_SPACE, KEY_NUM_SUBTRACT, KEY_NUM_TAB, KEY_NUM_UP, KEY_O, KEY_P, KEY_PAGEDOWN, KEY_PAGEUP, KEY_PARENLEFT, KEY_PARENRIGHT, KEY_PAUSE, KEY_PERCENT, KEY_PERIOD, KEY_PLUS, KEY_POUND, KEY_PRINT, KEY_Q, KEY_QUESTION, KEY_QUOTELEFT, KEY_R, KEY_RALT, KEY_RCOMMAND, KEY_RCTRL, KEY_REDO, KEY_RETURN, KEY_RIGHT, KEY_RMETA, KEY_ROPTION, KEY_RSHIFT, KEY_RWINDOWS, KEY_S, KEY_SCRIPTSWITCH, KEY_SCROLLLOCK, KEY_SELECT, KEY_SEMICOLON, KEY_SLASH, KEY_SPACE, KEY_SYSREQ, KEY_T, KEY_TAB, KEY_U, KEY_UNDERSCORE, KEY_UNDO, KEY_UP, KEY_V, KEY_W, KEY_X, KEY_Y, KEY_Z, KEY__0, KEY__1, KEY__2, KEY__3, KEY__4, KEY__5, KEY__6, KEY__7, KEY__8, KEY__9, MOUSE_BUTTON_LEFT, MOUSE_BUTTON_MIDDLE, MOUSE_BUTTON_NONE, MOUSE_BUTTON_RIGHT} from './JMSSGraphics.js';
var __name__ = '__main__';
export var game = Graphics (640, 480);
export var star_x = randint (0, 640 - 20);
export var star_y = 470;
export var star_speed = 2;
export var paddle_x = 0;
export var paddle_y = 0;
export var score = 0;
export var main = game.mainloop (function () {
	star_y -= star_speed;
	if (game.isKeyPressed (KEY_A)) {
		paddle_x -= 3;
	}
	if (game.isKeyPressed (KEY_D)) {
		paddle_x += 3;
	}
	if (IsColliding (paddle_x, paddle_y, 80, 16, star_x, star_y, 20, 20)) {
		star_y = 470;
		star_x = randint (0, 640 - 20);
		score++;
		star_speed += 0.05;
	}
	if (star_y < -(20)) {
		game.py_clear ();
		game.drawText ('GAME OVER!!', 200, 240, __kwargtrans__ ({fontSize: 30}));
	}
	else {
		game.py_clear ();
		game.drawImage ('star.gif', star_x, star_y);
		game.drawImage ('paddle.gif', paddle_x, paddle_y);
		game.drawText ('Score: ' + str (score), 280, 440, __kwargtrans__ ({fontSize: 20}));
	}
});
game.run ();

//# sourceMappingURL=catcher.map