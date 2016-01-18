import pygame

#Player class. Contains an x/y coordinate and a picture
class Player(pygame.sprite.Sprite):

    #initialization method
    def __init__(self, x, y, image):

        #call superclass constructor
        pygame.sprite.Sprite.__init__(self)

        #init object attributes
        self.x = x
        self.y = y
        self.image = image

    #update will update the players position on the screen
    def update(self, x_change, y_change):
        
	#This structure determines what function to call
	#Function called depends on value of the x_change/y_change variables.
        if x_change < 0:
            self.move_left(x_change)
        if x_change > 0:
            self.move_right(x_change)
        if y_change > 0:
            self.move_down(y_change)
        if y_change < 0:
            self.jump(y_change)

    #draw method draws the player to the screen
    #Method needs a reference to the game screen to function
    #The convert method simply speeds up the blitting process
    def draw(self, display):
        playerImage = pygame.image.load(self.image).convert()
        display.blit(playerImage, (player.x, player.y))

    #move_left function moves the player 5 pixels to the left
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
        self.y += y_change