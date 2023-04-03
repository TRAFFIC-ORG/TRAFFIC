import pygame
class Car(object):
    def __init__(self, nodePositions, startingNode, path):
        self.carImg = pygame.image.load('Car.png')
        self.carImg = pygame.transform.scale(self.carImg, (25, 15))
        self.speed = 5
        self.startingNode = startingNode
        self.nodePositions = nodePositions
        print("Node positions in car" )
        print(self.nodePositions)
        self.pos = self.nodePositions[startingNode]
        self.posX = self.pos[0]
        self.posY = self.pos[1]
        self.path = path
    def drawSelf(self,screen):
        screen.blit(self.carImg, (0,0))
    #function to move the car along the path that is passed to the car
    def moveCar(self ):
        print(self.path)
        print(self.nodePositions[self.path[1]])
        self.posX = self.nodePositions[self.path[1]]
        self.posY = self.nodePositions[self.path[1]]

    def draw(self, surface):
        surface.blit(self.carImg, (self.posX, self.posY))

