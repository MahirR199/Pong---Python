import pygame
import time
import sys
import random
import pickle

pygame.init() #Tells pygame to start running its codes

#Global variable declarations
borderx = 0
bordery = 0
borderWidth = 800
borderHeight = 600
borderThick = 10
LEFT = 1
RIGHT = 3
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
BLUE  = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
gameMenuBackground = pygame.image.load('background.png') #Setting up background
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT)) #Setting how big the screen is
clock = pygame.time.Clock() #Setting up a clock
 
def win(): #If user reaches the victory point of game
    gameDisplay.fill(BLACK)
    messageDisplay('YOU WIN', 115, DISPLAY_HEIGHT//2, DISPLAY_WIDTH//2)
    pygame.display.update()
    time.sleep(1.5)
    
    
def fps(): #Gets how much frames the game is running at and displays message
    messageDisplay(str(clock.get_fps()//1), 25, 760, 20)

def score(points): #Displays the score
    messageDisplay(('Score: ' + str(points)), 25, 60, 20)
    
def paused(): #Function used when player presses P to pause
    pause = True
    while pause:
        for event in pygame.event.get(): #For any thing user enters/does
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: #If any mouse button clicked
                if 150 + 100 >mouse[0] > 150 and 450+50>mouse[1]>450 and event.button == LEFT: #If mouse button click is left click on buttons
                    pause = False
                    return False
                elif 550+100 > mouse[0] > 550 and 450+50>mouse[1]>450 and event.button == LEFT:
                    pause = False
                    return True
                elif 350+100>mouse[0] > 350 and 450+50>mouse[1]>450 and event.button == LEFT:
                    pauseRules()
                    

        gameDisplay.fill(BLACK) #Background is black
        border(borderx,bordery,borderWidth,borderHeight,borderThick) #Redraws border
        mouse = pygame.mouse.get_pos() #Giving mouse x and y values from user mouse position
        pygame.draw.rect(gameDisplay, GREEN, (150, 450, 100, 50)) #Drawing rectangles
        pygame.draw.rect(gameDisplay, RED, (550, 450, 100, 50))
        pygame.draw.rect(gameDisplay, (255,69,0), (350, 450, 100, 50)) 
        messageDisplay('RESUME', 20, 200, 476) #Printing messages
        messageDisplay('MENU', 20, 600, 476)
        messageDisplay('RULES', 20, 400, 476) 
        
        
        pygame.display.update()
        
def pauseRules(): #For displaying rules with pause function
    info = True
    while info:
        for event in pygame.event.get(): #Anything the user enters/does
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: #If the user types anything
                if event.key == pygame.K_ESCAPE: #If the user presses escape it returns
                    info = False
                    return
        
        
                    
        gameDisplay.blit(gameMenuBackground,(0,0)) #Draws background on background
        messageDisplay('To move up and down', 30, 400, 50) #Printing messages
        messageDisplay('Use the up and down arrow keys', 30, 400, 100)
        messageDisplay('While in game press ''P'' to pause', 30, 400, 150)
        if pauseBack():
            return
        pygame.display.update()

def pauseBack(): #Back button to exit pause function
    back = True
    while back:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 7 + 50 > mouse[0] > 7 and 7+25 > mouse[1] > 7 and event.button == LEFT:
                    back = False
                    return True
                    
        mouse = pygame.mouse.get_pos()
        pygame.draw.rect(gameDisplay, (0,125,0), (7, 7, 50, 25))
        messageDisplay('<<<', 26, 30, 18)
        pygame.display.update()
def back(): #back button to exit other function example: rules
    back = True
    while back:
        for event in pygame.event.get(): #For each event user does
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: #If user presses a mouse button
                if 7 + 50 > mouse[0] > 7 and 7+25 > mouse[1] > 7 and event.button == LEFT: #Checks if user left clicks button where message is displayed and rectangle is displayed
                    back = False
                    game_intro()
                    
        mouse = pygame.mouse.get_pos()
        pygame.draw.rect(gameDisplay, (0,125,0), (7, 7, 50, 25))
        messageDisplay('<<<', 26, 30, 18)
        pygame.display.update()
    

def crash(crashSound): #Plays crash sound
    pygame.mixer.Sound.play(crashSound)
    time.sleep(1)
    pygame.mixer.Sound.stop(crashSound)
    
    
    
    
def rules(): #Displays rules when is called
    info = True
    while info:
        for event in pygame.event.get(): #For each event user does
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: #If user presses a mouse button
                if event.key == pygame.K_ESCAPE: #If user pressed escape
                    game_intro()
                    
                    
        
                    
                    
        gameDisplay.blit(gameMenuBackground,(0,0))
        messageDisplay('To move up and down', 30, 400, 50)
        messageDisplay('Use the up and down arrow keys', 30, 400, 100)
        messageDisplay('While in game press ''P'' to pause', 30, 400, 150)
        back()
        pygame.display.update()
        
def messageDisplay(text, fontSize, xcoord, ycoord): #Print messages at desired font size and at selected x and y coordinates
    largeText = pygame.font.Font('freesansbold.ttf', fontSize) 
    textSurf, textRect = textObjects(text, largeText)
    textRect.center = (xcoord, ycoord) 
    gameDisplay.blit(textSurf, textRect)
    
def playButtonShape(): #Creates play button, rules button, and quit button.
    pygame.draw.rect(gameDisplay, (0,170,0), (50, 450, 100, 50)) #Play button shape
    pygame.draw.rect(gameDisplay, (170,0,0), (650, 450, 100, 50)) #How to play
    pygame.draw.rect(gameDisplay, (0,0,170), (350, 450, 100, 50)) #Quit

def textObjects(text, font): 
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def lifeScore(lives): #Writes the lives in the bottom left corner
    font= pygame.font.SysFont(None, 25)
    text = font.render("Lives: " + str(lives), True, GREEN)
    gameDisplay.blit(text, (10,550))

def ball(ballx, bally, radius): #Draws the ball
    pygame.draw.circle(gameDisplay, WHITE, [ballx, bally], radius) 

def paddle(x, y, paddleWidth, paddleHeight, points): #Draws the paddle
    if points <255: 
        pygame.draw.rect(gameDisplay, (255,255-points,0), (x, y, paddleWidth, paddleHeight))#Keeps getting closer to red each time score goes up

    if points >=255:
        pygame.draw.rect(gameDisplay, (255, 0, 0), (x,y,paddleWidth,paddleHeight)) #Paddle becomes red when score is 255 and greater
        
        

def border(borderx, bordery, borderWidth, borderHeight, borderThick): #Draws a border around the screen
    pygame.draw.rect(gameDisplay, GREEN, (borderx, bordery, borderWidth, borderHeight), borderThick)

     

def game_intro(): #Calls other functions to create a main menu.
    intro = True
    pickle_in = open("dict.pickle" , "rb")
    highscore = pickle.load(pickle_in) 
    while intro:
        
        for event in pygame.event.get(): #Any event the user does
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: #If event is mouse click
                if 100 + 50 > mouse[0] > 50 and 450+50 > mouse[1] > 450 and event.button == LEFT: #If mouse over button play and is left clicked, function game loop is called
                    intro = False
                    gameLoop()
                if 400 + 50 > mouse[0] > 350 and 450 + 50 > mouse[1] > 450 and event.button == LEFT: #If mous over button rules and is left clicked, function rules is called
                    rules()
                if 700 + 50 > mouse[0] > 650 and 450+50 > mouse[1] > 450 and event.button == LEFT: #If mouse over button quit and is left clicked, exits out of game
                    pygame.quit()
                    sys.exit()
        
        gameDisplay.blit(gameMenuBackground,(0,0))
        messageDisplay('Pong', 115, DISPLAY_WIDTH//2, DISPLAY_HEIGHT//2)
        messageDisplay(('Highscore: '+ str(highscore)), 25, 400, 400)
        playButtonShape()
        mouse = pygame.mouse.get_pos()
        

        if 100 + 50 > mouse[0] > 50 and 450+50 > mouse[1] > 450: #Mouse position over play, box becomes highlighted
            pygame.draw.rect(gameDisplay, GREEN, (50, 450, 100, 50))
            messageDisplay('PLAY', 25, 100, 475)
            messageDisplay('RULES', 25, 400, 475)
            messageDisplay('QUIT', 25, 700, 475)
        else:
            pygame.draw.rect(gameDisplay, (0,170,0), (50, 450, 100, 50))
            messageDisplay('PLAY', 25, 100, 475)
            messageDisplay('RULES', 25, 400, 475)
            messageDisplay('QUIT', 25, 700, 475)

        if 400 + 50 > mouse[0] > 350 and 450 + 50 > mouse[1] > 450: #Mouse position over rules, box becomes highlighted
            pygame.draw.rect(gameDisplay, (BLUE), (350,450,100,50))
            messageDisplay('PLAY', 25, 100, 475)
            messageDisplay('RULES', 25, 400, 475)
            messageDisplay('QUIT', 25, 700, 475)
        else:
            pygame.draw.rect(gameDisplay, (0,0,170), (350,450,100,50))
            messageDisplay('PLAY', 25, 100, 475)
            messageDisplay('RULES', 25, 400, 475)
            messageDisplay('QUIT', 25, 700, 475)

        if 700 + 50 > mouse[0] > 650 and 450+50 > mouse[1] > 450: #Mouse position over quit, box becomes highlighted
            pygame.draw.rect(gameDisplay,(RED), (650, 450, 100, 50))
            messageDisplay('PLAY', 25, 100, 475)
            messageDisplay('RULES', 25, 400, 475)
            messageDisplay('QUIT', 25, 700, 475)
        else:
            pygame.draw.rect(gameDisplay,(170,0,0), (650, 450, 100, 50))
            messageDisplay('PLAY', 25, 100, 475)
            messageDisplay('RULES', 25, 400, 475)
            messageDisplay('QUIT', 25, 700, 475)
        pygame.display.update()
            
            
def gameLoop(): #Runs main game by calling other functions
    #Local variable declarations
    x = 760
    y = (DISPLAY_HEIGHT*0.38)
    points = 0
    ballx = DISPLAY_WIDTH // 2
    bally = DISPLAY_HEIGHT // 2
    ballxVelocity = random.randint(2,3)
    ballyVelocity = random.randint(2,3)
    radius = 12
    lives = 3
    paddleWidth = 1.5
    paddleHeight = 160
    yVelocity = 0
    pickle_in = open("dict.pickle" , "rb")
    highscore = pickle.load(pickle_in)

    goal = False
    
    crashSound = pygame.mixer.Sound("crash.wav")
    
    gameExit = False
    
    while gameExit != True:
        
        
        
        for event in pygame.event.get(): #Any event user does
            if event.type == pygame.QUIT:
                if points > highscore:
                    pickle_out = open("dict.pickle", "wb")
                    pickle.dump(points, pickle_out)
                    pickle_out.close()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: #If user presses button
                if event.key == pygame.K_UP: #Up arrow pressed
                    yVelocity = -2.2
                elif event.key == pygame.K_DOWN: #Down arrow pressed
                    yVelocity = 2.2
                elif event.key == pygame.K_p or event.key == pygame.K_ESCAPE: #If p is pressed, pauses game.
                    if paused():
                        if points > highscore:
                            pickle_out = open("dict.pickle", "wb")
                            pickle.dump(points, pickle_out)
                            pickle_out.close()
                        game_intro()
                        gameLoop()
            if event.type == pygame.KEYUP: #If button is stopped being pressed
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    yVelocity = 0
        if y-borderThick < 0 and yVelocity < 0: #If paddle tries going off screen stops it
            yVelocity = 0
        elif y > DISPLAY_HEIGHT - paddleHeight - borderThick and yVelocity > 0: 
            yVelocity = 0
        elif bally > DISPLAY_HEIGHT - radius - borderThick:
            ballyVelocity *= -1
            
            
        elif bally - radius < borderThick: #If ball hits edge, bounces
            ballyVelocity *= -1
           
            
        elif ballx >= DISPLAY_WIDTH-radius-borderThick: #When it hits wall
            lives -= 1
            time.sleep(1)
            ballx = DISPLAY_WIDTH // 2
            bally = DISPLAY_HEIGHT // 2
            x = 760
            y = (DISPLAY_HEIGHT*0.38)
            
        if bally+radius >= y and bally-radius <= y+paddleHeight: #When ball is equal or greater than paddle y and less than or equal to paddle y + height of paddle.
            if ballx + radius == x: #If ball + radius is equal to x of paddle, change direction of x movement of ball
                ballxVelocity = random.randint(-3,-2)
                if points <10:
                    points += 1
                if points>=10 and points<20:
                    points += 2
                if points>=20 and points<30:
                    points += 5
                if points>=30 and points < 255:
                    points += 10
                if points >= 255:
                    points += 100
        elif ballx + radius >= x and ballx <= x+paddleWidth: #If right of ball x is > left side of paddle x and left of ball x is less than right side of paddle x.
            if bally+radius == y: #If bottom of ball = y(top) of paddle
                ballyVelocity *= -1
                ballxVelocity *= -1
                if points <10:
                    points += 1
                if points>=10 and points<20:
                    points += 2
                if points>=20 and points<30:
                    points += 5
                if points>=30 and points < 255:
                    points += 10
                if points >= 255:
                    points += 100
            elif bally-radius == y+paddleHeight: #If top of ball hits bottom side of paddle(y+paddleHeight)
                ballyVelocity*=-1
                ballxVelocity*=-1
                if points <10:
                    points += 1
                if points>=10 and points<20:
                    points += 2
                if points>=20 and points<30:
                    points += 5
                if points>=30 and points < 255:
                    points += 10
                if points >= 255:
                    points += 100
          
        if goal == False: #If goal is reached statement becomes false
            scores = points
        else:
            scores = 0
        
        if lives == 0: #If player lives equal to 0
            crash(crashSound)
            messageDisplay('GAME OVER', 115, DISPLAY_WIDTH//2, DISPLAY_HEIGHT//2)
            pygame.display.update()
            time.sleep(2)
            lives = 3
            points = 0
            game_intro()
        if ballx-radius < borderThick: #If ball hits wall, bounces
            ballxVelocity *= -1
        if scores == 660:
            win()
            goal = True
        
        
            
                
                
        #Adding speed from if statements and calling functions to draw different things on screen
        ballx += ballxVelocity
        bally += ballyVelocity
        y += yVelocity
        gameDisplay.fill(BLACK)
        border(borderx, bordery, borderWidth, borderHeight, borderThick)
        lifeScore(lives)
        score(points)
        fps()
        paddle(x, y, paddleWidth, paddleHeight, points) 
        ball(ballx, bally, radius)
        pygame.display.update()
        clock.tick(240) #Fps max is 240, making the ideal experience at 240
    
        
game_intro() #Game intro only function called, main function as it calls all other functions including gameLoop()



