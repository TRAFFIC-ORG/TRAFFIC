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
<<<<<<< HEAD
        self.inQue = False
        self.timeInQue = 0
    def drawSelf(self,screen):
        screen.blit(self.carImg, (0,0))
    #function to move the car along the path that is passed to the car
    def moveCar(self, path):
        path.reverse()
        self.posX += self.speed
        self.posY += self.speed
    def leftQue(self):
        self.inQue = False
    def joinedQue(self):
        self.inQue = True
    def flagger(self):
        if self.inQue:
            self.timeInQue += 0.016
    def update(self):
        self.flagger()
        self.moveCar()
    def getPoints(self):
        return self.timeInQue
=======
        self.path = path
    def drawSelf(self,screen):
        screen.blit(self.carImg, (0,0))
    #function to move the car along the path that is passed to the car
    def moveCar(self ):
        print(self.path)
        print(self.nodePositions[self.path[1]])
        self.posX = self.nodePositions[self.path[1]]
        self.posY = self.nodePositions[self.path[1]]

>>>>>>> e4d6c48 (Started working on the light controls)
    def draw(self, surface):
        surface.blit(self.carImg, (self.posX, self.posY))

