import sys
import pygame as pg
import queue
import Car

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class TrafficLights(object):
    #Initilization function
    def __init__(self, nodes, initGrid, screen, nodePositions):
        self.nodes = nodes #list of nodes that exist in the simulations
        self.grid = self.constructGrid(nodes, initGrid) #Grid is a collection of all the nodes formed into a grid
        self.screen = screen #Screen that is defined in main 
        self.nodePositions = nodePositions #List of the node positions
        self.que = queue.Queue() #A queue object that will exist on each traffic light

    # This function creates the grid from the list of nodes
    def constructGrid(self, nodes, initGrid):
        #Add all of the nodes to the grid list
        grid = {}
        for node in nodes:
            grid[node] = {}

        
        grid.update(initGrid)
        # This loop ensures that for all nodes A->B with a value V, B->A has the same value V
        for node, edges in grid.items():
            for touchingNode, value in edges.items():
                if grid[touchingNode].get(node, False) == False:
                    grid[touchingNode][node] = value
        return grid

    def getNodes(self):
        return self.nodes

    # Return the values of the connecting nodes to the node
    def getOutGoingNodes(self, node):
        connectingNodes = []
        for outGoingNode in self.nodes:
            if self.grid[node].get(outGoingNode, False) != False:
                connectingNodes.append(outGoingNode)
        return connectingNodes
    # Returns the value of the edge between two nodes

    def getValues(self, node1, node2):
        return self.grid[node1][node2]

    def generatePath(self, startingNode, endNode):
        print("Starting node:", startingNode)
        print("End node:", endNode)
        print("Nodes:", self.nodes)
        print("Graph:", self.grid)

        unvisitedNodes = list(self.nodes)
        temp_path = {}
        visitedNodes = {}
        for node in unvisitedNodes:
            temp_path[node] = float('inf')
        temp_path[startingNode] = 0
        while unvisitedNodes:
            currentShortestNode = None
            for node in unvisitedNodes:
                if currentShortestNode == None:
                    currentShortestNode = node
                elif temp_path[node] < temp_path[currentShortestNode]:
                    currentShortestNode = node

            neighboringNodes = self.getOutGoingNodes(currentShortestNode)
            for neighbor in neighboringNodes:
                currValue = temp_path[currentShortestNode] + \
                    self.getValues(currentShortestNode, neighbor)
                if currValue < temp_path[neighbor]:
                    temp_path[neighbor] = currValue
                    visitedNodes[neighbor] = currentShortestNode
            unvisitedNodes.remove(currentShortestNode)

        # if endNode not in visitedNodes:
        #     raise ValueError("End node is not a valid node in the graph")

        path = []
        temp_node = endNode
        print("Visited Nodes")
        print(visitedNodes)
        while temp_node != startingNode:
            path.append(temp_node)
            temp_node = visitedNodes[temp_node]

        path.append(startingNode)
        path.reverse()

        return path

    def drawNodes(self, path, startNode, endNode):
        for node in self.nodes:
            pos = self.nodePositions[node]
            if node == startNode:
                pg.draw.circle(self.screen, WHITE, pos, 10)
            elif node == endNode:
                pg.draw.circle(self.screen, BLUE, pos, 10)
            elif node in path:
                pg.draw.circle(self.screen, GREEN, pos, 10)

    def lightState(self, node, north):
        pos = self.nodePositions[node]
        if north == 1:
            # Set the north and south lights to green
            # North and South
            pg.draw.line(self.screen, GREEN,
                         (pos[0]-15, pos[1]-19), (pos[0]+15, pos[1]-19), 5)
            pg.draw.line(self.screen, GREEN,
                         (pos[0]-15, pos[1]+19), (pos[0]+15, pos[1]+19), 5)
            pg.draw.line(self.screen, RED,
                         (pos[0]-19, pos[1]-15), (pos[0]-19, pos[1]+15), 5)
            pg.draw.line(self.screen, RED,
                         (pos[0]+19, pos[1]-15), (pos[0]+19, pos[1]+15), 5)
        else:
            # Set the west and east lights to green
            pg.draw.line(self.screen, RED,
                         (pos[0]-15, pos[1]-19), (pos[0]+15, pos[1]-19), 5)
            pg.draw.line(self.screen, RED,
                         (pos[0]-15, pos[1]+19), (pos[0]+15, pos[1]+19), 5)
            pg.draw.line(self.screen, GREEN,
                         (pos[0]-19, pos[1]-15), (pos[0]-19, pos[1]+15), 5)
            pg.draw.line(self.screen, GREEN,
                         (pos[0]+19, pos[1]-15), (pos[0]+19, pos[1]+15), 5)

    def addEdge(self, node1, node2, weight):
        # Add this line
        print(f"Adding edge between {node1} and {node2} with weight {weight}")
        if node1 not in self.grid:
            self.grid[node1] = {}
        if node2 not in self.grid:
            self.grid[node2] = {}
        self.grid[node1][node2] = weight
        self.grid[node2][node1] = weight

    #Function to add a car to the queue 
    def addToQue(self, car):
        queue.put(car)

    #Function to remove a car from the queue
    def removeFromQue(self):
        car = queue.get()
        car.nextNode()

    def printQue(self):
        print(queue)
