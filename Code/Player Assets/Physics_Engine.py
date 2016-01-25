import pygame
from Player_Assets import *

#Create group for physical entities
entities = pygame.sprite.Group()

"""#Physical Entities will be created and added to a group.
#This will make it so the Physics_Engine acts on a cluster of objects.
class Physical_Entity(pygame.sprite.Sprite):

    #init method will initialize a physical entity
    #It will store the objects x and y position to use later
    def __init__(self, p_object):

        #Call superclass constructor, with a reference to the entities group
        #Physical objects will automatically be stored in the group
        pygame.sprite.Sprite.__init__(self, entities)

        #init other attributes
        self.p_object = p_object
        self.x = p_object.getX()
        self.y = p_object.getY()

        #In order to handle collisions we need access to the entities rect attribute
        self.rect = p_object.rect
        self.rect.x = p_object.rect.x
        self.rect.y = p_object.rect.y
        self.area = p_object.area

    #Getters for the class
    def getY(self):
        return self.y

    def getX(self):
        return self.x

    #Setters for the class
    def setY(self, y_change):
        self.y += y_change

    def setY(self, x_change):
        self.x += x_change"""

class Engine(object):

    #init function
    #Takes the fall speed of gravity, and a player/AI object
    #We will nedd the moving objects position in space
    def __init__(self):
        self.clock = pygame.time.Clock()

    #gravity function will take a physical entity and translate its y_coordinate
    def gravity(self, character, fall_speed, maxY):

        #if the character is a player, proceed
        if isinstance(character, Player):

            #if the characters Y value is less than the max Y, proceed
            if character.getY() < maxY:
                character.setY(fall_speed)