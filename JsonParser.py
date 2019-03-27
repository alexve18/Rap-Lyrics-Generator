import os
import json
import re

 #This trims the dataset from any unwanted symbols and headers
def parsetrimmedfile():
    path = 'GeniusLyricsSet/'
    f2 = open("lyrics-trimmed.txt", "w", encoding="utf-8")

    for filename in os.listdir(path):
        f = open(path + filename, "r")
        if f.mode == "r":
            parsed_json = json.loads(f.read())          #reads the file into a variable
            text = str(parsed_json['songs'][0]['lyrics'])   #Gets the lyrics element of the parsed_json
            text = re.sub("(\[.+\])", "", text)         #Removes [Verse] [Hook] etc.
            text = re.sub("(?:\r?\n){2,}", " ", text)   #Removes extra blank lines
            text = re.sub("(\")", "", text)             #Removes quotation marks
            text = re.sub("(Chorus *(2x)*)", "", text)  #Removes when the lyrics says chorus
            #text = re.sub("(\(.*\))", "", text)
            f2.write(text)                              #Write it into lyrics.txt
        f.close
    f2.close

#This is the raw dataset combined into a single file
def parsefile():    
    path = 'GeniusLyricsSet/'
    f2 = open("lyrics.txt", "w", encoding="utf-8")

    for filename in os.listdir(path):
        f = open(path + filename, "r")
        if f.mode == "r":
            parsed_json = json.loads(f.read())
            f2.write(str(parsed_json['songs'][0]['lyrics']))
        f.close
    f2.close

def main():
    parsefile()
    parsetrimmedfile()

main()
