import pygame
import time
class Car(object):
    def __init__(self, nodePositions, startingNode, path):
        # self.carImg = pygame.image.load('Car.png')
        # self.carImg = pygame.transform.scale(self.carImg, (25, 15))
        self.speed = 2
        self.startingNode = startingNode
        self.nodePositions = nodePositions
        self.pos = self.nodePositions[startingNode]
        self.posX = self.pos[0]
        self.posY = self.pos[1]
        self.inQue = False
        self.timeInQue = 0
        self.path = path
        self.moving = True
        self.nextNode = 0
        self.i = 0
        self.atDest = False
        self.goingDown = False
        self.goingUp = False
        self.goingRight = False
        self.goingLeft = False
        self.currentNode = self.path[self.nextNode]

    def drawSelf(self,screen):
        # screen.blit(self.carImg, (0,0))
        pygame.draw.circle(screen, (128,230,155), (100, 100), 50)
   

    def moveCar(self):
        #Check to see if the car is moving to the next node
        if self.moving:
            if self.posX < self.nodePositions[self.path[self.nextNode]][0]:
                self.posX += self.speed
                self.goingDown = False
                self.goingUp = False
                self.goingRight = True
                self.goingLeft = False
            elif self.posY < self.nodePositions[self.path[self.nextNode]][1]:
                self.posY += self.speed
                self.goingDown = True
                self.goingUp = False
                self.goingRight = False
                self.goingLeft = False
            elif self.posX > self.nodePositions[self.path[self.nextNode]][0]:
                self.posX -= self.speed
                self.goingDown = False
                self.goingUp = False
                self.goingRight = False
                self.goingLeft = True
            elif self.posY > self.nodePositions[self.path[self.nextNode]][1]:
                self.posY -= self.speed
                self.goingDown = False
                self.goingUp = True
                self.goingRight = False
                self.goingLeft = False
            #If the car arrived at its destination node
            elif self.posX == self.nodePositions[self.path[self.nextNode]][0] and self.posY == self.nodePositions[self.path[self.nextNode]][1]:
                self.moving = False
                if not self.atDest:
                    self.timeInQue += 1
                #Check to see if it is at the last node 
                if self.nextNode < len(self.path) - 1:
                    self.nextNode += 1
                    self.currentNode = self.path[self.nextNode-1]
                else:
                    self.atDest = True

        #This implements a delay and is only for debugging
        #TODO remove this when the lights are implemented
        if self.i == 100:
            self.moving = True
            self.i = 0
        else:
            self.i += 1

    def draw(self, surface):
        if self.goingRight:
            pygame.draw.circle(surface, (255,255,255), (self.posX - 25, self.posY + 10), 5)
        elif self.goingLeft:
            pygame.draw.circle(surface, (255,255,255), (self.posX + 25, self.posY - 10), 5)
        elif self.goingDown:
            pygame.draw.circle(surface, (255,255,255), (self.posX - 10, self.posY - 25), 5)
        elif self.goingUp:
            pygame.draw.circle(surface, (255,255,255), (self.posX + 10, self.posY + 25), 5)


    def nextNode(self):
        if (self.nextNode + 1) <= len(self.path):
            self.nextNode += 1
            self.moving = True
        else:
            print("Arrived!")
