#JMSSNeural v0.8
import math
import random

# the inner dot product
def dot(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))
    
# the sigmoid function for classification
# it's a smooth and differientiable 'step' function
def sigmoid(t):
    return 1.0 / (1.0 + math.exp(-t))

def neuron_output(weights, inputs):
    return sigmoid(dot(weights, inputs))

def feed_forward(neural_network, inputs):
    outputs = []

    for layer in neural_network:
        # add a bias input with weight 1.0
        input_with_bias = inputs + [1]

        output = [neuron_output(neuron, input_with_bias)
                  for neuron in layer]
        outputs.append(output)

        #print (input_with_bias)

        #print(output)

        inputs = output
    return outputs

def backpropagate(network, inputs, targets, learning_rate = 1.0):
    hidden_outputs, outputs = feed_forward(network, inputs)

    output_deltas = [output * (1 - output) * (output - target)
                     for output, target in zip(outputs, targets)]

    for i, output_neuron in enumerate(network[-1]):
        for j, hidden_output in enumerate(hidden_outputs + [1]):
            output_neuron[j] -= learning_rate * output_deltas[i] * hidden_output

    hidden_deltas = [hidden_output * (1 - hidden_output) *
                     dot(output_deltas, [n[i] for n in network[-1]])
                     for i, hidden_output in enumerate(hidden_outputs)]

    for i, hidden_neuron in enumerate(network[0]):
        for j, in_put in enumerate(inputs + [1]):
            hidden_neuron[j] -= learning_rate * hidden_deltas[i] * in_put

def nn_predict(network, input):
    return feed_forward(network, input)[-1]


def nn_create(input_size, hidden_size, output_size):
    # structure of our neural net
    hidden_layer = []
    output_layer =  []

    #input_size = 25
    #hidden_size = 18
    #output_size = 10

    # training data and number epoch
    #training_data = []
    #num_epochs = 10000
    #random.seed(random.randint(0,30))

    ################################ setting up the network ######################################

    network = [hidden_layer, output_layer]

    for i in range(hidden_size):
        hidden_neuron = []                          # creating a hidden neuron
        for j in range(input_size + 1):             # +1 weight for additional bias weight
            hidden_neuron.append(random.random())   # start off with random weights
        hidden_layer.append(hidden_neuron)          # add it to the (single) hidden layer


    for i in range(output_size):
        output_neuron = []                          # creating an output neuron
        for j in range(hidden_size + 1):            # +1 weight for additional bias weight
            output_neuron.append(random.random())   # start off with random weights
        output_layer.append(output_neuron)          # add it to the output layer   

    return network

def nn_train(network, training_data, num_epochs, learning_rate = 1.0):
    for __ in range(num_epochs):
        for training_pair in training_data:
            backpropagate(network, training_pair[0], training_pair[1], learning_rate)
    return network

# the heaviside step function
def step(signal):
    if signal > 0:
        return 1
    else:
        return 0

# the summation of weights (including bias) and inputs
# note that the last input value (the 'answer') is ignored
# ^^ this assumes that the input values contain an answer!
# so not suitable for feedforward summation
def perceptron_train(input_values, weights):
    # weights 0 is the bias
    total = weights[0]
    i = 0
    while i < len(input_values)-1:
        total += input_values[i] * weights[i + 1]
        i += 1
    return step(total)

# used for feedforward summation
def perceptron(input_values, weights):
    # weights 0 is the bias
    total = weights[0]
    i = 0
    while i < len(input_values):
        total += input_values[i] * weights[i + 1]
        i += 1
    return step(total)

# Train Perceptron weights using gradient descent
def perceptron_train(dataset, learning_rate, epochs):
    weights = [0.0 for i in range(len(dataset[0]))]
    for epoch in range(epochs):
            sum_error = 0.0
            for row in dataset:
                prediction = perceptron_train(row, weights)
                error = row[-1] - prediction
                sum_error += error**2
                # weight 0 is the bias
                weights[0] = weights[0] + learning_rate * error
                for i in range(len(row)-1):
                    weights[i + 1] = weights[i + 1] + learning_rate * error * row[i]
    return weights
 
