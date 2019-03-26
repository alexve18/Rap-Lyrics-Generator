import random
import re

# Reads through the dataset and calculates the probabilites of words appearing after other words.
# Returns a dictionary of dictionaries that contain these probabilites.
def add_to_dictionary(fileName, freqDictionary):
    # Open the file for reading.
    f = open(fileName, 'r', encoding="utf8")
    # Seperate newline from words so the model doesn't associate 
    # new line with the word in front of it.
    words = re.sub("\n", " \n", f.read()).lower().split(' ')
    
    # Counts how often a word (successor) appears after a certain word (current)
    for current, successor in zip(words[1:], words[:-1]):
        # Check if the current word has been seen before, if not we give current it's own dictionary. 
        if current not in freqDictionary:
            freqDictionary[current] = {successor: 1}
        # If it has not been seen we check if the successor word is in the dictionary associated with the current word.
        else:
            # If successor is not in the dictionary we add it to it and assign it 1. 
            if successor not in freqDictionary[current]:
                freqDictionary[current][successor] = 1
            # If successor is in the dictionary we increment it's number by 1.
            else:
                freqDictionary[current][successor] += 1

    # Computes the probability of successors words from current words.
    probDictionary = {}
    # Takes the sum of every time a current word is found and divides the amount of times every successor
    # word is found and calculates the probability of a successor word from appearing behind 
    # a current word and stores it in a probDictionary
    for current, currDictionary in freqDictionary.items():
        probDictionary[current] = {}
        # Takes the sum of every time the current word was found in the dataset
        currentTotal = sum(currDictionary.values())
        # checks every successor word of the current word
        for successor in currDictionary:
            # Calculates the probabilities of words being the successor word of the current word
            # and stores them in the dictionary associated with the current word in probDictionary.
            probDictionary[current][successor] = currDictionary[successor] / currentTotal
    return probDictionary

# Returns a probable successor word for the current word.
def next_spit(current, probDictionary):

    # If the word is not in the probDictionary then choose a random successor word for it.
    if current not in probDictionary:
        return random.choice(list(probDictionary.keys()))
    # If the word is in the probDictionary then we find a the likeliest successor word for it.
    else:
        # Dictionary that stores the probabilities of each successor word appearing.
        successorProbs = probDictionary[current]
        # Gets a random probability
        randomProb = random.random()
        # Probability of the current successor word.
        currentProb = 0.0
        # Checks the pobability for every successor word and adds it to the currentProb,
        # when currentProb is equal to or higher than random then return the successor word
        # that we are currently looking at.
        for successor in successorProbs:
            currentProb += successorProbs[successor]
            if randomProb <= currentProb:
                return successor
        # If no probable successor word was found then return a random word. 
        return random.choice(list(probDictionary.keys()))


# Generates rap lyrics of the length of amountOfWords.
def dj_spin_that_shit(current, probDictionary, amountOfWords):

    # A list that stores our generated rap
    genRap = [current]
    # Append generated words from the last word in the rap list and the probDictionary
    # using the next_spit function.
    for word in range(amountOfWords):
        genRap.append(next_spit(genRap[-1], probDictionary))
    return " ".join(genRap)

if __name__ == '__main__':
    # A dictionary the stores the frequencies of successor words.
    rapFreqDictionary = {}
    # A dictionary that stores the probabilites of successor words appearing
    # after certain words.
    rapProbDictionary = add_to_dictionary('Superior-trimmed.txt', rapFreqDictionary)

    firstWord = input("Choose the first word for your rap!\n")
    print("Alright homie, here I go: \n")
    print(dj_spin_that_shit(firstWord, rapProbDictionary, 100))