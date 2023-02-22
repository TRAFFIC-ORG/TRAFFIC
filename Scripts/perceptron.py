import random
class Perceptron:
    def __init__(self, numberOfWeights):
        self.weights = [0] * numberOfWeights
        self.numberOfWeights = numberOfWeights
        for i in range(numberOfWeights):
            self.weights[i] = random.uniform(-1.1,1.1)
        print(self.weights)
    
    #Length of inputs must be the same as weights
    def createSum(self, inputs):
        sum = 0
        for i in range(len(inputs)):
            sum += (inputs[i] * self.weights[i])
        
        output = 0
        if sum >=0 :
            output = 1
        else:
            output=0
        print(output)
