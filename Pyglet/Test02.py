from JMSSGraphics import *

# creating our screen
game = Graphics(600, 400, "My Game!")

# your variables go here
x = 200
y = 300

r = 0.0

@game.mainloop
def test():
    global x, y, r
    y = y - 2
    game.clear(r = r)
    r += 0.01
    if r > 1.0:
        r = 0.0

game.run()
