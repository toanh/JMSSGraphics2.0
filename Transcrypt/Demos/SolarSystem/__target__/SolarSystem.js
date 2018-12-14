// Transcrypt'ed from Python, 2018-12-14 21:28:22
var math = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_math__ from './math.js';
__nest__ (math, '', __module_math__);
var __name__ = '__main__';
export var SolarSystem =  __class__ ('SolarSystem', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self) {
		self.sun = new Image ();
		self.moon = new Image ();
		self.earth = new Image ();
		self.sun.src = 'https://mdn.mozillademos.org/files/1456/Canvas_sun.png';
		if (self.sun.naturalWidth == 'undefined' || self.sun.naturalWidth == 0) {
			self.sun.src = 'Canvas_sun.png';
		}
		self.moon.src = 'https://mdn.mozillademos.org/files/1443/Canvas_moon.png';
		if (self.moon.naturalWidth == 'undefined' || self.moon.naturalWidth == 0) {
			self.moon.src = 'Canvas_moon.png';
		}
		self.earth.src = 'https://mdn.mozillademos.org/files/1429/Canvas_earth.png';
		if (self.earth.naturalWidth == 'undefined' || self.earth.naturalWidth == 0) {
			self.earth.src = 'Canvas_earth.png';
		}
		self.Keys = dict ({'SPACE': 32, 'LEFT': 37, 'UP': 38, 'RIGHT': 39, 'DOWN': 40});
		self.accel_value = 1.0;
		self.accelerate = 1.0;
		self.keyCode = -(1);
		document.onkeypress = self.keyHandler;
		self.paused = false;
		self.main_loop ();
	});},
	get render () {return __get__ (this, function (self) {
		self.ctx = document.getElementById ('canvas').getContext ('2d');
		self.ctx.globalCompositeOperation = 'destination-over';
		self.ctx.clearRect (0, 0, 300, 300);
		self.ctx.fillStyle = 'rgba(0, 0, 0, 0.4)';
		self.ctx.strokeStyle = 'rgba(0, 153, 255, 0.4)';
		self.ctx.save ();
		self.ctx.translate (150, 150);
		self.time = new Date ();
		var secs = self.time.getSeconds ();
		var msecs = self.time.getMilliseconds ();
		self.ctx.rotate ((((2 * math.pi) / 60) * self.accelerate) * secs + (((2 * math.pi) / 60000) * self.accelerate) * msecs);
		self.ctx.translate (105, 0);
		self.ctx.fillRect (0, -(12), 50, 24);
		self.ctx.drawImage (self.earth, -(12), -(12));
		self.ctx.save ();
		self.ctx.rotate ((((2 * math.pi) / 6) * self.accelerate) * secs + (((2 * math.pi) / 6000) * self.accelerate) * msecs);
		self.ctx.translate (0, 28.5);
		self.ctx.drawImage (self.moon, -(3.5), -(3.5));
		self.ctx.restore ();
		self.ctx.restore ();
		self.ctx.beginPath ();
		self.ctx.arc (150, 150, 105, 0, math.pi * 2, false);
		self.ctx.stroke ();
		self.ctx.font = '20px Arial';
		self.ctx.fillStyle = 'white';
		self.ctx.fillText ('Accel:' + str (self.accelerate), 10, 20);
		self.ctx.drawImage (self.sun, 0, 0, 300, 300);
		self.main_loop ();
	});},
	get pause () {return __get__ (this, function (self) {
		self.paused = !(self.paused);
		if (self.paused) {
			document.getElementById ('info').innerHTML = '<b>Game stopped</b>';
		}
		else {
			document.getElementById ('info').innerHTML = '<b>Game running</b>';
		}
	});},
	get keyHandler () {return __get__ (this, function (self, e) {
		self.keyCode = e.keyCode;
		self.charCode = e.charCode;
		console.log ((('keyCode: ' + str (self.keyCode)) + ' charCode: ') + str (self.charCode));
	});},
	get accel () {return __get__ (this, function (self) {
		self.accelerate += self.accel_value;
	});},
	get slowdown () {return __get__ (this, function (self) {
		self.accelerate -= self.accel_value;
	});},
	get user_input () {return __get__ (this, function (self) {
		if (self.keyCode == self.Keys ['RIGHT']) {
			self.accelerate += self.accel_value;
		}
		else if (self.keyCode == self.Keys ['LEFT']) {
			self.accelerate -= self.accel_value;
		}
		self.keyCode = -(1);
	});},
	get main_loop () {return __get__ (this, function (self) {
		self.user_input ();
		if (!(self.paused)) {
			self.animate = window.requestAnimationFrame (self.render);
		}
		else {
			setTimeout (self.main_loop, 50);
		}
	});}
});
export var solarSystem = SolarSystem ();

//# sourceMappingURL=SolarSystem.map