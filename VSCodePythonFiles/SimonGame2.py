#Imports ---------------------------------------------------
import pygame
import random 

pygame.init()

#Veriables ---------------------------------------------------
#For simplicity:
red = 1
green = 2
blue = 3
yellow = 4

#Move assignments:
move1 = 0
move2 = 0
move3 = 0
move4 = 0
move5 = 0
move6 = 0
move7 = 0
move8 = 0


x = 600
y = 400
screen = pygame.display.set_mode((x,y)) #Start screen
background_colour = (234,212,252)
screen.fill(background_colour)
gamestate = 1
clock = pygame.time.Clock() #Clock? Yes
#runstate = 1
moveNumber = 0

mouse = pygame.mouse.get_pos()

font = pygame.font.Font('freesansbold.ttf',32) #creates font object
text1 = font.render('START', True, (255,0,0),(255,255,255,0.7)) #Renders words to text
text2 = font.render('END', True, (0,0,255),(255,255,255,0.7))

textRect1 = text1.get_rect()       #Renders rectangle fo text
textRect1.center = (x//2,y//2)

textRect2 = text2.get_rect()
textRect2.center = (x//2,y//2)

width = screen.get_width()  
height = screen.get_height()

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

#Rect demensions
rectWidth = 60
rectHieght = 60 
rectStartX = 230
rectStartY = 130


#Def functions -----------------------------------------------------------

def draw_red_square():
    pygame.draw.rect(screen, rectColor1, pygame.Rect\
        (rectStartX,rectStartY,rectWidth,rectHieght))

def draw_red_square_alt():
    pygame.draw.rect(screen, rectColor1a, pygame.Rect\
        (rectStartX,rectStartY,rectWidth,rectHieght))

def draw_green_square():
    pygame.draw.rect(screen, rectColor2, pygame.Rect\
        (rectStartX + 70,rectStartY,rectWidth, rectHieght))

def draw_green_square_alt():
    pygame.draw.rect(screen, rectColor2a, pygame.Rect\
        (rectStartX + 70,rectStartY,rectWidth, rectHieght))

def draw_blue_square():
    pygame.draw.rect(screen, rectColor3, pygame.Rect\
        (rectStartX,rectStartY + 70,rectWidth, rectHieght))

def draw_blue_square_alt():
    pygame.draw.rect(screen, rectColor3a, pygame.Rect\
        (rectStartX,rectStartY + 70,rectWidth, rectHieght))

def draw_yellow_square():
    pygame.draw.rect(screen, rectColor4, pygame.Rect\
        (rectStartX + 70,rectStartY + 70,rectWidth, rectHieght))  

def draw_yellow_square_alt():
    pygame.draw.rect(screen, rectColor4a, pygame.Rect\
        (rectStartX + 70,rectStartY + 70,rectWidth, rectHieght))  

def draw_squares():
    screen.fill(background_colour) 
    draw_red_square()
    draw_green_square()
    draw_blue_square()
    draw_yellow_square()
    pygame.display.update()

def draw_squares_red():
    screen.fill(background_colour) 
    draw_red_square_alt()
    draw_green_square()
    draw_blue_square()
    draw_yellow_square()
    pygame.display.update()

def draw_squares_green():
    screen.fill(background_colour) 
    draw_red_square()
    draw_green_square_alt()
    draw_blue_square()
    draw_yellow_square()
    pygame.display.update()

def draw_squares_blue():
    screen.fill(background_colour) 
    draw_red_square()
    draw_green_square()
    draw_blue_square_alt()
    draw_yellow_square()
    pygame.display.update()
    
def draw_squares_yellow():
    screen.fill(background_colour) 
    draw_red_square()
    draw_green_square()
    draw_blue_square()
    draw_yellow_square_alt()
    pygame.display.update()

#draw start function
def draw_start():
    global mouse, gamestate
    run = True
    while (run):
        mouse = pygame.mouse.get_pos()
        #clock.tick(FPS)        UNCOMMENT LATER 
        pygame.draw.rect(screen,rectColor1, pygame.Rect(230,170,140,60))
        screen.blit(text1,textRect1)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if ((width/2) - 60) <= mouse[0] <= ((width/2) + 60)\
                    and ((height/2) - 30) <= mouse[1] <= ((height/2) + 30):
                    run = False         #Cancels loop 
                    gamestate = 2



#draw game function

def draw_game():
    global mouse

    if (moveNumber == 0):
        draw_squares()
        pygame.time.wait(200)
        draw_random_square()
        get_input1()
        print("moveNumber in loop is", moveNumber)

    if (moveNumber == 1):
        draw_squares()
        pygame.time.wait(200)
        printMove1()
        pygame.time.wait(200)
        draw_random_square()
        get_input2() #if input is wrong code gamestate change
        print("moveNumber in loop is", moveNumber)

    if (moveNumber == 2):
        draw_squares()
        pygame.time.wait(200)
        printMove1()
        pygame.time.wait(200)
        printMove2()
        pygame.time.wait(200)
        draw_random_square()
        get_input3()

    if (moveNumber == 3):
        draw_squares()
        pygame.time.wait(200)
        printMove1()
        pygame.time.wait(200)
        printMove2()
        pygame.time.wait(200)
        printMove3()
        pygame.time.wait(200)
        draw_random_square()
        get_input4()

    if (moveNumber == 4):
        draw_squares()
        pygame.time.wait(200)
        printMove1()
        pygame.time.wait(200)
        printMove2()
        pygame.time.wait(200)
        printMove3()
        pygame.time.wait(200)
        printMove4()
        pygame.time.wait(200)
        draw_random_square()
        get_input5()

    if (moveNumber == 5):
        draw_squares()
        pygame.time.wait(200)
        printMove1()
        pygame.time.wait(200)
        printMove2()
        pygame.time.wait(200)
        printMove3()
        pygame.time.wait(200)
        printMove4()
        pygame.time.wait(200)
        printMove5()
        pygame.time.wait(200)
        draw_random_square()
        get_input6()

    if (moveNumber == 6):
        draw_squares()
        pygame.time.wait(200)
        printMove1()
        pygame.time.wait(200)
        printMove2()
        pygame.time.wait(200)
        printMove3()
        pygame.time.wait(200)
        printMove4()
        pygame.time.wait(200)
        printMove5()
        pygame.time.wait(200)
        printMove6()
        pygame.time.wait(200)
        draw_random_square()
        get_input7()

    if (moveNumber == 7):
        draw_squares()
        pygame.time.wait(200)
        printMove1()
        pygame.time.wait(200)
        printMove2()
        pygame.time.wait(200)
        printMove3()
        pygame.time.wait(200)
        printMove4()
        pygame.time.wait(200)
        printMove5()
        pygame.time.wait(200)
        printMove6()
        pygame.time.wait(200)
        printMove7()
        pygame.time.wait(200)
        draw_random_square()
        get_input8()

    if(moveNumber == 8):
        print("You win!")




def printMove1():
        if (move1 == red):
            draw_squares_red()

        elif (move1 == green):
            draw_squares_green()

        elif (move1 == blue):
            draw_squares_blue()

        elif (move1 == yellow):
            draw_squares_yellow()
        pygame.time.wait(200)
        draw_squares()

def printMove2():
        if (move2 == red):
            draw_squares_red()

        elif (move2 == green):
            draw_squares_green()

        elif (move2 == blue):
            draw_squares_blue()

        elif (move2 == yellow):
            draw_squares_yellow()
        pygame.time.wait(200)
        draw_squares()

def printMove3():
        if (move3 == red):
            draw_squares_red()

        elif (move3 == green):
            draw_squares_green()

        elif (move3 == blue):
            draw_squares_blue()

        elif (move3 == yellow):
            draw_squares_yellow()
        pygame.time.wait(200)
        draw_squares()

def printMove4():
        if (move4 == red):
            draw_squares_red()

        elif (move4 == green):
            draw_squares_green()

        elif (move4 == blue):
            draw_squares_blue()

        elif (move4 == yellow):
            draw_squares_yellow()
        pygame.time.wait(200)
        draw_squares()

def printMove5():
        if (move5 == red):
            draw_squares_red()

        elif (move5 == green):
            draw_squares_green()

        elif (move5 == blue):
            draw_squares_blue()

        elif (move5 == yellow):
            draw_squares_yellow()
        pygame.time.wait(200)
        draw_squares()

def printMove6():
        if (move6 == red):
            draw_squares_red()

        elif (move6 == green):
            draw_squares_green()

        elif (move6 == blue):
            draw_squares_blue()

        elif (move6 == yellow):
            draw_squares_yellow()
        pygame.time.wait(200)
        draw_squares()

def printMove7():
        if (move7 == red):
            draw_squares_red()

        elif (move7 == green):
            draw_squares_green()

        elif (move7 == blue):
            draw_squares_blue()

        elif (move7 == yellow):
            draw_squares_yellow()
        pygame.time.wait(200)
        draw_squares()




def get_input1():
    userMove1Check()

def get_input2():
    userMove1Check()
    userMove2Check()

def get_input3():
    userMove1Check()
    userMove2Check()
    userMove3Check()

def get_input4():
    userMove1Check()
    userMove2Check()
    userMove3Check()
    userMove4Check()

def get_input5():
    userMove1Check()
    userMove2Check()
    userMove3Check()
    userMove4Check()
    userMove5Check()

def get_input6():
    userMove1Check()
    userMove2Check()
    userMove3Check()
    userMove4Check()
    userMove5Check()
    userMove6Check()

def get_input7():
    userMove1Check()
    userMove2Check()
    userMove3Check()
    userMove4Check()
    userMove5Check()
    userMove6Check()
    userMove7Check()

def get_input8():
    userMove1Check()
    userMove2Check()
    userMove3Check()
    userMove4Check()
    userMove5Check()
    userMove6Check()
    userMove7Check()
    userMove8Check()
    


def userMove1Check(): #Move to after input 2 after wrighting function
#Get the right input for the move number 
#This only works for the first input of the second move 
    run = True
    global userMove1, gamestate

    #Loop that gets mouse input
    while(run):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Check if red is clicked
                if (rectStartX <= mouse[0] <= (rectStartX + rectWidth)) \
                    and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                        print("Red input worked!")
                        userMove1 = red #Returns "if red is clicked" (kindof returns result)   
                        run = False #Exits out of input loop
                

                #Check if green is clicked  
                elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth)\
                    and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                        print("Green input worked!")
                        userMove1 = green #Returns "if green is clicked" (kindof returns result)   
                        run = False
                
                #Check if blue is clicked
                elif (rectStartX <= mouse[0] <= rectStartX + rectWidth)\
                    and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                        print("Blue input worked!")                
                        userMove1 = blue #Returns "if blue is clicked" (kindof returns result)   
                        run = False
                #Check if yellow is clicked
                elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth)\
                    and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                        print("Yellow input worked!")                
                        userMove1 = yellow #Returns "if yellow is clicked" (kindof returns result)       
                        run = False        
                
                if (userMove1 != move1):
                    gamestate = 3
                    run = False

                if event.type == pygame.QUIT:
                    gamestate = 4
                    run = False

def userMove2Check():#Move to after input 2 after wrighting function
#Get the right input for the move number 
#This only works for the first input of the second move 
    run = True
    global userMove2, gamestate

    #Loop that gets mouse input
    while(run):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Check if red is clicked
                if (rectStartX <= mouse[0] <= (rectStartX + rectWidth)) \
                    and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                        print("Red input worked!")
                        userMove2 = red #Returns "if red is clicked" (kindof returns result)   
                        run = False #Exits out of input loop

                #Check if green is clicked  
                elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth)\
                    and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                        print("Green input worked!")
                        userMove2 = green #Returns "if green is clicked" (kindof returns result)   
                        run = False
                
                #Check if blue is clicked
                elif (rectStartX <= mouse[0] <= rectStartX + rectWidth)\
                    and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                        print("Blue input worked!")                
                        userMove2 = blue #Returns "if blue is clicked" (kindof returns result)   
                        run = False
                #Check if yellow is clicked
                elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth)\
                    and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                        print("Yellow input worked!")                
                        userMove2 = yellow #Returns "if yellow is clicked" (kindof returns result)       
                        run = False        
                
                if event.type == pygame.QUIT:
                    gamestate = 4
                    run = False

def userMove3Check(): #Move to after input 2 after wrighting function
#Get the right input for the move number 
#This only works for the first input of the second move 
    run = True
    global userMove3, gamestate

    #Loop that gets mouse input
    while(run):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Check if red is clicked
                if (rectStartX <= mouse[0] <= (rectStartX + rectWidth)) \
                    and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                        print("Red input worked!")
                        userMove3 = red #Returns "if red is clicked" (kindof returns result)   
                        run = False #Exits out of input loop

                #Check if green is clicked  
                elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth)\
                    and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                        print("Green input worked!")
                        userMove3 = green #Returns "if green is clicked" (kindof returns result)   
                        run = False
                
                #Check if blue is clicked
                elif (rectStartX <= mouse[0] <= rectStartX + rectWidth)\
                    and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                        print("Blue input worked!")                
                        userMove3 = blue #Returns "if blue is clicked" (kindof returns result)   
                        run = False
                #Check if yellow is clicked
                elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth)\
                    and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                        print("Yellow input worked!")                
                        userMove3 = yellow #Returns "if yellow is clicked" (kindof returns result)       
                        run = False        
                
                if event.type == pygame.QUIT:
                    gamestate = 4
                    run = False

def userMove4Check(): #Move to after input 2 after wrighting function
#Get the right input for the move number 
#This only works for the first input of the second move 
    run = True
    global userMove4, gamestate

    #Loop that gets mouse input
    while(run):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Check if red is clicked
                if (rectStartX <= mouse[0] <= (rectStartX + rectWidth)) \
                    and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                        print("Red input worked!")
                        userMove4 = red #Returns "if red is clicked" (kindof returns result)   
                        run = False #Exits out of input loop

                #Check if green is clicked  
                elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth)\
                    and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                        print("Green input worked!")
                        userMove4 = green #Returns "if green is clicked" (kindof returns result)   
                        run = False
                
                #Check if blue is clicked
                elif (rectStartX <= mouse[0] <= rectStartX + rectWidth)\
                    and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                        print("Blue input worked!")                
                        userMove4 = blue #Returns "if blue is clicked" (kindof returns result)   
                        run = False
                #Check if yellow is clicked
                elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth)\
                    and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                        print("Yellow input worked!")                
                        userMove4 = yellow #Returns "if yellow is clicked" (kindof returns result)       
                        run = False        
                
                if event.type == pygame.QUIT:
                    gamestate = 4
                    run = False

def userMove5Check(): #Move to after input 2 after wrighting function
#Get the right input for the move number 
#This only works for the first input of the second move 
    run = True
    global userMove5, gamestate

    #Loop that gets mouse input
    while(run):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Check if red is clicked
                if (rectStartX <= mouse[0] <= (rectStartX + rectWidth)) \
                    and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                        print("Red input worked!")
                        userMove5 = red #Returns "if red is clicked" (kindof returns result)   
                        run = False #Exits out of input loop

                #Check if green is clicked  
                elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth)\
                    and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                        print("Green input worked!")
                        userMove5 = green #Returns "if green is clicked" (kindof returns result)   
                        run = False
                
                #Check if blue is clicked
                elif (rectStartX <= mouse[0] <= rectStartX + rectWidth)\
                    and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                        print("Blue input worked!")                
                        userMove5 = blue #Returns "if blue is clicked" (kindof returns result)   
                        run = False
                #Check if yellow is clicked
                elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth)\
                    and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                        print("Yellow input worked!")                
                        userMove5 = yellow #Returns "if yellow is clicked" (kindof returns result)       
                        run = False        
                
                if event.type == pygame.QUIT:
                    gamestate = 4
                    run = False

def userMove6Check(): #Move to after input 2 after wrighting function
#Get the right input for the move number 
#This only works for the first input of the second move 
    run = True
    global userMove6, gamestate

    #Loop that gets mouse input
    while(run):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Check if red is clicked
                if (rectStartX <= mouse[0] <= (rectStartX + rectWidth)) \
                    and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                        print("Red input worked!")
                        userMove6 = red #Returns "if red is clicked" (kindof returns result)   
                        run = False #Exits out of input loop

                #Check if green is clicked  
                elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth)\
                    and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                        print("Green input worked!")
                        userMove6 = green #Returns "if green is clicked" (kindof returns result)   
                        run = False
                
                #Check if blue is clicked
                elif (rectStartX <= mouse[0] <= rectStartX + rectWidth)\
                    and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                        print("Blue input worked!")                
                        userMove6 = blue #Returns "if blue is clicked" (kindof returns result)   
                        run = False
                #Check if yellow is clicked
                elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth)\
                    and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                        print("Yellow input worked!")                
                        userMove6 = yellow #Returns "if yellow is clicked" (kindof returns result)       
                        run = False        
                
                if event.type == pygame.QUIT:
                    gamestate = 4
                    run = False

def userMove7Check(): #Move to after input 2 after wrighting function
#Get the right input for the move number 
#This only works for the first input of the second move 
    run = True
    global userMove7, gamestate

    #Loop that gets mouse input
    while(run):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Check if red is clicked
                if (rectStartX <= mouse[0] <= (rectStartX + rectWidth)) \
                    and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                        print("Red input worked!")
                        userMove7 = red #Returns "if red is clicked" (kindof returns result)   
                        run = False #Exits out of input loop

                #Check if green is clicked  
                elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth)\
                    and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                        print("Green input worked!")
                        userMove7 = green #Returns "if green is clicked" (kindof returns result)   
                        run = False
                
                #Check if blue is clicked
                elif (rectStartX <= mouse[0] <= rectStartX + rectWidth)\
                    and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                        print("Blue input worked!")                
                        userMove7 = blue #Returns "if blue is clicked" (kindof returns result)   
                        run = False
                #Check if yellow is clicked
                elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth)\
                    and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                        print("Yellow input worked!")                
                        userMove7 = yellow #Returns "if yellow is clicked" (kindof returns result)       
                        run = False        
                
                if event.type == pygame.QUIT:
                    gamestate = 4
                    run = False

def userMove8Check(): #Move to after input 2 after wrighting function
#Get the right input for the move number 
#This only works for the first input of the second move 
    run = True
    global userMove8, gamestate

    #Loop that gets mouse input
    while(run):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Check if red is clicked
                if (rectStartX <= mouse[0] <= (rectStartX + rectWidth)) \
                    and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                        print("Red input worked!")
                        userMove8 = red #Returns "if red is clicked" (kindof returns result)   
                        run = False #Exits out of input loop

                #Check if green is clicked  
                elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth)\
                    and (rectStartY <= mouse[1] <= rectStartY + rectWidth):
                        print("Green input worked!")
                        userMove8 = green #Returns "if green is clicked" (kindof returns result)   
                        run = False
                
                #Check if blue is clicked
                elif (rectStartX <= mouse[0] <= rectStartX + rectWidth)\
                    and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                        print("Blue input worked!")                
                        userMove8 = blue #Returns "if blue is clicked" (kindof returns result)   
                        run = False
                #Check if yellow is clicked
                elif (rectStartX + 70 <= mouse[0] <= rectStartX + 70 + rectWidth)\
                    and (rectStartY + 70 <= mouse[1] <= rectStartY + 70 + rectWidth):
                        print("Yellow input worked!")                
                        userMove8 = yellow #Returns "if yellow is clicked" (kindof returns result)       
                        run = False        
                
                if event.type == pygame.QUIT:
                    gamestate = 4
                    run = False
    




def draw_end():
    global mouse, gamestate
    run = True
    while (run):
        mouse = pygame.mouse.get_pos()
        #clock.tick(FPS)        UNCOMMENT LATER 
        pygame.draw.rect(screen,rectColor3, pygame.Rect(230,170,140,60))
        screen.blit(text2,textRect2)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if ((width/2) - 60) <= mouse[0] <= ((width/2) + 60)\
                    and ((height/2) - 30) <= mouse[1] <= ((height/2) + 30):
                    run = False         #Cancels loop 
                    gamestate = 2


def draw_random_square():
    #This method hilights a random square on the screen for half a second and records the move
    #to the respective veriable

    #Move number only increments when this method is called which is once per move
    global moveNumber, move1, move2, move3, move4, move5, move6, move7, move8
    randNum = random.randrange(1,5)
    match randNum:
        case 1:
            moveNumber += 1
            #print("moveNumber = ",moveNumber)      Use for debugging later then delete
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
            pygame.time.wait(200)
            draw_squares()


        case 2: 
            moveNumber += 1
            #print("moveNumber = ",moveNumber)
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
            pygame.time.wait(200)
            draw_squares()

        case 3: 
            moveNumber += 1
            #print("moveNumber = ",moveNumber)
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
            #print("Case 3 was activated")
            draw_squares_blue()
            pygame.time.wait(200)
            draw_squares()

        case 4: 
            moveNumber += 1
            #print("moveNumber = ",moveNumber)
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
            #print("Case 4 was activated")
            draw_squares_yellow()
            pygame.time.wait(200)
            draw_squares()


#Start screen ------------------------------------------------------------

if (gamestate == 1):
    draw_start()

#Game screen -------------------------------------------------------------

if (gamestate == 2):
    draw_game()

#Eng screen -------------------------------------------------------------

if (gamestate == 3):
    draw_end()

#Quit screen -------------------------------------------------------------
#MAYBE DELETE 
run = True
if (gamestate == 4):
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                run = False


print("move1 = ", move1)
print("move2 = ", move2)
print("move3 = ", move3)

print("userMove1 = ", userMove1)
print("userMove2 = ", userMove2)