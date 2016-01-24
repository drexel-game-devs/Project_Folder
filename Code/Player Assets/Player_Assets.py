import pygame

#Player class. Contains an x/y coordinate and a picture
class Player(pygame.sprite.Sprite):

    #initialization method
    def __init__(self, x, y, image, gameDisplay):

        #call superclass constructor
        pygame.sprite.Sprite.__init__(self)

        #init object attributes
        self.x = x
        self.y = y
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.area = gameDisplay.get_rect()

    #update will update the players position on the screen
    def update(self, x_change, y_change):

        #change position according to velocity values if the new position is within the screen.
        newpos = self.rect.move(x_change, 0)
        if self.area.contains(newpos):
            self.x += x_change
        newpos = self.rect.move(0, y_change)
        if self.area.contains(newpos):
            self.y += y_change

        #rect should always be at x,y (undoes the move above if movement failed).
        self.rect.x = self.x
        self.rect.y = self.y

    #draw method draws the player to the screen
    #Method needs a reference to the game screen to function
    #The convert method simply speeds up the blitting process
    def draw(self, display):
        display.blit(self.image, (self.x, self.y))
    """#move_left function moves the player 5 pixels to the left
    def move_left(self, x_change):
        self.x += x_change
    #move_right function moves the player 5 pixels to the right
    def move_right(self, x_change):
        self.x += x_change
    #move_down function moves the player down 5 pixels
    #NOTE: This will be a test function. Will most likely be deleted later.
    def move_down(self, y_change):
        self.y += y_change
    #jump function allows player to jump 10 pixels up
    def jump(self, y_change):
        self.y += y_change"""

    #Getters
    def getX():
        return self.x

    def getY():
        return self.y


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

        #Store Keys in variable
        keys = pygame.key.get_pressed()

        #Handle changes
        if keys[pygame.K_a]:
            self.x_change = -5
        if keys[pygame.K_d]:
            self.x_change = 5
        if keys[pygame.K_w]:
            self.y_change = -10
        if keys[pygame.K_s]:
            self.y_change = 10

        #Handles running while using shift
        if keys[pygame.K_LSHIFT] and keys[pygame.K_d]:
            self.x_change = 10
        if keys[pygame.K_LSHIFT] and keys[pygame.K_a]:
            self.x_change = -10

           
        #call update method from player
        player.update(x_change, y_change) 

        #Handle Key Ups
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                self.x_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                self.y_change = 0

            #Call update method from player
            player.update(x_change, y_change)

    #Update the player class
    def updatePlayer(self, player):

        #Call the update method of the player class
        player.update(self.x_change, self.y_change)