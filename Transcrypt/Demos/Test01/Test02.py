from JMSSGraphics import *
from math import sin

# creating our screen
game = Graphics(600, 400, "My Game!")
frame = 0

@game.mainloop
def doFrame():
    global frame
    game.clear(g=0.5 * sin(frame * 0.05) +0.5)
    frame += 1

game.run()
