# ARTI_FINALE
This is our final project in the Artificial Intelligence course. 

We make a rap lyrics generator using a hidden Markov model.

We used this code https://github.com/johnwmillr/LyricsGenius to scrape rap lyrics from 998 different song from ten various rap artists from the Genius website. We then created a python script (jsonParser.py) to go through those files and trim what wasn't needed and combined them into a single text file which made up our training data. Our hidden Markov model (lilMarkov.py) goes through the dataset word by word and learns the probabilities of two words appearing together after particular words and can then determine from a single word what a plausible next word could be and can thus generate rap lyrics.

Nothing is needed to run the rap generator or the json parser expect python 2.7 or newer

To run the jsonParser which creates the dataset simply run the following command
```
python jsonParser.py
```
You can easily modify the json parser script and thus changing the data set.

To run the hidden markov model simply run the following command 
```
python lilMarkov.py
```
