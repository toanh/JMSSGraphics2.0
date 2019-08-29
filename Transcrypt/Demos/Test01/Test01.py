from JMSSGraphics import *

# creating our screen
game = Graphics(600, 400, "My Game!")

# your variables go here
x = 200
y = 300

red = 1.0

@game.mainloop
def doFrame():
    global y, r, game
    y = y - 2
    game.clear(r=red)

    game.drawText("Hello, world!", 100, 100)

    r += 0.01
    if r > 1.0:
        r = 0.0

game.run()
