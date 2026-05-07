import numpy
import scipy.special
import matplotlib.pyplot

import NeuralNetwork

# initialise the neural network


# create instance of neural network
neuralNetwork = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

# link weight matrices, wih and who
# weights inside the arrays are w_i_j, where link is from node i to node j in the next layer
# w11 w21
# w12 w22 etc
self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))