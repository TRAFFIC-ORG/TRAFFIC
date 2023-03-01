import sys
import pygame as pg

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
BLUE = (0,0,255)
class TrafficLights(object):
    def __init__(self, nodes, initGrid, screen, nodePositions):
        self.nodes = nodes
        self.grid = self.constructGrid(nodes, initGrid)
        self.screen = screen
        self.nodePositions = nodePositions

    #This function creates the grid from the list of nodes
    def constructGrid(self, nodes, initGrid):
        grid = {}
        for node in nodes:
            grid[node] = {}

        grid.update(initGrid)
        #This loop ensures that for all nodes A->B with a value V, B->A has the same value V
        for node, edges in grid.items():
            for touchingNode, value in edges.items():
                if grid[touchingNode].get(node, False) == False:
                    grid[touchingNode][node] = value
        return grid
    #Gets the nodes on the grid
    def getNodes(self):
        return self.nodes

    #Return the values of the connecting nodes to the node
    def getOutGoingNodes(self, node):
        connectingNodes = []
        for outGoingNode in self.nodes:
            if self.grid[node].get(outGoingNode,False) != False:
                connectingNodes.append(outGoingNode)
        return connectingNodes
    
    def getValues(self, node1, node2):
        return self.grid[node1][node2]

    def generatePath(self, startingNode, endNode):
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
                currValue = temp_path[currentShortestNode] + self.getValues(currentShortestNode, neighbor)
                if currValue < temp_path[neighbor]:
                    temp_path[neighbor] = currValue
                    visitedNodes[neighbor] = currentShortestNode
            unvisitedNodes.remove(currentShortestNode)

        path = []
        temp_node = endNode
        print("Visited Nodes")
        print(visitedNodes)
        while temp_node != startingNode:
            path.append(temp_node)
            temp_node = visitedNodes[temp_node]
        
        path.append(startingNode)
        
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
            else:
                pg.draw.circle(self.screen, RED, pos, 10)
