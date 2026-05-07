class NeuralNetwork:

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

    def train(self):
        print("I am training")
        pass

    def query(self):
        print("I ask...")
        pass
#ENDCLASS

# create instance Neural network
neuralNetwork = NeuralNetwork()

neuralNetwork.train()

outputs = neuralNetwork.query()