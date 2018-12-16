#Dylan Gonzalez

from Particle import *
from JMSSGraphics import *
import random, time, math

#Move the torch into the fire so that fire catches onto the torch. 

jmss = Graphics(width = 800, height = 600, title = "Flame", fps = 60) #graphics with jmss framework

#Images used
fire_img = jmss.loadImage("Rocket_Fire2.png") #fire particle image
fire2_img = jmss.loadImage("fire2.png") #2nd fire particle image
wood = jmss.loadImage("wood_campfire.png") #wood image
rain_img = jmss.loadImage("rain.png") #rain particle image
forest = jmss.loadImage("forest.jpeg") #forest background
torch_img = jmss.loadImage("torch.png") #torch image

#Sounds
rain_sound = jmss.loadSound("rain.wav")
jmss.playSound(rain_sound, streaming = True)
fire_sound = jmss.loadSound("crackling-fireplace.wav")
jmss.playSound(fire_sound, streaming = True)

#Lists for particles
fire_list = []
fire_img_list = [fire_img, fire2_img]
rain_list = []
torch_fire_list = []

#x variable for the wood image
wood_x = 368

#fire variables
fire1_pos_x = 395
fire2_pos_x = 595
fire3_pos_x = 195

#Torch variables
torch_x = 780
torch_y = 30

#maximum y position of the fire particle
max_fire_y = 140
max_torchfire_y = torch_y + 140

isTorchFire = False

p = 0 #control variable for while loops

#Draw all the images
def Draw():
    global forest, wood, wood_x
    jmss.drawImage(forest, x = 0, y = 0, width = 800, height = 600) #background image
    jmss.drawImage(wood, x = wood_x, y = 0, width = 100, height = 70)
    jmss.drawImage(wood, x = wood_x + 200, y = 0, width = 100, height = 70) #Draw the second wood image 200 to the right of the middle wood image
    jmss.drawImage(wood, x = wood_x - 200, y = 0, width = 100, height = 70) #Draw the third wood image 200 to the left of the middle wood image

#First fire function
def Fire1():
    global fire_list, p, fire_img_list

    #while loop for creating the particles
    p = 0
    while p < 5:
        fire = Particle() #create the object
        fire.img_number = random.randint(0,1) #random number for a random image particle
        fire.x = random.randint(fire1_pos_x,fire1_pos_x + 13) #set the x position of the fire to a random integer between 395 and 408
        fire.y = 25
        fire.vel_x = random.randint(-1,1)/2 #x velocity of the fire particle. Dividing by 2 to give a float
        fire.vel_y = random.random() * 2 + 1 #y velocity of the fire particle.
        fire.size = random.randint(1,30) #random size of the fire particle.
        fire.opacity = 0.5
        
        fire_list.append(fire) #add the particle to the list

        p += 1 #increase the control variable by 1

    #while loop for drawing the fire particles with their respective velocities
    for fire in fire_list:
        fire.y += fire.vel_y #increase the y velocity of the fire particle by vel_y
        fire.x += fire.vel_x #increase the x velocity of the fire particle by vel_x
        
        fire.size -= 0.2 #decrease the size of the fire particle by 0.2
        fire.opacity -= 0.01 #decrease the opacity of the fire particle by 0.01
        
        if fire.opacity < 0.0:
            fire.opacity = 0.0
        elif fire.opacity > 1.0:
            fire.opacity = 1.0
            
        jmss.drawImage(fire_img_list[fire.img_number], x = fire.x, y = fire.y, width = fire.size, height = fire.size, opacity = fire.opacity)

        #once the fire particle gets above 110, delete it from the list
        if fire.y > max_fire_y:
            fire_list.remove(fire)



#Second fire function
def Fire2():
    global fire_list, p, fire_img_list

    #while loop for creating the particles
    p = 0
    while p < 5:
        fire = Particle() #create the object
        fire.img_number = random.randint(0,1) #random number for a random image particle
        fire.x = random.randint(fire2_pos_x,fire2_pos_x + 13) #set the x position of the fire to a random integer between 595 and 608
        fire.y = 25
        fire.vel_x = random.randint(-1,1)/2 #x velocity of the fire particle. Dividing by 2 to give a float
        fire.vel_y = random.random() * 2 + 1 #y velocity of the fire particle.
        fire.size = random.randint(1,30) #random size of the fire particle.
        fire.opacity = 0.5
        
        fire_list.append(fire) #add the particle to the list

        p += 1 #increase the control variable by 1


    #while loop for drawing the fire particles with their respective velocities
    for fire in fire_list:
        fire.y += fire.vel_y #increase the y velocity of the fire particle by vel_y
        fire.x += fire.vel_x #increase the x velocity of the fire particle by vel_x
        
        fire.size -= 0.2 #decrease the size of the fire particle by 0.2
        fire.opacity -= 0.01 #decrease the opacity of the fire particle by 0.01

        jmss.drawImage(fire_img_list[fire.img_number], x = fire.x, y = fire.y, width = fire.size, height = fire.size, opacity = fire.opacity)        

        #once the fire particle gets above 110, delete it from the list
        if fire.y > max_fire_y:
            fire_list.remove(fire)

        if fire.opacity <= 0:
            fire.opacity = 0
            

def Fire3():
    global fire_list, p, fire_img_list

    #while loop for creating the particles
    p = 0
    while p < 5:
        fire = Particle() #create the object
        fire.img_number = random.randint(0,1) #random number for a random image particle
        fire.x = random.randint(fire3_pos_x,fire3_pos_x + 13) #set the x position of the fire to a random integer between 595 and 608
        fire.y = 25
        fire.vel_x = random.randint(-1,1)/2 #x velocity of the fire particle. Dividing by 2 to give a float
        fire.vel_y = random.random() * 2 + 1#y velocity of the fire particle.
        fire.size = random.randint(1,30) #random size of the fire particle.
        fire.opacity = 0.5
        
        fire_list.append(fire) #add the particle to the list

        p += 1 #increase the control variable by 1


    #while loop for drawing the fire particles with their respective velocities
    for fire in fire_list:
        fire.y += fire.vel_y #increase the y velocity of the fire particle by vel_y
        fire.x += fire.vel_x #increase the x velocity of the fire particle by vel_x
        
        fire.size -= 0.2 #decrease the size of the fire particle by 0.2
        fire.opacity -= 0.01 #decrease the opacity of the fire particle by 0.01

        jmss.drawImage(fire_img_list[fire.img_number], x = fire.x, y = fire.y, width = fire.size, height = fire.size, opacity = fire.opacity)        

        #once the fire particle gets above 110, delete it from the list
        if fire.y > max_fire_y:
            fire_list.remove(fire)

        if fire.opacity <= 0:
            fire.opacity = 0
            

def Rain():
    global rain_list
    #while loop for creating the particles
    p = 0
    while p < 1:
        rain = Particle() #create the object
        rain.img = rain_img #image of the rain particle
        rain.x = random.randint(0,800) #set the x position of the rain to a random integer between 0 and 800
        rain.y = 600
        rain.vel_y = random.randint(-15,-5) #y velocity of the rain particle.
        rain.size = 30 #rain particle size
        rain.opacity = 1 #rain particle opacity
        
        rain_list.append(rain)

        p += 1

    #while loop for drawing the fire particles with their respective velocities
    for rain in rain_list:
        rain.y += rain.vel_y #decrease the y velocity of the rain particle by vel_y
        
        jmss.drawImage(rain.img, x = rain.x, y = rain.y, width = rain.size, height = rain.size, opacity = rain.opacity)        


    for rain in rain_list:
        #once the rain particle gets below 0 (below the screen), delete it from the list
        if rain.y < 0:
            #del rain_list[n]
            rain_list.remove(rain)
            
        
def Torch():
    global torch_y, torch_x, max_fire_y, isTorchFire, torch_img, torch_fire_list

    torch_x = jmss.getMousePos()[0] #access the x position of the mouse
    torch_y = 600 - jmss.getMousePos()[1] #access the y position of the mouse

    #draw the torch
    jmss.drawImage(torch_img, x = torch_x, y = torch_y, width = 60, height = 60)        

    #check if the torch is in the region of the campfires. 
    if torch_y < max_fire_y and torch_y > 25 and ((torch_x < fire1_pos_x + 13 and torch_x > fire1_pos_x) or (torch_x < fire2_pos_x + 13 and torch_x > fire2_pos_x) or (torch_x < fire3_pos_x + 13 and torch_x > fire3_pos_x)):
        isTorchFire = True #set isTorchFire to true

    if isTorchFire == True:
        #while loop for creating the particles
        p = 0
        while p < 5:
            fire = Particle() #create the object
            fire.img_number = random.randint(0,1) #random number for a random image particle
            fire.x = random.randint(torch_x, torch_x + 4) #set the x position of the fire to a random integer between 595 and 608
            fire.y = torch_y + 41
            fire.vel_x = random.randint(-1,1)/4 #x velocity of the fire particle. Dividing by 4 to give a smaller number
            fire.vel_y = random.randint(1,4) #y velocity of the fire particle.
            fire.size = random.randint(1,20) #random size of the fire particle.
            fire.opacity = 0.3
            
            torch_fire_list.append(fire) #add the particle to the list

            p += 1 #increase the control variable by 1

        #while loop for drawing the fire particles with their respective velocities
        for t in torch_fire_list:
            t.y += t.vel_y #increase the y velocity of the fire particle by vel_y
            t.x += t.vel_x #increase the x velocity of the fire particle by vel_x
            
            t.size -= 0.2 #decrease the size of the fire particle by 0.2
            t.opacity -= 0.01 #decrease the opacity of the fire particle by 0.01

            jmss.drawImage(fire_img_list[t.img_number], x = t.x, y = t.y, width = t.size, height = t.size, opacity = t.opacity)        

            max_torchfire_y = torch_y + 140

            #once the fire particle gets above the max torch y position, delete it from the list
            if t.y > max_torchfire_y:
                torch_fire_list.remove(t)

            if t.opacity <= 0:
                t.opacity = 0
                

@jmss.mainloop
def Game():
    Draw() #Drawing the images
    Fire1() #First Campfire 
    Fire2() #Second Campfire
    Fire3() #Third Campfire
    Torch() #Torch with the fire
    Rain() #Rain particles

 #   Check how many particles are on the screen:
##    n = len(torch_fire_list) + len(rain_list) + len(fire_list)
##    jmss.drawText(str(n), 0, 0) 

jmss.clear()
jmss.run()
