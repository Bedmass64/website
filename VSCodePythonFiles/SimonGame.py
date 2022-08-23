#from ast import Str
import string
import pygame
import sys
import random


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
#gameRun = True #Veriable for game while loop to check for input #deleted veriable
mouse = pygame.mouse.get_pos()
font = pygame.font.Font('freesansbold.ttf',32) #creates font object
text = font.render('START', True, (255,0,0),(255,255,255,0.7))
textRect = text.get_rect()
textRect.center = (x//2,y//2)
width = screen.get_width()
height = screen.get_height()
move1 = 0
move2 = 0
move3 = 0
move4 = 0
move5 = 0
move6 = 0
move7 = 0
move8 = 0


#mixer.init()
#sound=mixer.Sound("bell.wav")
#sound.play()

#Regular square colors 
rectColor1 = (255,0,0) #Rect color1 - Red
rectColor2 = (0,255,0) #Rect color2 - Green
rectColor3 = (0,0,255) #Rect color3 - Blue 
rectColor4 = (255,255,0) #Rect color4 - Yellow


#Activation colors
rectColor1a = (175,0,0,0.5) #Rect color1a - Red
rectColor2a = (0,155,0,0.5) #Rect color2a - Green
rectColor3a = (0,0,125,0.5) #Rect color3a - Blue 
rectColor4a = (175,175,0,0.5) #Rect color4a - Yellow
rectColorTEST = (122,122,122) #Gray color 

pygame.display.set_caption("Simon")

screen.fill(background_colour) #Fill background colour to the screen

rectWidth = 60
rectHieght = 60 
rectStartX = 230
rectStartY = 130

FPS = 60



#Testing Operations ------------------------------------------------------------------------------
#print('Hi')
#print("Mouse[0] =", mouse[0])
#PreRun Operations ------------------------------------------------------------------------------
#Drawn Rectangles

def draw_start():
    pygame.draw.rect(screen,rectColor1, pygame.Rect(230,170,140,60))
    screen.blit(text,textRect)

def draw_squares():
    screen.fill(background_colour) 
    pygame.display.flip()
    pygame.draw.rect(screen, rectColor1, pygame.Rect(rectStartX,rectStartY,rectWidth,rectHieght))
    pygame.draw.rect(screen, rectColor2, pygame.Rect(rectStartX + 70,rectStartY,rectWidth, rectHieght))
    pygame.draw.rect(screen, rectColor3, pygame.Rect(rectStartX,rectStartY + 70,rectWidth, rectHieght))
    pygame.draw.rect(screen, rectColor4, pygame.Rect(rectStartX + 70,rectStartY + 70,rectWidth, rectHieght))
    pygame.display.update()

def draw_squares_red():
    screen.fill(background_colour) 
    pygame.display.flip()
    pygame.draw.rect(screen, rectColor1a, pygame.Rect(rectStartX,rectStartY,rectWidth,rectHieght))
    pygame.draw.rect(screen, rectColor2, pygame.Rect(rectStartX + 70,rectStartY,rectWidth, rectHieght))
    pygame.draw.rect(screen, rectColor3, pygame.Rect(rectStartX,rectStartY + 70,rectWidth, rectHieght))
    pygame.draw.rect(screen, rectColor4, pygame.Rect(rectStartX + 70,rectStartY + 70,rectWidth, rectHieght))
    pygame.display.update()

def draw_squares_green():
    screen.fill(background_colour) 
    pygame.display.flip()
    pygame.draw.rect(screen, rectColor1, pygame.Rect(rectStartX,rectStartY,rectWidth,rectHieght))
    pygame.draw.rect(screen, rectColor2a, pygame.Rect(rectStartX + 70,rectStartY,rectWidth, rectHieght))
    pygame.draw.rect(screen, rectColor3, pygame.Rect(rectStartX,rectStartY + 70,rectWidth, rectHieght))
    pygame.draw.rect(screen, rectColor4, pygame.Rect(rectStartX + 70,rectStartY + 70,rectWidth, rectHieght))
    pygame.display.update()

def draw_squares_blue():
    screen.fill(background_colour) 
    pygame.display.flip()
    pygame.draw.rect(screen, rectColor1, pygame.Rect(rectStartX,rectStartY,rectWidth,rectHieght))
    pygame.draw.rect(screen, rectColor2, pygame.Rect(rectStartX + 70,rectStartY,rectWidth, rectHieght))
    pygame.draw.rect(screen, rectColor3a, pygame.Rect(rectStartX,rectStartY + 70,rectWidth, rectHieght))
    pygame.draw.rect(screen, rectColor4, pygame.Rect(rectStartX + 70,rectStartY + 70,rectWidth, rectHieght))
    pygame.display.update()

def draw_squares_yellow():
    screen.fill(background_colour) 
    pygame.display.flip()
    pygame.draw.rect(screen, rectColor1, pygame.Rect(rectStartX,rectStartY,rectWidth,rectHieght))
    pygame.draw.rect(screen, rectColor2, pygame.Rect(rectStartX + 70,rectStartY,rectWidth, rectHieght))
    pygame.draw.rect(screen, rectColor3, pygame.Rect(rectStartX,rectStartY + 70,rectWidth, rectHieght))
    pygame.draw.rect(screen, rectColor4a, pygame.Rect(rectStartX + 70,rectStartY + 70,rectWidth, rectHieght))
    pygame.display.update()

def ran_draw_squares_function():
    randNum = random.randrange(1,5)
    match randNum:
        case 1:
            print("Case 1 was activated")
            draw_squares_red()
            pygame.time.wait(1000)
            draw_squares()

        case 2: 
            print("Case 2 was activated")
            draw_squares_green()
            pygame.time.wait(1000)
            draw_squares()

        case 3: 
            print("Case 3 was activated")
            draw_squares_blue()
            pygame.time.wait(1000)
            draw_squares()

        case 4: 
            print("Case 4 was activated")
            draw_squares_yellow()
            pygame.time.wait(1000)
            draw_squares()




def draw_game():
    draw_squares()
    pygame.time.wait(1000)
    ran_draw_squares_function()

'''
def get_input():
    gameRun = True
    while gameRun: 
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRun = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rectStartX <= mouse[0] <= rectStartX + 60 and rectStartY <= mouse[1] <= rectStartY + 60:
                    print("It worked! (kinda)")
                    gameRun = False
                    #---------------------------------------
                    while run:
                        for event in pygame.event.get():

                            if event.type == pygame.QUIT:
                                run = False


                            
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if ((width/2) - 60) <= mouse[0] <= ((width/2) + 60) and ((height/2) - 30) <= mouse[1] <= ((height/2) + 30):
                    run = False
                    '''

    #for i in range(1,9):


    



#pygame.display.flip() #Updates display



#Testing operations ------------------------------------------------------------------------------

#draw_game()

#Start menu -----------------------------------------------------------------------------------
#NEEDS MENU (check gamestate before run)

if gamestate == 1:
    while run:
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
                    run = False
                    gamestate = 2
                     
                    #pygame.quit() # gamestate = 2
                   # screen.fill(1,3,2)
                  # print("Hi hehe") 

                




#Game menu -----------------------------------------------------------------------------------
run = True
if (gamestate == 2):    
    #draw_squares()
    #draw_squares_yellow()
    #ran_draw_squares_function()

    draw_game()

    while run:
        clock.tick(FPS)  
       # pygame.display.update() #Updates display
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            



        