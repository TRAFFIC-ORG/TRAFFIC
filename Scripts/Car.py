import pygame
import time
class Car(object):
    def __init__(self, nodePositions, startingNode, path):
        self.carImg = pygame.image.load('Car.png')
        self.carImg = pygame.transform.scale(self.carImg, (25, 15))
        self.speed = 2
        self.startingNode = startingNode
        self.nodePositions = nodePositions
        self.pos = self.nodePositions[startingNode]
        self.posX = self.pos[0]
        self.posY = self.pos[1]
        self.inQue = False
        self.timeInQue = 0
        self.path = path
        print("path")
        print(self.path)
        self.moving = True
        self.nextNode = 0

    def drawSelf(self,screen):
        # screen.blit(self.carImg, (0,0))
        pygame.draw.circle(screen, (128,230,155), (100, 100), 50)
   

    def moveCar(self):
        if self.moving:
            if self.posX < self.nodePositions[self.path[self.nextNode]][0]:
                self.posX += self.speed
            elif self.posY < self.nodePositions[self.path[self.nextNode]][1]:
                self.posY += self.speed
            elif self.posX > self.nodePositions[self.path[self.nextNode]][0]:
                self.posY -= self.speed
            elif self.posY > self.nodePositions[self.path[self.nextNode]][1]:
                self.posY -= self.speed
            elif self.posX == self.nodePositions[self.path[self.nextNode]][0] and self.posY == self.nodePositions[self.path[self.nextNode]][1]:
                self.moving = False
        # self.posX = self.nodePositions[self.path[1]][0]
        # self.posY = self.nodePositions[self.path[1]][1]


    def draw(self, surface):
        surface.blit(self.carImg, (self.posX, self.posY))
        pygame.draw.circle(surface, (128,230,155), (self.posX, self.posY), 5)

    def nextNode(self):
        if (self.nextNode + 1) <= len(self.path):
            self.nextNode += 1
            self.moving = True
        else:
            print("Arrived!")
