import pygame
class Road(object):
    def __init__(self,screen):
        self.screen = screen
        self.roadImg = pygame.image.load('Road.png')
        self.roadImgVert = pygame.transform.rotate(self.roadImg, 90)
        #self.roadImg = pygame.transform.scale(self.roadImg, (WIDTH, 40))
    def drawSelf(self, xPos, yPos, vert):
        if vert:
            self.screen.blit(self.roadImgVert, (xPos,yPos))
        else:
            self.screen.blit(self.roadImg, (xPos,yPos))
