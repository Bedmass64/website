from ast import Str
import string
import pygame
import sys
pygame.init()



#init variables ------------------------------------------------------------------------------
#init background variables
x = 600
y = 400
screen = pygame.display.set_mode((x,y))
background_colour = (234,212,252)
gamestate = 1
clock = pygame.time.Clock()
run = True
mouse = pygame.mouse.get_pos()
font = pygame.font.Font('freesansbold.ttf',32) #creates font object
text = font.render('START', True, (255,0,0),(255,255,255,0.7))
textRect = text.get_rect()
textRect.center = (x//2,y//2)
width = screen.get_width()
height = screen.get_height()


#mixer.init()
#sound=mixer.Sound("bell.wav")
#sound.play()

#Regular square colors 
rectColor1 = (255,0,0) #Rect color1 - Red
rectColor2 = (0,255,0) #Rect color2 - Green
rectColor3 = (0,0,255) #Rect color3 - Blue 
rectColor4 = (255,255,0) #Rect color4 - Yellow


#Activation colors
rectColor1a = (255,0,0,0.5) #Rect color1a - Red
rectColor2a = (0,255,0,0.5) #Rect color2a - Green
rectColor3a = (0,0,255,0.5) #Rect color3a - Blue 
rectColor4a = (255,255,0,0.5) #Rect color4a - Yellow

pygame.display.set_caption("Simon")

screen.fill(background_colour) #Fill background colour to the screen

rectWidth = 60
rectHieght = 60 
rectStartX = 230
rectStartY = 130

FPS = 60



#Testing Operations ------------------------------------------------------------------------------
print('Hi')
print("Mouse[0] =", mouse[0])
#PreRun Operations ------------------------------------------------------------------------------
#Drawn Rectangles

def draw_squares():
    pygame.display.flip()
    pygame.draw.rect(screen, rectColor1, pygame.Rect(rectStartX,rectStartY,rectWidth,rectHieght))
    pygame.draw.rect(screen, rectColor2, pygame.Rect(rectStartX + 70,rectStartY,rectWidth, rectHieght))
    pygame.draw.rect(screen, rectColor3, pygame.Rect(rectStartX,rectStartY + 70,rectWidth, rectHieght))
    pygame.draw.rect(screen, rectColor4, pygame.Rect(rectStartX + 70,rectStartY + 70,rectWidth, rectHieght))

def draw_start():
    pygame.draw.rect(screen,rectColor1, pygame.Rect(230,170,140,60))
    screen.blit(text,textRect)

#pygame.display.flip() #Updates display



#Run operations ------------------------------------------------------------------------------


#Start menu -----------------------------------------------------------------------------------
#NEEDS MENU (check gamestate before run)


while run:
    if (gamestate == 1):    
        clock.tick(FPS)
        draw_start()
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        #  print("Mouse[0]", mouse[0])
        #  print("Mouse[1]", mouse[1])
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False


            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ((width/2) - 60) <= mouse[0] <= ((width/2) + 60) and ((height/2) - 30) <= mouse[1] <= ((height/2) + 30):
                    gamestate = 2
                    
                        
                    #pygame.quit() # gamestate = 2
                    # screen.fill(1,3,2)
                    # print("Hi hehe") 

                




#Game menu -----------------------------------------------------------------------------------
    if (gamestate == 2):    
        clock.tick(FPS)  
        draw_squares()
        pygame.display.update() #Updates display

        for event in pygame.event.get():
 
            if event.type == pygame.QUIT:
                run = False



        