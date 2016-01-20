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

    def update(self, player, x_change, y_change, event):

        #Handle Key Downs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.x_change = -5
            if event.key == pygame.K_d:
                self.x_change = 5
            if event.key == pygame.K_w:
                self.y_change = -10
            if event.key == pygame.K_s:
                self.y_change = 10

            #call update method from player
            player.update(x_change, y_change) 


        #Handle Key Ups
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.x_change = 0
            if event.key == pygame.K_d:
                self.x_change = 0
            if event.key == pygame.K_w:
                self.y_change = 0
            if event.key == pygame.K_s:
                self.y_change = 0

            #Call update method from player
            player.update(x_change, y_change)

    #Update the player class
    def updatePlayer(self, player):

        #Call the update method of the player class
        player.update(self.x_change, self.y_change)