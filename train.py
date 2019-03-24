import random
import math
import csv

def sigmoid(x):
    return 1 / (1 + math.exp(x))

class InputNode:
    def __init__(self):
        self.value = 0
        self.weight = random.random()

class Node:
    def __init__(self):
        self.value = 0
        self.weight = random.random()
        self.bias = random.uniform(-1, 1)
        self.nodes = []
    
    def calculateValue(self):
        value = 0
        for node in self.nodes:
            value += (node.weight * node.value)
        value += self.bias
        self.value = sigmoid(value)


class NeuralNetwork:
    def __init__(self):
        #Initialize variables
        self.inputs = []
        self.layer1 = []
        self.layer2 = []
        self.output = Node()

        #Create 64 input nodes
        for _ in range(64):
            self.inputs.append(InputNode())
            self.layer1.append(Node())
            self.layer2.append(Node())

        #Connect layer1 nodes to input nodes
        for node in self.layer1:
            for inputNode in self.inputs:
                node.nodes.append(inputNode)
        
        #Connect layer2 nodes to layer1 nodes
        for node in self.layer2:
            for otherNode in self.layer1:
                node.nodes.append(otherNode)

        #Connect output node to layer2 nodes
        for node in self.layer2:
            self.output.nodes.append(node)
        #Initialization complete

    def calculateOutput(self):
        #Set values in layer1 from input
        for node in self.layer1:
            node.calculateValue()
        
        #Set values in layer2 from layer1
        for node in self.layer2:
            node.calculateValue()

        self.output.calculateValue()
        return self.output.value

    def trainLyric(self, song):
        pass

def main():
    nn = NeuralNetwork()
    lyrics = []
    with open('lyrics.csv', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            lyrics.append(row[5])

    for song in lyrics:
        nn.trainLyric(song)
    

main()