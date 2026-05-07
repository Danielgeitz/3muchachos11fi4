import numpy
import matplotlib.pyplot
import scipy.special


class NeuralNetwork:

    def __init__(self, inputNodes, hiddenNodes, outputNodes, learningRate):
    # set number of nodes in each input, hidden output layer
        self.iNodes = inputNodes
        self.hNodes = hiddenNodes
        self.oNodes = outputNodes

    # learning rate
        self.lr = learningRate

    # link weight matrices, wih and who
    # weights inside the arrays are w_i_j, where link is from node i to node j in the next layer
    # w11 w21
    # w12 w22 etc
        self.wih = numpy.random.normal(0.0, pow(self.iNodes, -0.5), (self.hNodes, self.iNodes))
        self.who = numpy.random.normal(0.0, pow(self.hNodes, -0.5), (self.oNodes, self.hNodes))



    def train(self):
        print("I am training")
        pass

    def query(self):
        print("I ask...")
        pass
#ENDCLASS


# number of input, hidden & output nodes
input_nodes = 3
hidden_nodes = 3
output_nodes = 3

# learning rate is 0.3
learning_rate = 0.3

# create instance Neural network
neuralNetwork = NeuralNetwork(input_nodes,hidden_nodes,output_nodes, learning_rate)

neuralNetwork.train()

outputs = neuralNetwork.query()