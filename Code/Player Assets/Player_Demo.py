import pygame, time
from Player_Assets import *
#set the width and height
display_width = 800
display_height= 600

#init pygame
pygame.init()

#create reference to white screen
white = (255, 255, 255)

#load the game display, start the clock
gameDisplay = pygame.display.set_mode((display_height, display_width))
pygame.display.set_caption('Test')
clock = pygame.time.Clock()

#define velocity variables
x_change = 0
y_change = 0

#Create player reference, load the image
player = Player(300, 300, 'player.png')

#Create new controller
controller = Controller(x_change, y_change)

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