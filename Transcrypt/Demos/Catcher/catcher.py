from JMSSGraphics import *

from collision import *

from random import *

# creating our Graphics object
game = Graphics(640, 480)

star_x = randint(0, 640 - 20)
star_y = 470
star_speed = 2

paddle_x = 0
paddle_y = 0

score = 0

# using GOTOs... Evil??
# Or a good scaffolding tool?
@game.mainloop
def main():
    global star_x, star_y, star_speed, score, paddle_x, paddle_y, game
    star_y -= star_speed

    if game.isKeyPressed(KEY_A):
        paddle_x -= 3
    if game.isKeyPressed(KEY_D):
        paddle_x += 3

    if IsColliding(paddle_x, paddle_y, 80, 16, star_x, star_y, 20, 20):
        # resetting the star's position
        star_y = 470
        star_x = randint(0, 640 - 20)
        score += 1
        # slowly increasing its speed to ramp up difficulty
        star_speed += 0.05

    if star_y < -20:
        game.clear()
        game.drawText("GAME OVER!!", 200, 240, fontSize=30)
    else:
        game.clear()

        # drawing the images
        # note the order, drawn from back to front
        game.drawImage("star.gif", star_x, star_y)
        game.drawImage("paddle.gif", paddle_x, paddle_y)

        # BUG: drawText() has to be the LAST call to game or else everything after it flickers
        # AND there can only be ONE drawText call
        game.drawText("Score: " + str(score), 280, 440, fontSize=20)
game.run()