// Transcrypt'ed from Python, 2018-12-16 20:18:35
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
var __name__ = 'Particle';
export var Particle =  __class__ ('Particle', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, img, x, y, vel_x, vel_y, acc_x, acc_y, width, height, lifetime, life, opacity) {
		if (typeof img == 'undefined' || (img != null && img.hasOwnProperty ("__kwargtrans__"))) {;
			var img = null;
		};
		if (typeof x == 'undefined' || (x != null && x.hasOwnProperty ("__kwargtrans__"))) {;
			var x = 0;
		};
		if (typeof y == 'undefined' || (y != null && y.hasOwnProperty ("__kwargtrans__"))) {;
			var y = 0;
		};
		if (typeof vel_x == 'undefined' || (vel_x != null && vel_x.hasOwnProperty ("__kwargtrans__"))) {;
			var vel_x = 0;
		};
		if (typeof vel_y == 'undefined' || (vel_y != null && vel_y.hasOwnProperty ("__kwargtrans__"))) {;
			var vel_y = 0;
		};
		if (typeof acc_x == 'undefined' || (acc_x != null && acc_x.hasOwnProperty ("__kwargtrans__"))) {;
			var acc_x = 0;
		};
		if (typeof acc_y == 'undefined' || (acc_y != null && acc_y.hasOwnProperty ("__kwargtrans__"))) {;
			var acc_y = 0;
		};
		if (typeof width == 'undefined' || (width != null && width.hasOwnProperty ("__kwargtrans__"))) {;
			var width = null;
		};
		if (typeof height == 'undefined' || (height != null && height.hasOwnProperty ("__kwargtrans__"))) {;
			var height = null;
		};
		if (typeof lifetime == 'undefined' || (lifetime != null && lifetime.hasOwnProperty ("__kwargtrans__"))) {;
			var lifetime = 0;
		};
		if (typeof life == 'undefined' || (life != null && life.hasOwnProperty ("__kwargtrans__"))) {;
			var life = 0;
		};
		if (typeof opacity == 'undefined' || (opacity != null && opacity.hasOwnProperty ("__kwargtrans__"))) {;
			var opacity = 1.0;
		};
		self.x = x;
		self.y = y;
		self.vel_x = vel_x;
		self.vel_y = vel_y;
		self.acc_x = acc_x;
		self.acc_y = acc_y;
		self.img = img;
		self.lifetime = lifetime;
		self.life = life;
		self.opacity = opacity;
		self.width = width;
		self.height = height;
	});}
});

//# sourceMappingURL=Particle.map