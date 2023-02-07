import pygame
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
pygame.init()


size = (1300, 900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("TRAFFIC")


# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
 
#Creating class for the screen
class Screen:
    def __init__(self, title, size, fill=WHITE):
        self.title = title
        self.size = size
        self.isActive = False
        self.fill = WHITE
    
    def makeActiveScreen(self):
        pygame.display.set_caption(self.title)
        self.isActive = True
        self.screen = pygame.display.set_mode(self.size)

    def screenUpdate(self):
        if (self.isActive):
            self.screen.fill(self.fill)
    def endScreen(self):
        self.isActive = False
    def checkActive(self):
        #self.fill = fill
        return self.isActive


#Creating class for the button
class Button:
    #Initializing the button
    def __init__(self, text, pos, font, bg="black"):
         self.x, self.y = pos
         self.font = pygame.font.SysFont("Arial", font)
         self.changeText(text, bg)

    #Method for changing the text based on what you want
    def changeText(self, text, bg="black"):
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    #Method for showing the button
    def show(self):
        screen.blit(self.surface, (self.x,self.y))

    #Method for when the button is clicked
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if self.rect.collidepoint(x, y):
                return True
            else:
                return False


# -------- Main Program Loop -----------
mainScreen = Screen("Main", (1200, 900))
testScreen = Screen("Test", (1000, 400))
window = mainScreen.makeActiveScreen()
button1 = Button("Test", (100,100), font=30, bg="navy")


while carryOn:
    # --- Main event loop
    mainScreen.screenUpdate()

    button1.show()

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we can exit the while loop
        if mainScreen.checkActive():
            buttonPressed = button1.click(event)
        if buttonPressed:
            testScreen.makeActiveScreen()
            mainScreen.endScreen()



    
            
            
     # --- Game logic should go here
 
     # --- Drawing code should go here
     #
     #We should add a background immage here
    
    pygame.display.update()
    #The you can draw different shapes and lines or add text to your background stage.
    


    # --- Go ahead and update the screen with what we've drawn.
    

    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:

pygame.quit()
print("hello")