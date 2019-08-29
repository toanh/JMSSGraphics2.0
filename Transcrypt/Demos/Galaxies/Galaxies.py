from JMSSGraphics import *
from vector import *

import random
from math import *

stars = []
blackholes = []

def SpawnGalaxyStarsByRing(center, numrings, color = (255, 255, 255)):
    for i in range(0, numrings):
        radius = 4 + i * 3
        circumference = radius * 2 * 3.14159
        for j in range (0, int(circumference / 5) + 1):
            a = j / radius * 5
            pos = Vector(radius * cos(a), radius * sin(a)) + center

            relpos = pos - center
            magnitude = sqrt(10 / relpos.norm())
            vel = Vector(relpos[1], -relpos[0])
            vel = vel.normalize()
            if (color[0] == 255):
                stars.append([pos,
                              vel.__mul__(magnitude),
                              Vector(0,0),
                              [180 + 75 * (1 - i/numrings), 255, 255]])
            else:
                stars.append([pos,
                              vel.__mul__(magnitude),
                              Vector(0,0),
                              [255, 255, 180 + 75 * (1 - i/numrings)]])

def SpawnGalaxyStars(center, numstars, radius, color = 0.0):
    for i in range(0, numstars):
        d = random.random() * radius + 4
        a = random.random() * 3.14159 * 2

        #test = Vector(1,1).__add__(Vector(2,2))
        pos = Vector(d * cos(a), d * sin(a)).__add__(center)

        relpos = pos.__sub__(center)
        magnitude = sqrt(10 / relpos.norm())
        vel = Vector(relpos[1], -relpos[0])
        vel = vel.normalize()
        if (color == 1.0):
            stars.append([pos,
                          vel.__mul__(magnitude),
                          Vector(0,0),
                          [c/255.0 for c in [180 + 75 * (1 - d/44), random.random() * 75 + 180, random.random() * 75 + 180]]])
        else:
            stars.append([pos,
                          vel.__mul__(magnitude),
                          Vector(0,0),
                          [c/255.0 for c in [random.random() * 75 + 180, random.random() * 75 + 180, 180 + 75 * (1 - d/44)]]])

def Initialise():
    
    centre = Vector(150, 80)
    blackholes.append([centre,     # position
                       Vector(0.08,0),     # velocity
                       Vector(0,0)      # acceleration
                       ])
    
    SpawnGalaxyStars(centre, 400, 40, 0.0)
    #SpawnGalaxyStarsByRing(centre, 20, (180, 180, 255))
    

    centre = Vector(300, 160)
    blackholes.append([centre,     # position
                       Vector(-0.08,0),     # velocity
                       Vector(0,0)      # acceleration
                       ])
    SpawnGalaxyStars(centre, 800, 80, 1.0)
    #SpawnGalaxyStarsByRing(centre, 20, (180, 180, 255))

def Render():
    jmss.clear()
    # draw the stars around the supermassive black holes
    for i in range(0, len(stars)):
        #jmss.drawCircle(stars[i][3], stars[i][0], 1)
        jmss.drawPixel(stars[i][0][0],\
                       stars[i][0][1],\
                       stars[i][3][0],\
                       stars[i][3][1],\
                       stars[i][3][2])
        
    for i in range(0, len(blackholes)):
        #print(blackholes[i][0])
        jmss.drawCircle(blackholes[i][0][0],\
                        blackholes[i][0][1],\
                        5,\
                        255,\
                        255,\
                        255)


def UpdateStatic():
    # apply gravity from the black holes on the stars
    for j in range(0, 400):
        # apply gravity force
        difference = blackholes[0][0].__sub__(stars[j][0])

        direction = difference.normalize()
        distance = difference[0]*difference[0] + difference[1]*difference[1]

        magnitude = 1/distance * 10;

        stars[j][2] = stars[j][2].__add__(direction.__mul__(magnitude))
    for j in range(400, len(stars)):
        # apply gravity force
        difference = blackholes[1][0].__sub__(stars[j][0])

        direction = difference.normalize()
        distance = difference[0]*difference[0] + difference[1]*difference[1]

        magnitude = 1/distance * 10;

        stars[j][2] = stars[j][2].__add__(direction.__mul__(magnitude))


    # update the stars
    for i in range(0, len(stars)):
        # integrate
        stars[i][1] = stars[i][1].__add__(stars[i][2])
        stars[i][0] = stars[i][0].__add__(stars[i][1])

        # zero out the force
        stars[i][2] = Vector(0,0)

    return

def Update():

    for i in range(0, len(blackholes)):
        for j in range(1, len(blackholes)):
            if (i == j):
                continue
            # apply gravity force
            difference = blackholes[i][0].__sub__(blackholes[j][0])

            direction = difference.normalize()
            distance = difference[0]*difference[0] + difference[1]*difference[1]

            magnitude = 1/distance * 10;

            if (magnitude > 2):
                magnitude = 2

            blackholes[j][2] = blackholes[j][2].__add__(direction.__mul__(magnitude))

            blackholes[i][2] = blackholes[i][2].__sub__(direction.__mul__(magnitude))

    # update the black holes
    for i in range(0, len(blackholes)):
        # integrate
        blackholes[i][1] = blackholes[i][1].__add__(blackholes[i][2])
        blackholes[i][0] = blackholes[i][0].__add__(blackholes[i][1])

        # zero out the force
        blackholes[i][2] = Vector(0,0)

    # apply gravity from the black holes on the stars
    for i in range(0, len(blackholes)):
        for j in range(0, len(stars)):
            # apply gravity force
            difference = blackholes[i][0].__sub__(stars[j][0])

            direction = difference.normalize()
            distance = difference[0]*difference[0] + difference[1]*difference[1]

            magnitude = 1/distance * 10;
            if (magnitude > 1):
                magnitude = 1

            stars[j][2] = stars[j][2].__add__(direction.__mul__(magnitude))


    # update the stars
    for i in range(0, len(stars)):
        # integrate
        stars[i][1] = stars[i][1].__add__(stars[i][2])
        stars[i][0] = stars[i][0].__add__(stars[i][1])

        # zero out the force
        stars[i][2] = Vector(0,0)

    return

gravity = False
paused = False

jmss = Graphics(800, 600, "Galaxies Simulation")
Initialise()
#jmss.addEventListener(SimulationKeyListener)

@jmss.mainloop
def Simulate():
    global gravity

    if (not paused):
        if (gravity):
            Update()
        else:
            UpdateStatic()
    Render()

jmss.run()

def SimulationKeyListener(event):
    global gravity, paused
    if (event.type == pygame.KEYUP and event.key == pygame.K_a):
        gravity = not gravity
    if (event.type == pygame.KEYUP and event.key == pygame.K_SPACE):
        paused = not paused

