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
runstate = 1
#gameRun = True #Veriable for game while loop to check for input #deleted veriable
mouse = pygame.mouse.get_pos()
font = pygame.font.Font('freesansbold.ttf',32) #creates font object
text1 = font.render('START', True, (255,0,0),(255,255,255,0.7))
text2 = font.render('END', True, (0,0,255),(255,255,255,0.7))

textRect1 = text1.get_rect()
textRect1.center = (x//2,y//2)

textRect2 = text2.get_rect()
textRect2.center = (x//2,y//2)

width = screen.get_width()
height = screen.get_height()
moveNumber = 0
move1 = 0 # 1 = red 2 = green 3 = blue 4 = yellow
move2 = 0
move3 = 0
move4 = 0
move5 = 0
move6 = 0
move7 = 0
move8 = 0

userMove1 = 0
userMove2 = 0
userMove3 = 0
userMove4 = 0
userMove5 = 0
userMove6 = 0
userMove7 = 0
userMove8 = 0



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
    screen.blit(text1,textRect1)

def draw_end():
    pygame.draw.rect(screen,rectColor3, pygame.Rect(230,170,140,60))
    screen.blit(text2,textRect2)

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
    global moveNumber, move1, move2, move3, move4, move5, move6, move7, move8
    randNum = random.randrange(1,5)
    match randNum:
        case 1:
            moveNumber += 1
            print("moveNumber = ",moveNumber)
            if (moveNumber == 1):
                move1 = 1
            elif (moveNumber == 2): 
                move2 = 1
            elif (moveNumber == 3): 
                move3 = 1
            elif (moveNumber == 4): 
                move4 = 1
            elif (moveNumber == 5): 
                move5 = 1
            elif (moveNumber == 6): 
                move6 = 1
            elif (moveNumber == 7): 
                move7 = 1
            elif (moveNumber == 8): 
                move8 = 1
       #     print("Case 1 was activated")
            draw_squares_red()
            pygame.time.wait(1000)
            draw_squares()


        case 2: 
            moveNumber += 1
            print("moveNumber = ",moveNumber)
            if (moveNumber == 1):
                move1 = 2
            elif (moveNumber == 2): 
                move2 = 2
            elif (moveNumber == 3): 
                move3 = 2
            elif (moveNumber == 4): 
                move4 = 2
            elif (moveNumber == 5): 
                move5 = 2
            elif (moveNumber == 6): 
                move6 = 2
            elif (moveNumber == 7): 
                move7 = 2
            elif (moveNumber == 8): 
                move8 = 2
            #print("Case 2 was activated")
            draw_squares_green()
            pygame.time.wait(1000)
            draw_squares()

        case 3: 
            moveNumber += 1
            print("moveNumber = ",moveNumber)
            if (moveNumber == 1):
                move1 = 3
            elif (moveNumber == 2): 
                move2 = 3
            elif (moveNumber == 3): 
                move3 = 3
            elif (moveNumber == 4): 
                move4 = 3
            elif (moveNumber == 5): 
                move5 = 3
            elif (moveNumber == 6): 
                move6 = 3
            elif (moveNumber == 7): 
                move7 = 3
            elif (moveNumber == 8): 
                move8 = 3
        #    print("Case 3 was activated")
            draw_squares_blue()
            pygame.time.wait(1000)
            draw_squares()

        case 4: 
            moveNumber += 1
            print("moveNumber = ",moveNumber)
            if (moveNumber == 1):
                move1 = 4
            elif (moveNumber == 2): 
                move2 = 4
            elif (moveNumber == 3): 
                move3 = 4
            elif (moveNumber == 4): 
                move4 = 4
            elif (moveNumber == 5): 
                move5 = 4
            elif (moveNumber == 6): 
                move6 = 4
            elif (moveNumber == 7): 
                move7 = 4
            elif (moveNumber == 8): 
                move8 = 4
       #     print("Case 4 was activated")
            draw_squares_yellow()
            pygame.time.wait(1000)
            draw_squares()




def draw_game():
    if (moveNumber == 0):
        draw_squares()
        pygame.time.wait(500)
        ran_draw_squares_function()

    elif (moveNumber == 1):
        draw_squares()              #Draws normal squares
        pygame.time.wait(500)
        if (move1 == 1):            #Draws previous move
            draw_squares_red()
        elif (move1 == 2):
            draw_squares_green()
        elif (move1 == 3):
            draw_squares_blue()
        elif (move1 == 4):
            draw_squares_yellow()
        pygame.time.wait(500)
        draw_squares()              #Draws normal squares
        pygame.time.wait(200)
        ran_draw_squares_function() #Draws next move
    
    '''
    elif (moveNumber == 2):
        draw_squares()
        pygame.time.wait(500)
        ran_draw_squares_function()
        '''


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

def get_input1():
    global moveNumber, move1, move2, move3, move4, move5, move6, move7, move8, run
    global userMove1, userMove2, userMove3, userMove4, userMove5, userMove6, userMove7, userMove8
    global gamestate
    #repeatRun = True
    #runstate = 1

    if (moveNumber == 1):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (rectStartX <= mouse[0] <= (rectStartX + rectWidth)) and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                print("Red input worked!")
                userMove1 = 1            
                run = False

            elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth) and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                print("Green input worked!")
                userMove1 = 2
                run = False

            elif (rectStartX <= mouse[0] <= rectStartX + rectWidth) and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                print("Blue input worked!")                
                userMove1 = 3
                run = False

            elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth) and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                print("Yellow input worked!")                
                userMove1 = 4           
                run = False

            else:
                print("I suspect you didn't click near a square")

            if(move1 != userMove1):
                gamestate = 3
                run = False



def get_input2_1():
    global gamestate 
    global run
    global runstate 
    global userMove2
    if (event.type == pygame.MOUSEBUTTONDOWN and runstate == 1):
        if (rectStartX <= mouse[0] <= (rectStartX + rectWidth)) and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
            print("Red input worked!")
            if(move1 != 1):
                gamestate = 3
                run = False
                print("Gamestate = 3 Red get_input2")
            else:
                runstate = 2
                run = False 

        elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth) and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
            print("Green input worked!")
            if(move1 != 2):
                gamestate = 3
                run = False
                print("Gamestate = 3 Green get_input2")
            else:
                runstate = 2  
                run = False                  

        elif (rectStartX <= mouse[0] <= rectStartX + rectWidth) and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
            print("Blue input worked!")
            if(move1 != 3):
                gamestate = 3
                run = False
                print("Gamestate = 3 Blue get_input2")
            else:
                runstate = 2   
                run = False               

        elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth) and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
            print("Yellow input worked!")
            if(move1 != 4):
                gamestate = 3
                run = False
                print("Gamestate = 3 Yellow get_input2")
            else:
                runstate = 2   
                run = False                  

def get_input2_2():
    global gamestate 
    global run
    global runstate 
    global userMove2
    if (event.type == pygame.MOUSEBUTTONDOWN and runstate == 2):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (rectStartX <= mouse[0] <= (rectStartX + rectWidth)) and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                print("Red input worked!")
                userMove2 = 1            
                run = False

            elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth) and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                print("Green input worked!")
                userMove2 = 2
                run = False

            elif (rectStartX <= mouse[0] <= rectStartX + rectWidth) and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                print("Blue input worked!")                
                userMove2 = 3
                run = False

            elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth) and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                print("Yellow input worked!")                
                userMove2 = 4           
                run = False

            else:
                print("I suspect you didn't click near a square")

            if(move2 != userMove2):
                gamestate = 3
                print("Gamestate 3 chance get_input2_2")
                run = False
                



'''
global gamestate
global run
runstate = 1
repeatRun = True
if (moveNumber == 2):
    if event.type == pygame.MOUSEBUTTONDOWN: #Only checks for one click
        while repeatRun:
            if runstate == 1:
                print("runstate = 1")
                if (rectStartX <= mouse[0] <= (rectStartX + rectWidth)) and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                    print("Red input worked!")
                    repeatRun = False
                    if(move1 != 1):
                        print("gamestate 3 activated - get_input_moveNumber2")
                        gamestate = 3
                        repeatRun = False 
                    else:
                        runstate = 2
                        repeatRun = False


                elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth) and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                    print("Green input worked!")
                    repeatRun = False
                    if(move1 != 2):
                        print("gamestate 3 activated - get_input_moveNumber2")
                        gamestate = 3   
                        repeatRun = False                     
                    else: 
                        runstate = 2
                        repeatRun = False
                        

                elif (rectStartX <= mouse[0] <= rectStartX + rectWidth) and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                    print("Blue input worked!")
                    repeatRun = False
                    if(move1 != 3):
                        print("gamestate 3 activated - get_input_moveNumber2")
                        gamestate = 3
                        repeatRun = False
                    else: 
                        runstate = 2 
                        repeatRun = False                           
                    
                elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth) and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                    print("Yellow input worked!")
                    repeatRun = False
                    if(move1 != 4): 
                        print("gamestate 3 activated - get_input_moveNumber2")
                        gamestate = 3
                        repeatRun = False
                    else: 
                        runstate = 2 
                        repeatRun = False                                  

                else:
                    print("I suspect you didn't click near a square")

    #if event.type == pygame.MOUSEBUTTONDOWN:
        if runstate == 2:
            print("runstate = 2")
            if (rectStartX <= mouse[0] <= (rectStartX + rectWidth)) and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                print("Red input worked!")
                userMove2 = 1            
                run = False

            elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth) and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                print("Green input worked!")
                userMove2 = 2
                run = False

            elif (rectStartX <= mouse[0] <= rectStartX + rectWidth) and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                print("Blue input worked!")                
                userMove2 = 3
                run = False

            elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth) and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                print("Yellow input worked!")                
                userMove2 = 4           
                run = False

            else:
                print("I suspect you didn't click near a square")

            if(move2 != userMove2):
                print("move2 gamestate 3 change")
                gamestate = 3
                run = False 
'''

        






    #for i in range(1,9):


    



#pygame.display.flip() #Updates display



#Testing operations ------------------------------------------------------------------------------

#draw_game()

#print("Mouse[0] = ", mouse[0])
#print("Mouse[1] = ", mouse[1])

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

    draw_game() #Drawing start of game #MoveNumber = 0

    while run:                  #Getting fist input or exiting
        clock.tick(FPS) 
        mouse = pygame.mouse.get_pos() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamestate = 4
                run = False
            
            get_input1() #In while loop #moveNumber increments when square is pressed

            if (moveNumber == 8):
                gamestate = 4
                run = False

    if gamestate == 2:
        draw_game() 
        run = True
    '''
    while run2:
        clock.tick(FPS) 
        mouse = pygame.mouse.get_pos() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamestate = 4
                run = False
            
            get_input2_1() #In while loop
            print("runstate = ", runstate)

            if (moveNumber == 8):
                gamestate = 4
                run = False


    pygame.time.wait(4000)
    
    while run:
        clock.tick(FPS) 
        mouse = pygame.mouse.get_pos() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamestate = 4
                run = False
            
            get_input2_2() #In while loop

            if (moveNumber == 8):
                gamestate = 4
                run = False

    if gamestate == 2:
        draw_game() 
        run = True

    '''
    print("move1 = ", move1)
    print("move2 = ", move2)
    print("move3 = ", move3)
    print("move4 = ", move4)

    print("moveNumber = ", moveNumber)
#End menu -----------------------------------------------------------------------------------
run = True
if (gamestate == 3):  
    screen.fill(background_colour) 
    pygame.display.flip()  
    while run:
        clock.tick(FPS)
        draw_end()
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
                    gamestate = 4


#Quit game -----------------------------------------------------------------------------------

run = True
if (gamestate == 4):
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                run = False
                     
        

