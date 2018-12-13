import sys

sys.path.append("../..")
from JMSSGraphics import *

# creating our screen
game = Graphics(600, 400, "My Game!")

# your variables go here
x = 200
y = 300

while True:
    y = y - 2

    game.clear()
    game.drawImage("mario.gif", x, y)

    game.reveal()




