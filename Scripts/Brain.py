from perceptron import Perceptron
class Brain():
    def __init__(self, weights=None):
        self.perceptrons = [Perceptron(4,weights[0]),Perceptron(4,weights[1]),Perceptron(2,weights[2])] if weights else [Perceptron(4),Perceptron(4),Perceptron(2)]
    def chooseState(self,inputs):
        perSum1 = self.perceptrons[0].createSum(inputs)
        perSum2 = self.perceptrons[1].createSum(inputs)
        finalSum = self.perceptrons[2].createSum([perSum1,perSum2])
        output = 0
        if finalSum >= 0:
            output = 1
        else:
            output = -1
        return output
    def getWeights(self):
        weights = []
        weights.append(self.perceptrons[0].getWeights())
        weights.append(self.perceptrons[1].getWeights())
        weights.append(self.perceptrons[2].getWeights())
        return weights
