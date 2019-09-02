from JMSSGraphics import *

# creating our screen
game = Graphics(600, 400, "My Game!")

# your variables go here
x = 200
y = 300

r = 0.0

drum = game.loadSound("drum.wav", False)
blip = game.loadSound("blip.wav", False)

sound = drum

while game.reveal():
    y = y - 2
    game.clear(r = r)
    r += 0.01
    if game.isKeyPressed(KEY_A):
        sound = drum
        game.playSound(sound)
    elif game.isKeyPressed(KEY_D):
        sound = blip
        game.playSound(sound)
    elif game.isKeyPressed(KEY_S):
        game.pauseSound(sound)
    if r > 1.0:
        #answer = game.input("Enter your name:")
        #print(answer)
        r = 0.0

