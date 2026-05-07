import numpy
import scipy.special
import matplotlib.pyplot

# initialise the neural network
def __init__(self, inputNodes, hiddenNodes, outputNodes, learningRate):
    # set number of nodes in each input, hidden output layer
    self.inodes = inputNodes
    self.hNodes = hiddenNodes
    self.oNodes = outputNodes

    # learning rate
    self.lr = learningRate
    pass

# number of input, hidden & output nodes

input_nodes = 3
hidden_nodes = 3
output_nodes = 3

# learning rate is 0.3
learning_rate = 0.3

# create instance of neural network
neuralNetwork = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

# link weight matrices, wih and who
# weights inside the arrays are w_i_j, where link is from node i to node j in the next layer
# w11 w21
# w12 w22 etc
self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))