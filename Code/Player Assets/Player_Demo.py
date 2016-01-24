import pygame, time
from Player_Assets import *
#from Physics_Engine import * TOFO: this doesn't work for a file in a separate folder.

#init pygame
pygame.init()

#White background
white = (255, 255, 255)

#load the game display to fullscreen, start the clock
gameDisplay = pygame.display.set_mode((800, 1200))
pygame.display.set_caption('Test')
clock = pygame.time.Clock()

#create sprite groups and add player.
visible = pygame.sprite.Group()

#define velocity variables
#x_change = 0
#y_change = 0

#Create player reference, load the image
player = Player(300, 300, 'player.png', gameDisplay)
player.add(visible) #<-----TODO: This should be in the player initializer but as-is, referencing visible from another file throws undefined.
#Create new controller <----- not currently used.
#controller = Controller(x_change, y_change)

#Create reference to engine
#physics = Engine()

#loop control variable
crashed = False

#Game Loop Controller
while not crashed:

    #Event Handler
    for event in pygame.event.get():
        
        #Exit if quit
        if event.type == pygame.QUIT:
            crashed = True

        #update the player using the controller
        #controller.update(player, x_change,y_change, event)
    #update all objects.
    for o in visible.sprites():
        o.update()


    #Apply gravity <----- this should happen in the update event of each object that is affected by gravity. TODO.
    #physics.gravity(player, 7, 500)
        
    #update the display
    gameDisplay.fill(white)
    for o in visible.sprites():
        o.draw(gameDisplay)
    pygame.display.update()
    clock.tick(30)     

#quit
pygame.quit()
quit()