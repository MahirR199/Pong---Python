import random
import time
import pygame
#Tells the program to start using pygame stuff
pygame.init()

#Dimensions of the box
DISPLAY_WIDTH = 1280 #All caps means constant, dont change it, stays the same
DISPLAY_HEIGHT = 1024
WHITE = (255, 255, 255) #rgb vals limit 256 due to it being 8 bits so we go 1 down
BLACK = (0, 0, 0)
CAR_WIDTH = 73

#Create window with those dimensions
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
#Names the window    
pygame.display.set_caption("DAB <o/!")
#Sets up a clock for fps
clock = pygame.time.Clock()
carImg = pygame.image.load('racecar.png')
def obstaclesDodged(count):
    font= pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(count), True, BLACK)
    gameDisplay.blit(text, (1200,0))
def car(x, y):
    gameDisplay.blit(carImg, (x, y)) #Tells the program to put the variable at those coordinates

def textObjects(text, font):  #Creating an invisible rect that holds text
    textSurface = font.render(text, True, BLACK)   #text surface filled with some font
    return textSurface, textSurface.get_rect()
def welcomeText(text, font):
    welcomeMes = font.render(text, True, WHITE)
    return welcomeMes, welcomeMes.get_rect()
def crash():
    messageDisplay('You Crashed!') #When user crashes, message displays

def welcomeMessage():
    
    gameDisplay.fill(WHITE)
    welcomeDisplay('Welcome to yayeet123')
    time.sleep(2)
    
def welcomeDisplay(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115) 
    textSurf, textRect = textObjects(text, largeText)
    textRect.center = ((DISPLAY_WIDTH/2), (DISPLAY_HEIGHT/2)) 
    gameDisplay.blit(textSurf, textRect) #Put it on the screen
    pygame.display.update() #Redraw everything on screen; Refreshes
    time.sleep(2) #Time delay; waits for 2 seconds to do next task
    return
    
def obstacles(obstacleX, obstacleY, obstacleWidth, obstacleHeight, colour):
    pygame.draw.rect(gameDisplay, colour, (obstacleX, obstacleY, obstacleWidth, obstacleHeight))
def messageDisplay(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115) #Font type to use and size
    textSurf, textRect = textObjects(text, largeText)
    textRect.center = ((DISPLAY_WIDTH/2), (DISPLAY_HEIGHT/2)) #Text origin is right in the middle, Putting font in middle
    gameDisplay.blit(textSurf, textRect) #Put it on the screen
    pygame.display.update() #Redraw everything on screen; Refreshes
    time.sleep(2) #Time delay; waits for 2 seconds to do next task
    gameLoop() #Restarts game
    
def gameLoop():
    x = (DISPLAY_WIDTH * 0.45) #Origin is at top left of the screen
    y = (DISPLAY_HEIGHT * 0.9)
    dodged = 0
    xVelocity = 0
    obstacleStartX = random.randrange(0, DISPLAY_WIDTH)
    obstacleStartY = -600
    obstacleSpeed = 10 + dodged
    obstacleWidth = 100
    obstacleHeight = 100
    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    i = int()
    gameExit = False
    
    while gameExit == False:
        
        for event in pygame.event.get():     #go through all events(anything user inputs)
            if event.type == pygame.QUIT:    #if the user quit
                pygame.quit()                #close display
                quit()
            if event.type == pygame.KEYDOWN: #If someone presses a button on the keyboard
                if event.key == pygame.K_a:
                    xVelocity = -5 - dodged
                elif event.key == pygame.K_d:
                    xVelocity = 5 + dodged
            if event.type == pygame.KEYUP: #when we let go we want to change velocity back to 0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    xVelocity = 0
        x+= xVelocity
        gameDisplay.fill(WHITE) #fills colour with rgb values
        while i == 0:
            colour = (r,g,b)
            i = 2 
        obstacles(obstacleStartX, obstacleStartY, obstacleWidth, obstacleHeight, colour)
        obstacleStartY = obstacleStartY + obstacleSpeed
        car(x, y)
        obstaclesDodged(dodged)

        if x>DISPLAY_WIDTH - CAR_WIDTH or x<0:
            crash()
            gameExit = True
        if obstacleStartY > DISPLAY_HEIGHT:
            r = random.randrange(0,255)
            g = random.randrange(0,255)
            b = random.randrange(0,255)
            obstacleStartY = 0-obstacleHeight
            obstacleStartX = random.randrange(0, DISPLAY_WIDTH)
            dodged+=1
            colour = (r, g, b)
        if y < obstacleStartY + obstacleHeight:
            if (x > obstacleStartX and x< obstacleStartX + obstacleWidth) or (x+CAR_WIDTH>obstacleStartX and x + CAR_WIDTH < obstacleStartX + obstacleWidth):
                crash()
        pygame.display.update() #refreshes the screen
        clock.tick(60) #How rapidly to load the frames (60FPS)
gameLoop()      

