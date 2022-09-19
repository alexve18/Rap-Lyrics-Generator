import random
import re

# Reads through the datasets and calculates the probabilites of three words appearing together.
# these words appearing in those orders.
def create_dictionaries(fileName):

    # Open the file for reading.
    f = open(fileName, 'r', encoding="utf8")
    # Seperate newline from words so the model doesn't associate new line with the word in front of it.
    words = re.sub("( *\\n)", " \n", f.read()).lower().split(' ')

    # A dictionary that will store the frequencies of a pair of successor words.
    freqDictionary = {}    
    # A dictionary that will store computed the probabilities of a pair of successor words.
    probDictionary = {}

    # Counts how often a word appers (succSuccessor) after two other particular words (current and successor)
    for current, successor, succSuccessor in zip(words[:-2], words[1:-1], words[2:]):
        # Check if the current word has been seen before, if not we add it to the freqDictionary.
        if current not in freqDictionary:
            freqDictionary[current] = {successor: 1}
            freqDictionary[current][successor] =  {succSuccessor: 1}
        # If it has been seen we check if the successor word is in the dictionary associated with the current word.
        else:
            # If successor is not in the dictionary associated with current then we add it to it.
            if successor not in freqDictionary[current]:
                freqDictionary[current][successor] =  {succSuccessor: 1}
            # If successor is in the dictionary we check if the succSuccessor is in the dictionary.
            # If it's not than we assign the value of succSuccessor 1.
            # If it is then we increment the value of succSuccesser by 1. 
            else:
                if succSuccessor not in freqDictionary[current][successor]:
                    freqDictionary[current][successor][succSuccessor] = 1
                else:
                    freqDictionary[current][successor][succSuccessor] += 1 

    # Takes the sum of the number of times a word (succSuccessor) appeared behind 
    # a pair of two words (successor and current). Then divides the time the particular
    # word appeared behind the pair of words to get the probability of that word appearing after this pair of words.
    for current, currDictionary in freqDictionary.items():
        probDictionary[current] = {}
        currentTotal = 0.0

        for successor, succDictionary in currDictionary.items():
            currentTotal += sum(succDictionary.values())

        for successor, succDictionary in currDictionary.items():
            probDictionary[current][successor] = {}
            for succSuccessor in succDictionary:
                probDictionary[current][successor][succSuccessor] = succDictionary[succSuccessor] / currentTotal
    
    return probDictionary, freqDictionary

# Returns probable successor words for the current word.
def next_spit(current, probDictionary):

    # If the word is not in the probDictionary then choose a random successor word for it.
    if current not in probDictionary:
        return [random.choice(list(probDictionary.keys()))]
    # If the word is in the probDictionary then we find a probable successor word for the 
    # current word and the next word.
    else:
        # Dictionary that stores the probabilities of each successor word appearing.
        successorProbs = probDictionary[current]
        probThreshold = random.randint(80, 100)/100
        currentProb = 0.0
        # Checks the probability of every known word that has come after a successor word
        # from the current word, then chooses a likely word and returns the word's predecessor.
        for successor, succDictionary in successorProbs.items():
            for succSuccessor in succDictionary:
                currentProb += succDictionary[succSuccessor]
                if probThreshold <= currentProb:
                    return [successor, succSuccessor]
 
        # If no probable successor word was found then return a random word. 
        return [random.choice(list(probDictionary.keys()))]


# Generates rap lyrics of the same length as amountOfWords.
def dj_spin_that_shit(current, probDictionary, amountOfWords):

    # A list that stores our generated rap
    genRap = [current]
    # Append generated words from the last word in the rap list and the probDictionary
    # using the next_spit function.
    for word in range(0, amountOfWords, 2):
        genRap.extend(next_spit(genRap[-1], probDictionary))
    genRap.append('(END OF RAP)')
    return " ".join(genRap)

if __name__ == '__main__':

    # The lyrics-trimmed.txt dataset is trimmed and contains fewer quotation 
    # marks, no headers like [chorus], and no extra blank lines.
    rapProbDictionary, rapFreqDictionary = create_dictionaries('lyrics-trimmed.txt')

    # You can use the non-trimmed lyrics and generate lyrics that are more like the setup
    # on the genius.com website. However the algorithm is more prone to errors because he has a hard
    # time determining when it is apporiate to use brackets and parantheses.
    #rapProbDictionary = add_to_dictionary('lyrics.txt', rapFreqDictionary)

    rapLength = input('How many words do you want to generate?\n> ')
    intRapLength = int(rapLength)
    firstWord = input('Choose the first word for your rap!\n> ')
    print('Alright homie, here I go: \n')
    print(dj_spin_that_shit(firstWord.lower(), rapProbDictionary, intRapLength))