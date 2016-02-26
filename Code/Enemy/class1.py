import pygame, math
from PythonApplication8 import Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
red_c = (255,0,0)

class mob(pygame.sprite.Sprite):
    """description of class"""
    def __init__(self):
        super().__init__()
       # Call the parent's constructor
        
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        width = 40
        height = 60
        self.movement = 'right'

        #Direction player is facing. Defaults to Right
        self.direction = "R"
        
        #Get a list of images for animation
        self.left_frames = []
        self.right_frames = []

        #grab all images and add them to their respective lists
        image = pygame.image.load("main_player.png").convert()
        self.left_frames.append(image)
        image = pygame.image.load("main_walk_0.png").convert()
        self.left_frames.append(image)
        image = pygame.image.load("main_walk_1.png").convert()
        self.left_frames.append(image)
        image = pygame.image.load("main_walk_2.png").convert()
        self.left_frames.append(image)
        image = pygame.image.load("main_walk_3.png").convert()
        self.left_frames.append(image)

        #create the right frames by flipping the left frames
        for image in range(len(self.left_frames)):

            image = pygame.transform.flip(self.left_frames[image], True, False)
            self.right_frames.append(image)

        #starting image is the first in left frames
        self.image = self.left_frames[0]
 
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
 
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
 
        # List of sprites we can bump against
        self.level = None

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
 
        # Move left/right
        self.rect.x += self.change_x

        #Grab the players position
        pos = self.rect.x

        #Update the image loaded
        if self.direction == "L":
            frame = (pos // 30) % len(self.right_frames)
            self.image = self.right_frames[frame]
        else:
            frame = (pos // 30) % len(self.left_frames)
            self.image = self.left_frames[frame]

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .34
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
    def jump(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10
    def moveleft(self):       
        if self.rect.left < 0:
            self.rect.left = 0          
        else:
            self.change_x = -5
            self.direction = 'L'
    def moveright(self):
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH       
        else:

            self.change_x = 5
            self.direction = 'R'

    def stop(self):
        self.change_x = 0
    def spawn(self,display):
        display.blit(self.image,(self.rect.x,self.rect.y))

    def follow(self, player, jumpl, counter):
        if self.rect.x in range(jumpl, jumpl + 15):
            if self.direction == 'L':
                self.jump()
                self.moveleft()
            elif self.direction == 'R':
                self.jump()
                self.moveright()
                #self.stop()
        elif player.rect.x > self.rect.x:
            self.moveright()
            self.direction = 'R'
        elif player.rect.x < self.rect.x:
            self.moveleft()
            self.direction = 'L'
        elif player.rect.x == player.rect.x:
            self.stop()
        elif player.rect.x > self.rect.x and player.rect.y < self.rect.y:
            if self.rect.x in range(jumpl - 10, jumpl + 15):
                self.jump()
                self.moveright()
                self.direction = 'R'
        elif player.rect.x < self.rect.x and player.rect.y < self.rect.y:
            print('In if statement')
            if self.rect.x in range(jumpl + 10, jumpl - 15):
                print('Enemy x' + str(self.rect.x))
                self.jump()
                self.moveleft()
                self.direction = 'L'
   
        elif player.rect.x == self.rect.x and player.rect.y < self.rect.y:
            self.stop()
        print(str(self.rect.x) + ' + ' + str(self.change_x))
        
    def sight(self, gameDisplay):
        #pygame.draw.rect(screen, color, (x,y,width,height), thickness)     
        pygame.draw.rect(gameDisplay, red_c, (self.rect.x, self.rect.y, 300, 50), 0)

    def sight2(self, gameDisplay):
        #pygame.draw.rect(screen, color, (x,y,width,height), thickness)
        pygame.draw.rect(gameDisplay, red_c, (self.rect.x, self.rect.y, -300, 60), 0)
    
    def patrol(self,gameDisplay,player, jumpl):
        if self.movement == 'right':
            self.moveright()
            self.direction = 'R'
            self.sight(gameDisplay)
            newcor = player.rect.y + 34
            #print(player.rect.x)
            if player.rect.x in range(self.rect.x, self.rect.x + 201) and (player.rect.y in range(self.rect.y, self.rect.y + 34) or newcor in range(self.rect.y, self.rect.y + 34)):
                self.follow(player, jumpl)
                #print("Following")
            elif self.rect.x >= 300:
                self.movement = 'left'
            
        elif self.movement == 'left':
            self.moveleft()
            self.direction = 'L'
            self.sight2(gameDisplay)
            newcor = player.rect.y + 34
            if player.rect.x in range(self.rect.x - 201, self.rect.x) and (player.rect.y in range(self.rect.y, self.rect.y + 34) or newcor in range(self.rect.y, self.rect.y + 34)):
                self.follow(player,jumpl)      
                #print("Following2") 
            if self.rect.x == 30:
                self.movement = 'right'

