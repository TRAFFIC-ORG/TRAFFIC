import pygame
from button import Button

WIDTH = 1000
HEIGHT = 700
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Builder:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = []
        self.grid = []

    def create_grid(self):
        # create a 2D grid of squares for placing intersections
        for i in range(6):
            row = []
            for j in range(8):
                square = pygame.Rect(j * 100 + 125, i * 100 + 75, 50, 50)
                row.append(square)
            self.grid.append(row)

        # add intersection button to the list of buttons
        intersectionButton = Button(
            (5, 650), (150, 50), (255, 0, 0), "Intersection")
        self.buttons.append(intersectionButton)

        # add start button to the list of buttons
        startButton = Button((155, 650), (100, 50), (0, 255, 0), "Start")
        self.buttons.append(startButton)

        # add pause button to the list of buttons
        pauseButton = Button((255, 650), (100, 50), (0, 0, 255), "Pause")
        self.buttons.append(pauseButton)

        # add end button to the list of buttons
        endButton = Button((355, 650), (100, 50), (255, 255, 0), "End")
        self.buttons.append(endButton)

        # add intersection points to the grid
        for i, row in enumerate(self.grid):
            for j, square in enumerate(row):
                center = (square.centerx, square.centery)
                pygame.draw.circle(self.screen, BLACK, center, 5)

    def display_grid(self):
        # draw the grid on the screen
        for row in self.grid:
            for square in row:
                pygame.draw.rect(self.screen, (200, 200, 200), square, 1)

    def draw_buttons(self):
        # draw the menu buttons on the screen
        for button in self.buttons:
            button.draw(self.screen)

    def handle_click(self, event):
        # handle button clicks
        for button in self.buttons:
            if button.is_clicked(event):
                print(button.text)

        # handle intersection placement
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, row in enumerate(self.grid):
                for j, square in enumerate(row):
                    if square.collidepoint(event.pos):
                        print("Intersection placed at", i, j)

    def handle_hover(self, event):
        # highlight button on hover
        for button in self.buttons:
            if button.rect.collidepoint(event.pos):
                button.image.fill((200, 200, 200))
            # else:
                # button.image.fill(button.RED)
