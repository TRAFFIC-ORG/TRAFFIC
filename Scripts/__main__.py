import pygame

#constants
#---------
WIDTH = 1000
HEIGHT = 700
FPS = 60
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

#class
#----------

class Button(object):

    #Initialization function
    def __init__(self, position, size, color, text):

        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = pygame.Rect((0,0), size)

        font = pygame.font.SysFont(None, 32)
        text = font.render(text, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = self.rect.center

        self.image.blit(text, text_rect)

        # set after centering text
        self.rect.topleft = position
    #Function to draw the button
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    #Function to check if the button is pressed
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)

#Function for the first screen
def mainMenu(screen):
    #Creating the buttons
    goToSim = Button((400, 200), (200, 100), RED, "Start Sim")
    goToOptions = Button((400, 320), (200,100), RED, "Options")
    goToSave = Button((400, 440), (200, 100), RED, "Save/Load")
    exitButton = Button((400, 560), (200, 100), RED, "EXIT")

    # Main loop for main menu

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -
        #Checking for events
        for event in pygame.event.get():
            #If someone presses the X in the corner
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #If someone presses escape key
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            #If someone presses the go to sim button
            if goToSim.is_clicked(event):
                # go to simScreen
                simScreen(screen)
            
            #If someone presses go to options
            if goToOptions.is_clicked(event):
                optionsScreen(screen)
            
             #If someone presses go to options
            if goToSave.is_clicked(event):
                saveLoadScreen(screen)

            #If someone presses the exit button
            if exitButton.is_clicked(event):
                # exit
                pygame.quit()
                exit()

        #Draw all of the buttons on the screen
        screen.fill((255,255,255))    
        goToSim.draw(screen)
        goToSave.draw(screen)
        goToOptions.draw(screen)
        exitButton.draw(screen)
        pygame.display.flip()

        # - FPS -
        clock.tick(FPS)

#Function for the Sim Screen
def simScreen(screen):
    simRunning = True
    clock = pygame.time.Clock()
    goBack = Button((5, 25), (120, 40), RED, "Main Menu")
    while simRunning:
        #Checking for events
        for event in pygame.event.get():
            #If someone presses the X in the corner
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
             #If someone presses go to options
            if goBack.is_clicked(event):
                mainMenu(screen)
        
        screen.fill((255,255,255))   
        vertRoads = 8;
        horizontalRoads = 6;
        #Draw Screen
        currentX = 150;
        for i in range(vertRoads):
            pygame.draw.line(screen, BLACK, [currentX, 0], [currentX, HEIGHT], 40)
            currentX += 100

        currentY = 100;
        for i in range(horizontalRoads):
            pygame.draw.line(screen, BLACK, [0, currentY], [WIDTH, currentY], 40)
            currentY += 100
        
        goBack.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

def optionsScreen(screen):
    pass

def saveLoadScreen(screen):
    pass

# MAIN LOGIC
# ----------
#Initialize pygame
pygame.init()
#Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#Start the sim
mainMenu(screen)
#End the sim
pygame.quit()