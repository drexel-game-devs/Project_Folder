import pygame

#Controller class for character movement
class Controller(object):

    #constructor accept a player object for now
    def __init__(self, x_change, y_change):

        #init the x_change and y_change
        self.x_change = x_change
        self.y_change = y_change

        #Give the vars 0
        self.x_change = 0
        self.y_change = 0

    #Determine how to move the player
    for event in pygame.event.get():

        #Handle Key Downs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_change = -5
            if event.key == pygame.K_d:
                x_change = 5
            if event.key == pygame.K_w:
                y_change = -10
            if event.key == pygame.K_s:
                y_change = 10

        #Handle Key Ups
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                x_change = 0
            if event.key == pygame.K_d:
                x_change = 0
            if event.key == pygame.K_w:
                y_change = 0
            if event.key == pygame.K_s:
                y_change = 0

    #Update the player class
    def updatePlayer(self, player):

        #Call the update method of the player class
        player.update(x_change, y_change)