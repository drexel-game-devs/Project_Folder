import pygame
import time


#loads pygame
pygame.init()

#screen display size
display_width = 800
display_height = 600

#color values
black = (0,0,0)
white = (255, 255, 255)
red = (200,0,0)
green = (0,200, 0)
bright_green = (0,255,0)
bright_red = (255,0,0)

#text values
largeText = pygame.font.Font('freesansbold.ttf', 85)
smallText = pygame.font.Font('freesansbold.ttf', 20)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Title')
clock = pygame.time.Clock()

#function that takes a string text and font type
#returns textSurface with the info
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
#button function used in title screen
def button(msg, x, y, width, height, acolor, icolor, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(gameDisplay,acolor, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "play":
                print("play")
                #needs code or function to start the game!
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay,icolor,(x,y,width,height))
   
    textSurf, textRect = text_objects(msg, smallText)
    textRect = ( (x + (width/6)), (y + (height/3)) )
    gameDisplay.blit(textSurf, textRect)

    
#function that runs the title screen
def Intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event) #I used this to show mouse events 
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.fill(black)
        
        TextSurf, TextRect = text_objects('Low Rez Studios', largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("START", 150,450,100,50,bright_green, green, "play")
        button("QUIT", 550,450,100,50, bright_red, red, "quit")
        


        pygame.display.update()
        clock.tick(15)



Intro()
pygame.quit()
quit()