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


class Builder:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = []
        self.squares = []
        self.lines = []

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

        # add map save button
        mapSaveButton = Button((700, 650), (100, 50),
                               (255, 255, 255), "Save")
        self.buttons.append(mapSaveButton)

        # add map load button
        mapLoadButton = Button((800, 650), (100, 50),
                               (255, 255, 255), "Load")
        self.buttons.append(mapLoadButton)

        # # add intersection removal button
        # removeButton = Button((600, 650), (100, 50),
        #                       (255, 255, 255), "Remove")
        # self.buttons.append(removeButton)

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

    # def drawNode(self, pos):
    #     # create a Rect object at the specified position
    #     node_square = pygame.Rect(pos[0], pos[1], 15, 15)
    #     # append the new node to the list
    #     self.squares.append(node_square)
    #     # draw the node on the screen
    #     pygame.draw.rect(self.screen, RED, node_square)
    #     # pygame.draw.rect(self.screen, RED, (x, y, 15, 15))

    def drawNode(self, pos, is_intersection):
        if is_intersection:
            node_type = "Intersection"
        else:
            node_type = "Road"

        # create a Rect object at the specified position
        node_square = pygame.Rect(pos[0], pos[1], 15, 15)
        # append the new node to the list
        self.squares.append((node_square, node_type, RED))
        # draw the node on the screen
        for square, type, color in self.squares:
            pygame.draw.rect(self.screen, color, square)

        # check if a node square has been clicked and toggle its color
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]
        for i, (square, type, color) in enumerate(self.squares):
            if square.collidepoint(mouse_pos) and mouse_clicked:
                if color == RED:
                    self.squares[i] = (square, type, YELLOW)
                else:
                    self.squares[i] = (square, type, RED)
                break

    def drawLine(self, node1, node2):
        pygame.draw.line(self.screen, (255, 0, 0), node1, node2)
        self.lines.append((node1, node2))
