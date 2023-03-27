import pygame
class Car(object):
    def __init__(self, nodePositions, startingNode):
        self.carImg = pygame.image.load('Car.png')
        self.carImg = pygame.transform.scale(self.carImg, (25, 15))
        self.speed = 5
        self.startingNode = startingNode
        self.nodePositions = nodePositions
        self.pos = self.nodePositions[startingNode]
        self.posX = self.pos[0]
        self.posY = self.pos[1]
    def drawSelf(self,screen):
        screen.blit(self.carImg, (0,0))
    #function to move the car along the path that is passed to the car
    def moveCar(self, path):
        path.reverse()
        self.posX += self.speed
        self.posY += self.speed

    def draw(self, surface):
        surface.blit(self.carImg, (self.posX, self.posY))

