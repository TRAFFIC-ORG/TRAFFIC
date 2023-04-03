from Car import Car
from Brain import Brain
class Sim(object):
    def __init__(self, weights=None):
        #List of Cars
        #Brain
        self.brain = Brain(weights) if weights else Brain()
        self.cars = []
        self.points = 0
    #Control Cars
    def carControl(self):
        for i in range(len(self.cars)):
            #Whatever cars need
            self.cars[i].update()
            self.points += self.cars[i].getPoints()
    #Call Brain for certain Light
    def getLightState(self, inputs):
        return self.brain.chooseState(inputs)
    #Get Points
    def getScore(self):
        return self.points
    #Get Weights
    def getWeights(self):
        return self.brain.getWeights()