// Transcrypt'ed from Python, 2018-12-15 20:12:40
var math = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_math__ from './math.js';
__nest__ (math, '', __module_math__);
import {_array, _bitmask1, _bitmask2, _bitmask3, _fill_array, _index, _random_integer, choice, randint, random, seed, shuffle} from './random.js';
import {Graphics, JMSSImage, KEY_A, KEY_AMPERSAND, KEY_APOSTROPHE, KEY_ASCIICIRCUM, KEY_ASCIITILDE, KEY_ASTERISK, KEY_AT, KEY_B, KEY_BACKSLASH, KEY_BACKSPACE, KEY_BAR, KEY_BEGIN, KEY_BRACELEFT, KEY_BRACERIGHT, KEY_BRACKETLEFT, KEY_BRACKETRIGHT, KEY_BREAK, KEY_C, KEY_CANCEL, KEY_CAPSLOCK, KEY_CLEAR, KEY_COLON, KEY_COMMA, KEY_D, KEY_DELETE, KEY_DOLLAR, KEY_DOUBLEQUOTE, KEY_DOWN, KEY_E, KEY_END, KEY_ENTER, KEY_EQUAL, KEY_ESCAPE, KEY_EXCLAMATION, KEY_EXECUTE, KEY_F, KEY_F1, KEY_F10, KEY_F11, KEY_F12, KEY_F13, KEY_F14, KEY_F15, KEY_F16, KEY_F17, KEY_F18, KEY_F19, KEY_F2, KEY_F20, KEY_F3, KEY_F4, KEY_F5, KEY_F6, KEY_F7, KEY_F8, KEY_F9, KEY_FIND, KEY_FUNCTION, KEY_G, KEY_GRAVE, KEY_GREATER, KEY_H, KEY_HASH, KEY_HELP, KEY_HOME, KEY_I, KEY_INSERT, KEY_J, KEY_K, KEY_KEY_SPACE, KEY_L, KEY_LALT, KEY_LCOMMAND, KEY_LCTRL, KEY_LEFT, KEY_LESS, KEY_LINEFEED, KEY_LMETA, KEY_LOPTION, KEY_LSHIFT, KEY_LWINDOWS, KEY_M, KEY_MENU, KEY_MINUS, KEY_MODESWITCH, KEY_MOTION_BACKSPACE, KEY_MOTION_BEGINNING_OF_FILE, KEY_MOTION_BEGINNING_OF_LINE, KEY_MOTION_DELETE, KEY_MOTION_DOWN, KEY_MOTION_END_OF_FILE, KEY_MOTION_END_OF_LINE, KEY_MOTION_LEFT, KEY_MOTION_NEXT_PAGE, KEY_MOTION_NEXT_WORD, KEY_MOTION_PREVIOUS_PAGE, KEY_MOTION_PREVIOUS_WORD, KEY_MOTION_RIGHT, KEY_MOTION_UP, KEY_N, KEY_NUMLOCK, KEY_NUM_0, KEY_NUM_1, KEY_NUM_2, KEY_NUM_3, KEY_NUM_4, KEY_NUM_5, KEY_NUM_6, KEY_NUM_7, KEY_NUM_8, KEY_NUM_9, KEY_NUM_ADD, KEY_NUM_BEGIN, KEY_NUM_DECIMAL, KEY_NUM_DELETE, KEY_NUM_DIVIDE, KEY_NUM_DOWN, KEY_NUM_END, KEY_NUM_ENTER, KEY_NUM_EQUAL, KEY_NUM_F1, KEY_NUM_F2, KEY_NUM_F3, KEY_NUM_F4, KEY_NUM_HOME, KEY_NUM_INSERT, KEY_NUM_LEFT, KEY_NUM_MULTIPLY, KEY_NUM_NEXT, KEY_NUM_PAGE_DOWN, KEY_NUM_PAGE_UP, KEY_NUM_PRIOR, KEY_NUM_RIGHT, KEY_NUM_SEPARATOR, KEY_NUM_SPACE, KEY_NUM_SUBTRACT, KEY_NUM_TAB, KEY_NUM_UP, KEY_O, KEY_P, KEY_PAGEDOWN, KEY_PAGEUP, KEY_PARENLEFT, KEY_PARENRIGHT, KEY_PAUSE, KEY_PERCENT, KEY_PERIOD, KEY_PLUS, KEY_POUND, KEY_PRINT, KEY_Q, KEY_QUESTION, KEY_QUOTELEFT, KEY_R, KEY_RALT, KEY_RCOMMAND, KEY_RCTRL, KEY_REDO, KEY_RETURN, KEY_RIGHT, KEY_RMETA, KEY_ROPTION, KEY_RSHIFT, KEY_RWINDOWS, KEY_S, KEY_SCRIPTSWITCH, KEY_SCROLLLOCK, KEY_SELECT, KEY_SEMICOLON, KEY_SLASH, KEY_SPACE, KEY_SYSREQ, KEY_T, KEY_TAB, KEY_U, KEY_UNDERSCORE, KEY_UNDO, KEY_UP, KEY_V, KEY_W, KEY_X, KEY_Y, KEY_Z, KEY__0, KEY__1, KEY__2, KEY__3, KEY__4, KEY__5, KEY__6, KEY__7, KEY__8, KEY__9, MOUSE_BUTTON_LEFT, MOUSE_BUTTON_MIDDLE, MOUSE_BUTTON_NONE, MOUSE_BUTTON_RIGHT} from './JMSSGraphics.js';
var __name__ = '__main__';
export var Entity =  __class__ ('Entity', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, filename) {
		if (isinstance (filename, str)) {
			self.image = jmss.loadImage (filename);
		}
		else {
			self.image = filename;
		}
		self.x = 0;
		self.y = 0;
		self.xdir = 0;
		self.ydir = 0;
		self.width = self.image.width;
		self.height = self.image.height;
		self.opacity = null;
	});},
	get Draw () {return __get__ (this, function (self) {
		jmss.drawImage (self.image, self.x, self.y, __kwargtrans__ ({opacity: self.opacity}));
	});},
	get Update () {return __get__ (this, function (self) {
		self.x += self.xdir;
		self.y += self.ydir;
	});}
});
export var Paddle =  __class__ ('Paddle', [Entity], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, filename, gunfilename, upKey, downKey, fireKey, lives, fireDir) {
		__super__ (Paddle, '__init__') (self, filename);
		self.up = upKey;
		self.down = downKey;
		self.fire = fireKey;
		self.lives = lives;
		self.fireDir = fireDir;
		self.coolDown = 40;
		self.timer = 0;
		self.gun = jmss.loadImage (gunfilename);
	});},
	get Draw () {return __get__ (this, function (self) {
		__super__ (Paddle, 'Draw') (self);
		if (self.fireDir > 0) {
			jmss.drawImage (self.gun, self.x, (self.y + self.image.height / 2) - self.gun.height / 2);
		}
		else {
			jmss.drawImage (self.gun, self.x - self.gun.width / 2, (self.y + self.image.height / 2) - self.gun.height / 2);
		}
	});},
	get Update () {return __get__ (this, function (self) {
		self.timer--;
		if (self.timer < 0) {
			self.timer = 0;
		}
		self.ydir *= 0.9;
		if (jmss.isKeyPressed (self.up)) {
			self.ydir += 0.5;
			if (self.ydir >= 3) {
				self.ydir = 3;
			}
		}
		if (jmss.isKeyPressed (self.down)) {
			self.ydir -= 0.5;
			if (self.ydir <= -(3)) {
				self.ydir = -(3);
			}
		}
		if (jmss.isKeyPressed (self.fire) && self.timer == 0) {
			self.timer = self.coolDown;
			if (self.fireDir > 0) {
				game.SpawnBullet (self.x + self.gun.width / 2, self.y + self.height / 2, self.fireDir * 10, self);
			}
			else {
				game.SpawnBullet (self.x - self.gun.width / 2, self.y + self.height / 2, self.fireDir * 10, self);
			}
		}
		__super__ (Paddle, 'Update') (self);
	});}
});
export var Ball =  __class__ ('Ball', [Entity], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, filename, respawnable) {
		if (typeof respawnable == 'undefined' || (respawnable != null && respawnable.hasOwnProperty ("__kwargtrans__"))) {;
			var respawnable = true;
		};
		__super__ (Ball, '__init__') (self, filename);
		self.respawnable = respawnable;
		self.opacity = 0.5;
	});},
	get Update () {return __get__ (this, function (self) {
		self.opacity += 0.01;
		if (self.opacity >= 1.0) {
			self.opacity = 1.0;
		}
		if (abs (self.xdir) >= 5) {
			self.xdir = (self.xdir / abs (self.xdir)) * 5;
		}
		__super__ (Ball, 'Update') (self);
	});}
});
export var Bullet =  __class__ ('Bullet', [Entity], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, filename, owner) {
		self.owner = owner;
		__super__ (Bullet, '__init__') (self, filename);
	});}
});
export var Game =  __class__ ('Game', [object], {
	__module__: __name__,
	get SpawnBall () {return __get__ (this, function (self, x, y, xdir, ydir, filename, respawnable) {
		if (typeof xdir == 'undefined' || (xdir != null && xdir.hasOwnProperty ("__kwargtrans__"))) {;
			var xdir = null;
		};
		if (typeof ydir == 'undefined' || (ydir != null && ydir.hasOwnProperty ("__kwargtrans__"))) {;
			var ydir = null;
		};
		if (typeof filename == 'undefined' || (filename != null && filename.hasOwnProperty ("__kwargtrans__"))) {;
			var filename = 'ball.png';
		};
		if (typeof respawnable == 'undefined' || (respawnable != null && respawnable.hasOwnProperty ("__kwargtrans__"))) {;
			var respawnable = true;
		};
		var ball = Ball (filename, respawnable);
		ball.x = x;
		ball.y = y;
		if (xdir === null) {
			ball.xdir = (random () - 0.5) * 2;
			if (ball.xdir < 0) {
				ball.xdir -= 2;
			}
			else {
				ball.xdir += 2;
			}
		}
		else {
			ball.xdir = xdir;
		}
		if (ydir === null) {
			ball.ydir = (random () - 0.5) * 2;
			if (ball.ydir < 0) {
				ball.ydir -= 2;
			}
			else {
				ball.ydir += 2;
			}
		}
		else {
			ball.ydir = ydir;
		}
		self.balls.append (ball);
	});},
	get drawTriangleList () {return __get__ (this, function (self, triList) {
		var colour = list ([1, 1, 1]);
		for (var i = 0; i < len (triList); i += 3) {
			jmss.drawLine (triList [i] [0], triList [i] [1], triList [i + 1] [0], triList [i + 1] [1], __kwargtrans__ ({r: colour [0], g: colour [1], b: colour [2]}));
			jmss.drawLine (triList [i + 1] [0], triList [i + 1] [1], triList [i + 2] [0], triList [i + 2] [1], __kwargtrans__ ({r: colour [0], g: colour [1], b: colour [2]}));
			jmss.drawLine (triList [i + 2] [0], triList [i + 2] [1], triList [i] [0], triList [i] [1], __kwargtrans__ ({r: colour [0], g: colour [1], b: colour [2]}));
		}
	});},
	get rotateTransform () {return __get__ (this, function (self, triList3D, angle) {
		var transformedList = list ([]);
		for (var vertex of triList3D) {
			var x = vertex [0] * math.cos (angle) - vertex [2] * math.sin (angle);
			var y = vertex [1];
			var z = vertex [0] * math.sin (angle) + vertex [2] * math.cos (angle);
			var newTri = tuple ([x, y, z]);
			transformedList.append (newTri);
		}
		return transformedList;
	});},
	get translateTransform () {return __get__ (this, function (self, triList3D, cameraPos) {
		var transformedList = list ([]);
		for (var i = 0; i < len (triList3D); i++) {
			var newTri = tuple ([triList3D [i] [0] - cameraPos [0], triList3D [i] [1] - cameraPos [1], triList3D [i] [2] - cameraPos [2]]);
			transformedList.append (newTri);
		}
		return transformedList;
	});},
	get perspectiveTransform () {return __get__ (this, function (self, triList3D) {
		var triList2D = list ([]);
		for (var i = 0; i < len (triList3D); i++) {
			var newTri = tuple ([triList3D [i] [0] / triList3D [i] [2], triList3D [i] [1] / triList3D [i] [2]]);
			triList2D.append (newTri);
		}
		return triList2D;
	});},
	get viewportTransform () {return __get__ (this, function (self, triList2D, width, height) {
		var transformedList = list ([]);
		for (var vertex of triList2D) {
			var x = (vertex [0] + 0.6) * width;
			var y = (vertex [1] + 0.5) * height;
			var newTri = tuple ([x, y]);
			transformedList.append (newTri);
		}
		return transformedList;
	});},
	get SpawnBullet () {return __get__ (this, function (self, x, y, xdir, owner) {
		if (owner == self.p1) {
			var bullet = Bullet (self.bullet_red_image, owner);
		}
		else {
			var bullet = Bullet (self.bullet_blue_image, owner);
		}
		bullet.x = x;
		bullet.y = y - bullet.image.height / 2;
		bullet.xdir = xdir;
		bullet.ydir = 0;
		self.bullets.append (bullet);
	});},
	get ResetGame () {return __get__ (this, function (self) {
		self.balls = list ([]);
		self.bullets = list ([]);
		self.p1.xdir = 0;
		self.p1.ydir = 0;
		self.p1.x = 0;
		self.p1.y = 100;
		self.p1.lives = 3;
		self.p2.xdir = 0;
		self.p2.ydir = 0;
		self.p2.x = 600 - 24;
		self.p2.y = 100;
		self.p2.lives = 3;
		self.SpawnBall (300, 200, __kwargtrans__ ({filename: self.ball_green_image}));
	});},
	get __init__ () {return __get__ (this, function (self) {
		self.balls = list ([]);
		self.bullets = list ([]);
		var paddle1 = Paddle ('paddle_red.png', 'gun_left.png', KEY_W, KEY_S, KEY_D, 3, 1);
		paddle1.xdir = 0;
		paddle1.ydir = 0;
		paddle1.x = 0;
		paddle1.y = 100;
		self.p1 = paddle1;
		var paddle2 = Paddle ('paddle_blue.png', 'gun_right.png', KEY_UP, KEY_DOWN, KEY_LEFT, 3, -(1));
		paddle2.xdir = 0;
		paddle2.ydir = 0;
		paddle2.x = 600 - 24;
		paddle2.y = 100;
		self.p2 = paddle2;
		self.angle = 0;
		self.camera = list ([0, 1.7, -(8)]);
		self.shape = list ([list ([0, 1, 0]), list ([-(1), -(1), -(1)]), list ([1, -(1), -(1)]), list ([0, 1, 0]), list ([1, -(1), -(1)]), list ([1, -(1), 1]), list ([0, 1, 0]), list ([1, -(1), 1]), list ([-(1), -(1), 1]), list ([0, 1, 0]), list ([-(1), -(1), -(1)]), list ([-(1), -(1), 1])]);
		self.triList = list ([]);
		self.gameState = 0;
		self.title_image = jmss.loadImage ('title.png');
		self.bg_image = jmss.loadImage ('background.png');
		self.bg_x = 0;
		self.blip_sound = jmss.loadSound ('blip.wav', __kwargtrans__ ({streaming: false}));
		self.background_music = jmss.loadSound ('piano.wav', __kwargtrans__ ({streaming: true}));
		self.bullet_red_image = jmss.loadImage ('bullet_red.png');
		self.bullet_blue_image = jmss.loadImage ('bullet_blue.png');
		self.ball_red_image = jmss.loadImage ('ball_red.png');
		self.ball_green_image = jmss.loadImage ('ball.png');
		self.SpawnBall (300, 200, __kwargtrans__ ({filename: self.ball_green_image}));
		jmss.playSound (self.background_music);
	});},
	get Draw () {return __get__ (this, function (self) {
		if (self.gameState == 0) {
			self.DrawTitle ();
		}
		else if (self.gameState == 1) {
			self.DrawGame ();
		}
		else if (self.gameState == 2) {
			self.DrawWin ();
		}
	});},
	get Update () {return __get__ (this, function (self) {
		if (self.gameState == 0) {
			self.UpdateTitle ();
		}
		else if (self.gameState == 1) {
			self.UpdateGame ();
		}
		else if (self.gameState == 2) {
			self.UpdateWin ();
		}
	});},
	get DrawTitle () {return __get__ (this, function (self) {
		jmss.drawImage (self.title_image, 0, 0);
	});},
	get UpdateTitle () {return __get__ (this, function (self) {
		if (jmss.isKeyPressed (KEY_SPACE)) {
			self.gameState = 1;
		}
	});},
	get DrawWin () {return __get__ (this, function (self) {
		jmss.drawImage (self.title_image, 0, 0);
		if (self.p1.lives <= 0) {
			var winner = 2;
		}
		else {
			var winner = 1;
		}
		jmss.drawText (('Player ' + str (winner)) + ' wins!!', 170, 200, __kwargtrans__ ({fontSize: 30}));
	});},
	get UpdateWin () {return __get__ (this, function (self) {
		if (jmss.isKeyPressed (KEY_SPACE)) {
			self.gameState = 1;
			self.ResetGame ();
		}
	});},
	get DrawGame () {return __get__ (this, function (self) {
		jmss.py_clear ();
		self.bg_x--;
		if (self.bg_x <= -(self.bg_image.width) / 2) {
			self.bg_x = 0;
		}
		jmss.drawImage (self.bg_image, self.bg_x, 0);
		self.drawTriangleList (self.triList);
		for (var b of self.bullets) {
			b.Draw ();
		}
		for (var b of self.balls) {
			b.Draw ();
		}
		self.p1.Draw ();
		self.p2.Draw ();
		jmss.drawText ('Lives: ' + str (self.p1.lives), 10, 350, __kwargtrans__ ({fontSize: 20}));
		jmss.drawText ('Lives: ' + str (self.p2.lives), 490, 350, __kwargtrans__ ({fontSize: 20}));
	});},
	get UpdateGame () {return __get__ (this, function (self) {
		if (self.p1.lives <= 0 || self.p2.lives <= 0) {
			self.gameState = 2;
			return ;
		}
		self.angle = self.angle + 0.05;
		self.triList = self.rotateTransform (self.shape, self.angle);
		self.triList = self.translateTransform (self.triList, self.camera);
		self.triList = self.perspectiveTransform (self.triList);
		self.triList = self.viewportTransform (self.triList, 500, 500);
		if (randint (0, 600) < 1) {
			self.SpawnBall (300, 200, __kwargtrans__ ({filename: self.ball_red_image, respawnable: false}));
		}
		for (var b of self.bullets) {
			if (b.x >= 600 || b.x <= -(b.width)) {
				self.bullets.remove (b);
			}
		}
		for (var ball of self.balls) {
			for (var bullet of self.bullets) {
				if (self.Intersects (bullet.x, bullet.y, bullet.x + bullet.width, bullet.y + bullet.height, ball.x, ball.y, ball.x + ball.width, ball.y + ball.height)) {
					if (ball.xdir * bullet.xdir < 0) {
						ball.xdir *= -(1);
						self.bullets.remove (bullet);
						continue;
					}
					else if (ball.xdir * bullet.xdir > 0) {
						ball.xdir += bullet.xdir / 2.0;
						self.bullets.remove (bullet);
						continue;
					}
				}
			}
		}
		for (var b of self.balls) {
			if (self.Intersects (self.p1.x, self.p1.y, self.p1.x + self.p1.width, self.p1.y + self.p1.height, b.x, b.y, b.x + b.width, b.y + b.height)) {
				b.x = self.p1.x + self.p1.width;
				b.xdir *= -(1.05);
				b.ydir *= 1.05;
				jmss.playSound (self.blip_sound);
			}
			if (self.Intersects (self.p2.x, self.p2.y, self.p2.x + self.p2.width, self.p2.y + self.p2.height, b.x, b.y, b.x + b.width, b.y + b.height)) {
				b.x = self.p2.x - b.width;
				b.xdir *= -(1.05);
				b.ydir *= 1.05;
				jmss.playSound (self.blip_sound);
			}
			if (b.y <= 0) {
				b.y = 0;
				b.ydir *= -(1);
			}
			if (b.y >= 400 - b.height) {
				b.y = 400 - b.height;
				b.ydir *= -(1);
			}
		}
		if (self.p1.y + self.p1.height > 400) {
			self.p1.y = 400 - self.p1.height;
			self.p1.ydir *= -(1);
		}
		if (self.p2.y + self.p2.height > 400) {
			self.p2.y = 400 - self.p2.height;
			self.p2.ydir *= -(1);
		}
		if (self.p1.y < 0) {
			self.p1.y = 0;
			self.p1.ydir *= -(1);
		}
		if (self.p2.y < 0) {
			self.p2.y = 0;
			self.p2.ydir *= -(1);
		}
		for (var b of self.balls) {
			b.Update ();
		}
		for (var b of self.bullets) {
			b.Update ();
		}
		self.p1.Update ();
		self.p2.Update ();
		for (var b of self.balls) {
			if (b.x >= 600) {
				self.p2.lives--;
				self.balls.remove (b);
				if (b.respawnable) {
					self.SpawnBall (300, 200, __kwargtrans__ ({filename: self.ball_green_image}));
				}
			}
			if (b.x <= -(b.width)) {
				self.p1.lives--;
				self.balls.remove (b);
				if (b.respawnable) {
					self.SpawnBall (300, 200, __kwargtrans__ ({filename: self.ball_green_image}));
				}
			}
		}
	});},
	get Intersects () {return __get__ (this, function (self, x1, y1, x2, y2, x3, y3, x4, y4) {
		return !(x2 < x3 || x1 > x4 || y2 < y3 || y1 > y4);
	});}
});
export var jmss = Graphics (__kwargtrans__ ({width: 600, height: 400, title: 'Super Pong'}));
export var game = Game ();
export var mainloop = jmss.mainloop (function () {
	game.Update ();
	game.Draw ();
});
jmss.run ();

//# sourceMappingURL=SuperPong.map