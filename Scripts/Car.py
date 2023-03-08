import pygame
class Car(object):
    def __init__(self):
        self.carImg = pygame.image.load('Car.png')
        self.carImg = pygame.transform.scale(self.carImg, (25, 15))
    def drawSelf(self,screen):
        screen.blit(self.carImg, (0,0))
