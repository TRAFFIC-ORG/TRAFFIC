import pygame
from Sim import Sim
import random
class Trainer(object):
    def __init__(self):
        self.sims = []
        for i in range(5):
            self.sims.append(Sim())
        self.currentSim = 0
        self.switched = False
    def switchSim(self):
        self.currentSim += 1 
        # print(self.currentSim)
        if self.currentSim == len(self.sims):
            self.currentSim -= 1
            self.train()
    def shouldSwitch(self):
        if(pygame.time.get_ticks() % 500 >= 400 and self.switched == False):
            self.switched = True
            return True
        if(pygame.time.get_ticks() % 500 <= 100):
            self.switched = False
        return False
    def train(self):
        topScore = self.sims[0].getScore()
        topScoreIndex = 0
        for i in range(len(self.sims)):
            if topScore < self.sims[i].getScore():
                topScoreIndex = i
                topScore = self.sims[i].getScore()
        topSim = self.sims[topScoreIndex]
        succesWeights = topSim.getWeights()
        self.currentSim = 0
        self.sims.clear()
        for x in range(5):
            for i in range(len(succesWeights)):
                for j in range(len(succesWeights[i])):
                    succesWeights[i][j] += random.uniform(-0.1,0.1)
            self.sims.append(Sim(succesWeights))
    def getCurrentSim(self):
        return self.sims[self.currentSim]
            

