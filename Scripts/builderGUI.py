import pygame
from button import Button

WIDTH = 1000
HEIGHT = 700
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (0, 0, 255)


class Square:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.rect = pygame.Rect(x, y, size, size)


class Builder:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = []
        self.squares = []

        # add intersection button to the list of buttons
        intersectionButton = Button(
            (5, 650), (150, 50), WHITE, "Intersection")
        self.buttons.append(intersectionButton)

        # add start button to the list of buttons
        roadButton = Button((155, 650), (100, 50), WHITE, "Road")
        self.buttons.append(roadButton)

        # add start button to the list of buttons
        startButton = Button((255, 650), (100, 50), GREEN, "Start")
        self.buttons.append(startButton)

        # add pause button to the list of buttons
        pauseButton = Button((355, 650), (100, 50), YELLOW, "Pause")
        self.buttons.append(pauseButton)

        # add end button to the list of buttons
        endButton = Button((455, 650), (100, 50), RED, "End")
        self.buttons.append(endButton)

        # add list button to the list of buttons
        listButton = Button((900, 650), (100, 50),
                            (255, 255, 255), "List")
        self.buttons.append(listButton)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # create a new square where the user clicked
                    x, y = pygame.mouse.get_pos()
                    new_square = Square(x, y, 50)
                    self.squares.append(new_square)

        self.display_squares()
        self.draw_buttons()
        pygame.display.update()

    def display_squares(self):
        # draw all the squares on the screen
        for square in self.squares:
            pygame.draw.rect(self.screen, (200, 200, 200), square.rect, 1)

    def draw_buttons(self):
        # draw the menu buttons on the screen
        for button in self.buttons:
            button.draw(self.screen)

    def display_grid(self):
        # draw the grid on the screen
        for row in self.grid:
            for square in row:
                pygame.draw.rect(self.screen, (200, 200, 200), square, 1)
