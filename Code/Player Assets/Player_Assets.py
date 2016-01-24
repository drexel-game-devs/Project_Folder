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
        self.dx = 0  #delta x and delta y, for velocities on the x and y axes, respectively.
        self.dy = 0
        self.maxdx = 20  #maximum velocities on x and y axes.
        self.maxdy = 20
        self.accelx = 2 #How much to accelerate by each frame.
        self.accely = 2
        self.decelx = 1 #rate of deceleration when no key is pressed.
        self.decely = 1
        #.inAir = true #True if the player is in the air <-----included for future use.
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.area = gameDisplay.get_rect()
        #Must add player to visible group so it gets updated.
        #self.add(visible)

    #update will update the players position on the screen
    def update(self):
        
        #Store Keys in variable
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.dx -= self.accelx
        if keys[pygame.K_d]:
            self.dx += self.accelx
        if keys[pygame.K_w]:
            self.dy -= self.accely
        if keys[pygame.K_s]:
            self.dy += self.accely
        #TODO: Add shift to sprint.
        #Player must slow down if no keys are pressed.
        if not (keys[pygame.K_a] or keys[pygame.K_d]):
            if (-self.accelx < self.dx , self.accelx): #Set to zero if below a threshold to avoid jittering.
                 self.dx = 0
            elif self.dx > 0:
                self.dx -= self.decelx
            elif self.dx < 0:
                self.dx += self.decelx
        if not (keys[pygame.K_w] or keys[pygame.K_s]):
            if(-self.accely < self.dy < self.accely):
                self.dy = 0
            elif self.dy > 0:
                self.dy -= self.decely
            elif self.dy < 0:
                self.dy += self.decely
        
        #Trim values down to max speed.
        #else statements avoid unnecessary checks.
        if self.dx > self.maxdx:
            self.dx = self.maxdx
        elif self.dx < -self.maxdx:
            self.dx = -self.maxdx
        if self.dy > self.maxdy:
            self.dy = self.maxdy
        elif self.dy < -self.maxdy:
            self.dy = -self.maxdy

        #change position according to velocity values if the new position is within the screen.
        newpos = self.rect.move(self.dx, 0)
        if self.area.contains(newpos):
            self.x += self.dx
        newpos = self.rect.move(0, self.dy)
        if self.area.contains(newpos):
            self.y += self.dy

        #rect should always be at x,y (undoes the move above if movement failed).
        self.rect.x = self.x
        self.rect.y = self.y

    #draw method draws the player to the screen
    #Method needs a reference to the game screen to function
    #The convert method simply speeds up the blitting process
    def draw(self, display):
        display.blit(self.image, (self.x, self.y))

    #Getters
    def getX():
        return self.x

    def getY():
        return self.y


#Controller class for character movement
"""class Controller(object):

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
        keys = pygame.key.get_pressed() #<----- this requires copying the entire array every frame, more expensive than just indexing the array

        #Handle changes
        #We add to the values instead of setting them directly so that opposite keys will cancel out.
        if keys[pygame.K_a]:
            self.x_change += -5
        if keys[pygame.K_d]:
            self.x_change += 5
        if keys[pygame.K_w]:
            self.y_change += -10
        if keys[pygame.K_s]:
            self.y_change += 10

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
        player.update(self.x_change, self.y_change)"""