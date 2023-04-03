import random
class Perceptron:
    def __init__(self, numberOfWeights, weights=None):
        self.numberOfWeights = numberOfWeights
        self.weights= weights if weights else self.createWeights()
    def createWeights(self):
        self.weights= []
        for i in range(self.numberOfWeights):
            self.weights.append(0)
        for i in range(self.numberOfWeights):
            self.weights[i] = random.uniform(-1.1,1.1)
        return self.weights
    #Length of inputs must be the same as weights
    def createSum(self, inputs):
        sum = 0
        for i in range(len(inputs)):
            sum += (inputs[i] * self.weights[i])
        return sum
    def getWeights(self):
        return self.weights
