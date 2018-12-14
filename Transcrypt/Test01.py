from JMSSGraphics import *

# creating our screen
game = Graphics(600, 400, "My Game!")

# your variables go here
x = 200
y = 300

r = 1.0

def frame():
    global y
    y = y - 2
    game.clear(r = r, b = 1.0)
    r += 0.01
    if r > 1.0:
        r = 0.0

game.mainloop(main)

game.run()
