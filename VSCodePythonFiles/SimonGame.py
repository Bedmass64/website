import pygame



#init variables ------------------------------------------------------------------------------
#init background variables
background_colour = (234,212,252)
screen = pygame.display.set_mode((600,400))

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


#PreRun Operations ------------------------------------------------------------------------------
#Drawn Rectangles
pygame.draw.rect(screen, rectColor1, pygame.Rect(rectStartX,rectStartY,rectWidth,rectHieght))
pygame.draw.rect(screen, rectColor2, pygame.Rect(rectStartX + 70,rectStartY,rectWidth, rectHieght))
pygame.draw.rect(screen, rectColor3, pygame.Rect(rectStartX,rectStartY + 70,rectWidth, rectHieght))
pygame.draw.rect(screen, rectColor4, pygame.Rect(rectStartX + 70,rectStartY + 70,rectWidth, rectHieght))

pygame.display.flip() #Updates display



#Run operations ------------------------------------------------------------------------------


#Start menu -----------------------------------------------------------------------------------
#NEEDS MENU (check gamestate before run)

#Game menu -----------------------------------------------------------------------------------
run = True
clock = pygame.time.Clock()
while run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


    