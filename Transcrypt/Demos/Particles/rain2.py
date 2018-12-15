#Daniel E Hong
from Particle import *
import random#allow random numbers
from JMSSGraphics import *
jmss = Graphics(width = 800, height = 450, title = 'rain', fps = 60)#draw screen
bg0 = jmss.loadImage('rf0.jpg')#load background images into ram
bg1 = jmss.loadImage('rf1.png')
bg2 = jmss.loadImage('rf2.png')
bg3 = jmss.loadImage('rf3.png')

current_bg = bg0

water_list = []#create list
n=0#set value
while n<1000:#add seperate values to each list item
    water = Particle()
    water.img = jmss.loadImage('water.png')
    water.x = random.randint(0,784)
    water.y = random.randint(10,490)
    water.yvel = random.randint(50,150)
    water.yvel = water.yvel/10#making yvel go between 5 and 15
    water.xvel = random.randint(20,70)
    water.xvel = water.xvel/10#making xvel go between 2 and 7
    water_list.append(water)
    n+=1

Music = jmss.loadSound("rain.wav", streaming = True)#loading music

def rain():
    global water_list, water, n#adding values to class
    n=0
    while n<1000:#draw every one of the 1000 particles
        water = water_list[n]
        jmss.drawImage(water.img, water.x, water.y, width = 1.5, height = 15)
        if jmss.isKeyDown(KEY_A):#if a is pressed the rain is blow to the left
            water.x -= water.xvel
        if jmss.isKeyDown(KEY_D):#if d is pressed the rain is blow to the right
            water.x += water.xvel
        if jmss.isKeyDown(KEY_S):#if s is pressed the rain speeds up
            water.yvel *= 1.5
        if jmss.isKeyDown(KEY_W):#if w is pressed the rain slows down
            water.yvel *= 1/2
        if water.yvel > 76:#making sure the rain doesn't go too fast
            water.yvel = random.randint(50,150)
            water.yvel /= 10
        water.y -= water.yvel
        if water.y <-16:#looping the rain so it"s never ending
            water.y = 501
            water.x = random.randint(-100,884)
        else:
            n+=1
def bg():
    global bg0, bg1, bg2, bg3, current_bg
    #press and hold one of these buttons to change the background
    if jmss.isKeyDown(KEY_Z):
        current_bg = bg0
    elif jmss.isKeyDown(KEY_X):
        current_bg = bg1
    elif jmss.isKeyDown(KEY_C):
        current_bg = bg2
    elif jmss.isKeyDown(KEY_V):
        current_bg = bg3

    jmss.drawImage(current_bg, 0, 0)
    
            
jmss.playSound(Music)#play the music
@jmss.mainloop
def Game():
    global water_list, water, n, bg0, bg1, bg2, bg3
    jmss.clear(0, 0, 0, 1)#clear values
    bg()#run the code in these classes
    rain()
jmss.run()#run the program
jmss.pauseSound(Music)#pause the music is the program stops
