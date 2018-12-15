from JMSSGraphics import *

class Particle():
    def __init__(self, img = None, x = 0, y = 0, vel_x = 0, vel_y = 0, acc_x = 0, acc_y = 0, \
                 width = None, height = None, lifetime = 0, life = 0, opacity = 1.0):
        self.x = x
        self.y = y

        self.vel_x = vel_x
        self.vel_y = vel_y
        self.acc_x = acc_x
        self.acc_y = acc_y

        self.img = img

        self.lifetime = lifetime
        self.life = life

        self.opacity = opacity

        self.width = width
        self.height = height
