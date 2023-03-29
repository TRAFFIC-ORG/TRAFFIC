import pygame
import random
from perceptron import Perceptron
from builderGUI import Builder
from TrafficLights import *
from Car import Car
from Road import Road
import math
import textwrap

import pickle
import os

# constants
# ---------
WIDTH = 1000
HEIGHT = 700
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (0, 0, 255)

# class
# ----------

# Add this class at the beginning of your script


class LogBox:
    def __init__(self, screen, x, y, width, height, font_size=20, max_lines=10):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_size = font_size
        self.max_lines = max_lines
        self.font = pygame.font.Font(None, font_size)
        self.messages = []

    def add_message(self, message):
        # Split the message if it's too long
        wrapped_message = textwrap.fill(message, 20)
        wrapped_lines = wrapped_message.splitlines()

        # Append the wrapped lines to the messages list
        for line in wrapped_lines:
            self.messages.append(line)

        # Remove the oldest message if the list exceeds the maximum number of lines
        while len(self.messages) > self.max_lines:
            self.messages.pop(0)

    def draw(self):
        # Clear the log box area
        log_box_bg_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, (255, 255, 255), log_box_bg_rect)

        # Draw the log box
        log_box_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, (200, 200, 200), log_box_rect, 2)

        # Draw the log messages
        for i, message in enumerate(self.messages):
            text_surface = self.font.render(message, True, (0, 0, 0))
            text_position = (self.x + 5, self.y + i * self.font_size)
            self.screen.blit(text_surface, text_position)


class Button(object):

    # Initialization function
    def __init__(self, position, size, color, text):

        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = pygame.Rect((0, 0), size)

        font = pygame.font.SysFont(None, 32)
        text = font.render(text, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = self.rect.center

        self.image.blit(text, text_rect)

        # set after centering text
        self.rect.topleft = position
    # Function to draw the button

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    # Function to check if the button is pressed

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)

# Function for the first screen


def mainMenu(screen):
    # Creating the buttons
    goToSim = Button((400, 100), (200, 100), RED, "Start Sim")
    goToMapBuilder = Button((400, 220), (200, 100), RED, "Map Builder")
    goToOptions = Button((400, 340), (200, 100), RED, "Options")
    goToSave = Button((400, 460), (200, 100), RED, "Save/Load")
    exitButton = Button((400, 580), (200, 100), RED, "EXIT")

    # Main loop for main menu

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -
        # Checking for events
        for event in pygame.event.get():
            # If someone presses the X in the corner
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # If someone presses escape key
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            # If someone presses the go to sim button
            if goToSim.is_clicked(event):
                # go to simScreen
                simScreen(screen)

            # If someone presses go to options
            if goToOptions.is_clicked(event):
                optionsScreen(screen)

             # If someone presses go to options
            if goToSave.is_clicked(event):
                saveLoadScreen(screen)
            if goToMapBuilder.is_clicked(event):
                mapBuilder(screen)
            # If someone presses the exit button
            if exitButton.is_clicked(event):
                # exit
                pygame.quit()
                exit()

        # Draw all of the buttons on the screen
        screen.fill((255, 255, 255))
        goToSim.draw(screen)
        goToSave.draw(screen)
        goToOptions.draw(screen)
        goToMapBuilder.draw(screen)
        exitButton.draw(screen)
        pygame.display.flip()

        # - FPS -
        clock.tick(FPS)

# Function for the Sim Screen


def simScreen(screen):
    ##############################################

    # params
    vertRoads = 8
    horzRoads = 8
    startX = 150
    startY = 100
    roadIncrementX = 100
    roadIncrementY = 80

    # Creating the dict for nodes as well as the dict for nodePositions and list of nodes
    nodeDict = {}
    nodePositions = {}
    nodes = []

    # Creating the nodes list based on the ammount of vertical and horizontal nodes
    for i in range(vertRoads*horzRoads):
        nodes.append(i)

    # Assign nodes positions based on the number of roads and gaps given
    for node in nodes:
        nodeDict[node] = {}
        nodePositions[node] = [startX + (roadIncrementX * ((node) % horzRoads)), startY + (
            roadIncrementY * math.floor((node) / vertRoads))]

    # Adding nodes to the node dictionary and giving them weight 1
    i = 0
    # horizonally connecting the roads
    for horizonal in range(horzRoads):
        for vertical in range(vertRoads-1):
            nodeDict[vertical+(horizonal*vertRoads)
                     ][vertical+1+(horizonal*vertRoads)] = 1

    for vertical in range(vertRoads):
        for horizontal in range(horzRoads-1):
            nodeDict[(horizontal*horzRoads) +
                     vertical][((horizontal+1)*horzRoads)+vertical] = 1
    print(nodeDict)

    i = 0
    # horizonally connecting the roads
    for horizonal in range(horzRoads):
        for vertical in range(vertRoads-1):
            nodeDict[vertical+(horizonal*vertRoads)
                     ][vertical+1+(horizonal*vertRoads)] = 1
    # horizonally connecting the roads
    for vertical in range(vertRoads):
        for horizontal in range(horzRoads-1):
            nodeDict[(horizontal*horzRoads) +
                     vertical][((horizontal+1)*horzRoads)+vertical] = 1
    print("node dict")
    print(nodeDict)

    # Generate a grid with the nodes and the traffic lights
    grid = TrafficLights(nodes, nodeDict, screen, nodePositions)
    print("Grid.grid")
    print(list(grid.grid))
    print("Node Positions")
    print(grid.nodePositions)

    path = grid.generatePath(0, 37)
    print("path")
    print(path)

    car = Car(grid.nodePositions, 0)
############################################

    simRunning = True
    clock = pygame.time.Clock()
    goBack = Button((5, 25), (120, 40), RED, "Main Menu")
    while simRunning:
        # Checking for events
        for event in pygame.event.get():
            # If someone presses the X in the corner
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
             # If someone presses go to options
            if goBack.is_clicked(event):
                mainMenu(screen)

        screen.fill((255, 255, 255))

        # Draw Screen
        startX = 130
        startY = 80
        road = Road(screen)
        for i in range(vertRoads):
            road.drawSelf(startX, 0, True)
            startX += roadIncrementX

        for i in range(horzRoads):
            road.drawSelf(0, startY, False)
            startY += roadIncrementY

        # Draw the path for the car
        grid.drawNodes(path, 0, 37)

        car.moveCar(path)
        for i in range(len(grid.getNodes())):
            # array = [perceptron.createSum(random.uniform(1,10)),0]
            carsWaiting = random.uniform(1, 10)
            carsWaiting2 = random.uniform(1, 10)
            grid.lightState(i, perceptron.createSum(
                [carsWaiting, carsWaiting2]))

        # Draw the elements on the screen
        goBack.draw(screen)
        car.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


def mapBuilder(screen):
    simRunning = True
    clock = pygame.time.Clock()
    builder = Builder(screen)
    # builder.create_grid()
    goBack = Button((5, 25), (120, 40), RED, "Main Menu")

    log_box = LogBox(screen, screen.get_width() -
                     200, 10, 190, screen.get_height()-500)

    screen.fill((255, 255, 255))
    check = 0  # off
    count = 0
    intersectionList = list(())
    save_count = 0
    save_name_prefix = "map"

    # Load the Road.png sprite
    road_sprite = pygame.image.load("Road.png")

    # New function to draw road sprite between two points
    def draw_road_sprite(node1, node2):
        dx, dy = node2[0] - node1[0], node2[1] - node1[1]
        angle = math.degrees(math.atan2(dy, dx))
        distance = math.sqrt(dx * dx + dy * dy)

        # Change the second value in the tuple to adjust the road's width
        road_sprite_scaled = pygame.transform.scale(
            road_sprite, (int(distance), 20))
        road_sprite_rotated = pygame.transform.rotate(
            road_sprite_scaled, -angle)

        sprite_rect = road_sprite_rotated.get_rect(
            center=((node1[0] + node2[0]) / 2, (node1[1] + node2[1]) / 2))
        screen.blit(road_sprite_rotated, sprite_rect.topleft)

    while simRunning:
        # Checking for events
        for event in pygame.event.get():
            # If someone presses the X in the corner
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

             # If someone presses go to options
            if goBack.is_clicked(event):
                mainMenu(screen)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Handle handle click event
                for button in builder.buttons:
                    if button.is_clicked(event) and button.text == "Intersection" and check == 0:
                        print("Intersection Placement On")
                        log_box.add_message("Intersection Placement On")
                        # Pass log_lines as an argument
                        check = 1  # intersection on
                    elif button.is_clicked(event) and button.text == "Intersection" and check == 1:
                        print("Intersection Placement Off")
                        log_box.add_message("Intersection Placement Off")
                        check = 0  # off
                        pass
                    elif button.is_clicked(event) and button.text == "Road" and check == 0:
                        print("Road Placement On")
                        log_box.add_message("Road Placement On")
                        print("Select First Node")
                        log_box.add_message("Select First Node")
                        check = 2  # road on
                    elif button.is_clicked(event) and button.text == "Road" and check == 2:
                        print("Road Placement Off")
                        log_box.add_message("Road Placement Off")
                        check = 0  # off
                        pass

                    elif button.is_clicked(event) and button.text == "Start":
                        # Check for placed nodes
                        if not intersectionList:
                            print("Nothing to Start")
                            log_box.add_message("Nothing to Start")
                            continue

                        # Start the simulation
                        print("Start button clicked")
                        log_box.add_message("Start button clicked")
                        nodeDict = {}
                        nodePositions = {}
                        nodes = []

                        for i in range(len(intersectionList)):
                            nodes.append(i)

                        i = 0
                        # connect the nodes in the lines
                        # create a mapping from (x, y) tuple to node index
                        node_index = {}
                        for i, intersection in enumerate(intersectionList):
                            rounded_intersection = tuple(
                                map(round, intersection))
                            node_index[rounded_intersection] = i

                        # create nodes list and nodeDict dictionary
                        nodes = list(range(len(intersectionList)))
                        nodeDict = {i: {} for i in nodes}
                        nodePositions = {i: tuple(
                            map(round, intersection)) for i, intersection in enumerate(intersectionList)}

                        # connect the nodes in the lines
                        for line in builder.lines:
                            rounded_line = (
                                tuple(map(round, line[0])), tuple(map(round, line[1])))
                            if rounded_line[0] not in node_index or rounded_line[1] not in node_index:
                                continue
                            node1 = node_index[rounded_line[0]]
                            node2 = node_index[rounded_line[1]]
                            nodeDict[node1][node2] = 1
                            nodeDict[node2][node1] = 1

                            print(f"Connected nodes: {node1} and {node2}")

                        print("Intersection list:", intersectionList)
                        intersectionList = [tuple(
                            map(round, intersection)) for intersection in intersectionList]  # Add this line
                        # You can add this line to check the updated intersectionList
                        print("Rounded Intersection list:", intersectionList)

                        print(nodeDict)
                        print(nodePositions)
                        print("End node index:", len(intersectionList) - 1)
                        grid = TrafficLights(
                            nodes, nodeDict, screen, nodePositions)

                        # Add edges to the graph
                        for i, intersection1 in enumerate(intersectionList):
                            for j, intersection2 in enumerate(intersectionList):
                                if i != j:
                                    distance = math.sqrt(
                                        (intersection1[0] - intersection2[0])**2 + (intersection1[1] - intersection2[1])**2)
                                    grid.addEdge(i, j, distance)

                        print("Grid nodeDict:", nodeDict)
                        print(list(grid.grid))
                        path = grid.generatePath(0, len(intersectionList) - 1)

                        # pass
                    elif button.is_clicked(event) and button.text == "Pause":
                        # Stop the simulation
                        print("Pause button clicked")
                        log_box.add_message("Pause button clicked")
                        pass
                    elif button.is_clicked(event) and button.text == "End":
                        # Pause the simulation
                        print("End button clicked")
                        log_box.add_message("End button clicked")
                        pass
                    elif button.is_clicked(event) and button.text == "List":
                        # Print List
                        for i in intersectionList:
                            log_box.add_message("Hello")

                        print("intersectionList: ", intersectionList)
                        pass

                    elif button.is_clicked(event) and button.text == "Save":
                        # Save Map
                        save_count = 1
                        save_name = save_name_prefix + str(save_count)
                        while os.path.exists(save_name + ".pkl"):
                            save_count += 1
                            save_name = save_name_prefix + str(save_count)
                        data = {
                            "intersectionList": intersectionList,
                            "squares": builder.squares,
                            "lines": builder.lines,
                        }
                        with open(save_name + ".pkl", "wb") as f:
                            pickle.dump(data, f)
                        print(f"Map saved as {save_name}")

                    elif button.is_clicked(event) and button.text == "Load":
                        # Load Map
                        print("Available saves:")
                        for i in range(1, save_count + 1):
                            print(save_name_prefix + str(i))
                        save_to_load = input("Which Save?: ")
                        try:
                            with open(save_to_load + ".pkl", "rb") as f:
                                data = pickle.load(f)
                            intersectionList = data["intersectionList"]
                            builder.squares = data["squares"]
                            builder.lines = data["lines"]

                            # Redraw the loaded map
                            screen.fill((255, 255, 255))
                            for square, type, color in builder.squares:
                                pygame.draw.rect(screen, color, square)
                            for line in builder.lines:
                                # Replace the line drawing with the draw_road_sprite function
                                draw_road_sprite(line[0], line[1])
                            print(f"Loaded {save_to_load}")
                        except FileNotFoundError:
                            print("Map does not exist")

            # Draw Intersection Nodes
            if event.type == pygame.MOUSEBUTTONDOWN and check == 1 and event.pos[1] < 650:
                print("Intersection Place ", event.pos)
                builder.drawNode(event.pos, is_intersection=True)
                intersectionList.append(event.pos)

            # Place a road node
            if event.type == pygame.MOUSEBUTTONDOWN and check == 2:
                for square, type, color in builder.squares:
                    # Check if an intersection node square has been clicked and turn it yellow
                    if square.collidepoint(event.pos) and type == "Intersection" and color == RED:
                        builder.drawNode(square.topleft, is_intersection=True)
                        break
                    # Place a road node
                    elif square.collidepoint(event.pos) and type == "Intersection" and color == YELLOW:
                        if count == 0:
                            point1 = square.center
                            print("Select Second Node")
                            count = 1
                        elif count == 1:
                            point2 = square.center
                            builder.drawLine(point1, point2)
                            count = 0
                        break

        builder.draw_buttons()

        goBack.draw(screen)
        log_box.draw()
        pygame.display.flip()
        clock.tick(FPS)


def optionsScreen(screen):
    optionsRunning = True
    clock = pygame.time.Clock()
    num_sim_options = [1, 10, 20, 50, 100]
    num_sim_index = 0
    sim_num = 1
    goBack = Button((350, 500), (300, 50), RED, "Main Menu")
    show_graphics_button = Button(
        (350, 400), (300, 50), RED, "Show Graphics: No")
    show_graphics = False
    simulations_button = Button(
        (350, 300), (300, 50), RED, "Simulations: " + str(num_sim_options[num_sim_index]))

    while optionsRunning:

        # Checking for events
        for event in pygame.event.get():
            # If someone presses the X in the corner
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

             # If someone presses go to options
            if goBack.is_clicked(event):
                mainMenu(screen)

            if show_graphics_button.is_clicked(event):
                if show_graphics == False and sim_num == 1:
                    show_graphics = True
                    show_graphics_button = Button(
                        (350, 400), (300, 50), RED, "Show Graphics: Yes")
                else:
                    show_graphics = False
                    show_graphics_button = Button(
                        (350, 400), (300, 50), RED, "Show Graphics: No")

            if simulations_button.is_clicked(event):
                if sim_num == 1:
                    sim_num = 10
                    simulations_button = Button(
                        (350, 300), (300, 50), RED, "Simulations: 10")
                elif sim_num == 10:
                    sim_num = 20
                    simulations_button = Button(
                        (350, 300), (300, 50), RED, "Simulations: 20")
                elif sim_num == 20:
                    sim_num = 50
                    simulations_button = Button(
                        (350, 300), (300, 50), RED, "Simulations: 50")
                elif sim_num == 50:
                    sim_num = 100
                    simulations_button = Button(
                        (350, 300), (300, 50), RED, "Simulations: 100")
                elif sim_num == 100:
                    sim_num = 1
                    simulations_button = Button(
                        (350, 300), (300, 50), RED, "Simulations: 1")
                if sim_num > 1:
                    show_graphics = False
                    show_graphics_button = Button(
                        (350, 400), (300, 50), RED, "Show Graphics: No")

            # Draw Screen
            screen.fill((255, 255, 255))
            goBack.draw(screen)
            show_graphics_button.draw(screen)
            simulations_button.draw(screen)
            pygame.display.flip()
            clock.tick(FPS)


def saveLoadScreen(screen, builder):
    # Creating the buttons
    goToMenu = Button((400, 100), (200, 100), RED, "Menu")
    saveButton = Button((400, 340), (200, 100), RED, "Save")
    loadButton = Button((400, 460), (200, 100), RED, "Load")

    save_count = 0
    save_name_prefix = "map"
    # Main loop for save menu

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -
        # Checking for events
        for event in pygame.event.get():
            # If someone presses the X in the corner
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # If someone presses escape key
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            # If someone presses go to menu
            if goToMenu.is_clicked(event):
                mainMenu(screen)

            # If someone presses save the current config and results
            if saveButton.is_clicked(event):
                save_count += 1
                save_name = save_name_prefix + str(save_count)
                data = {
                    "intersectionList": intersectionList,
                    "squares": builder.squares,
                    "lines": builder.lines,
                }
                with open(save_name + ".pkl", "wb") as f:
                    pickle.dump(data, f)
                print(f"Map saved as {save_name}")

            # If someone presses load an existing config and results
            if loadButton.is_clicked(event):
                print("Available saves:")
                for i in range(1, save_count + 1):
                    print(save_name_prefix + str(i))
                save_to_load = input("Which Save?: ")
                with open(save_to_load + ".pkl", "rb") as f:
                    data = pickle.load(f)
                intersectionList = data["intersectionList"]
                builder.squares = data["squares"]
                builder.lines = data["lines"]
                print(f"Loaded {save_to_load}")

        # Draw all of the buttons on the screen
        screen.fill((255, 255, 255))
        goToMenu.draw(screen)
        saveButton.draw(screen)
        loadButton.draw(screen)
        pygame.display.flip()

        # - FPS -
        clock.tick(FPS)


# MAIN LOGIC
# ----------
# Initialize pygame
pygame.init()
# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
perceptron = Perceptron(2)
# Start the sim
mainMenu(screen)
# End the sim
pygame.quit()
