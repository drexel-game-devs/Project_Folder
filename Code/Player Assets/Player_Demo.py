import pygame, time
from Player_Assets import *

#init pygame
pygame.init()

#load the game display to fullscreen, start the clock
gameDisplay = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption('Test')
clock = pygame.time.Clock()

#define velocity variables
x_change = 0
y_change = 0

#Create player reference, load the image
player = Player(300, 300, 'player.png', gameDisplay)

#Create new controller
controller = Controller(x_change, y_change)

#loop control variable
crashed = False

pygame.draw.rect(gameDisplay, black, (500, 500, 400, 400))

#Game Loop Controller
while not crashed:

    #Event Handler
    for event in pygame.event.get():
        
        #Exit if quit
        if event.type == pygame.QUIT:
            crashed = True

        #update the player using the controller
        controller.update(player, x_change,y_change, event)
        
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