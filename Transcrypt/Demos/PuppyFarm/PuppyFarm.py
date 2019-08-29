from JMSSGraphics import *

window = Graphics(640, 480, fps = 1)

#######################################################################
# the Puppy class (a class is like a 'blueprint')
#######################################################################
class Puppy:
    # the class constructor
    def __init__(self):
        # the class constructor initialises the class attributes
        # below
        self.name = None
        self.num_legs = 4
        self.ID = 0
        self.breed = None
        self.dateofbirth = None
        self.x = 0        
        self.y = 0
        self.caught = False             # adding a new attribute to
                                        # keep track of when I am caught
        self.r = 0
        self.g = 0
        self.b = 0

    # the class methods are below
    def Move(self, direction):
        # 0: left, 1: right, 2: up, 3: down
        if self.caught == False:
        #if not self.caught:
            if direction == 0:
                self.x -= 1
            elif direction == 1:
                self.x += 1             

    def Draw(self):
        if not self.caught:
        # display my name, x, y
        # print(self.name + ":" + str(self.x) + "," + str(self.y))
            print("{}:{},{}".format(self.name,self.x,self.y))
            window.drawRect(self.x * 16, self.y * 16, \
                            self.x * 16 + 16, self.y * 16 + 16, \
                            self.r, self.g, self.b)

    def Bark(self):
        if self.breed == "bulldog":
            print("Woof woof!")
        elif self.breed == "chihuahua":
            print("Yap yap!")
        else:
            print("Bark bark!")
            
#######################################################################
# the PuppyCatcher class
#######################################################################
class PuppyCatcher:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.puppies = []

    def Catch(self, caught_puppy):        
        print("Gotcha!" + caught_puppy.name)
        self.puppies.append(caught_puppy)
        caught_puppy.caught = True

    def Free(self, free_puppy):
        # print "Freeing... " + puppy name
        # remove the puppy from the list
        # tell the puppy that it is freed
        print("Freeing..." + free_puppy.name)
        #print("Freeing....{}".format(free_puppy.name))
        self.puppies.remove(free_puppy)
        free_puppy.caught = False

    def Draw(self):
        window.drawRect(self.x * 16, self.y * 16, \
                        self.x * 16 + 16, self.y * 16 + 16, \
                        1, 0, 1)        


#######################################################################
# setting up the simulation
#######################################################################

# instantiate a PuppyCatcher
fred = PuppyCatcher()
fred.x = 5
fred.y = 0

# instantiate 2 Puppies
pup1 = Puppy()
pup1.name = "Fido"
pup1.ID = 1
pup1.breed = "bulldog"
pup1.x = 0
pup1.y = 0
# set up the color for Fido
pup1.r = 0
pup1.g = 1
pup1.b = 0

pup2 = Puppy()
pup2.name = "Fluffy"
pup2.ID = 2
pup2.breed = "chihuahua"
pup2.x = 14
pup2.y = 0
# set up the color for Fluffy
pup2.r = 1
pup2.g = 1
pup2.b = 1


#######################################################################
# Run the simulation
#######################################################################
i = 0

@window.mainloop
def RunSimulation():
    global window, pup1, pup2, fred, i
    window.clear()

    print("Simulation in step: " + str(i))

    # in simulation step 25,
    # if fluffy is caught, free her
    if i == 25 and pup2.caught == True:
        
        fred.Free(pup2)
    
    # move the puppies
    pup1.Move(1)
    pup2.Move(0)

    # check if any puppies are at the same spot as the puppycatcher
    if pup1.x == fred.x and pup1.y == fred.y:
        # this is to prevent the puppy from being re-caught
        if pup1.caught == False:
            fred.Catch(pup1)
            
    if pup2.x == fred.x and pup2.y == fred.y:
        if pup2.caught == False:
            fred.Catch(pup2)

    #draw the puppies
    pup2.Draw()
    pup1.Draw()

    if window.isKeyPressed(KEY_W):
        fred.y += 1

    fred.Draw()

    i += 1

    # unveiling the curtain
    window.reveal()


window.run()
