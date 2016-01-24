import pygame, time
from Player_Assets import *
from Physics_Engine import *

#init pygame
pygame.init()

#White background
white = (255, 255, 255)

#load the game display to fullscreen, start the clock
gameDisplay = pygame.display.set_mode((800, 1200))
pygame.display.set_caption('Test')
clock = pygame.time.Clock()

#define velocity variables
x_change = 0
y_change = 0

#Create player reference, load the image
player = Player(300, 300, 'player.png', gameDisplay)

#Create new controller
controller = Controller(x_change, y_change)

#Create reference to engine
physics = Engine()

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
        controller.update(player, x_change,y_change, event)


    #Apply gravity
    physics.gravity(player, 7, 500)
        
    #update the display
    gameDisplay.fill(white)
    player.update(x_change, y_change)
    controller.updatePlayer(player)
    player.draw(gameDisplay)
    pygame.display.update()
    clock.tick(30)     

#quit
pygame.quit()
quit()