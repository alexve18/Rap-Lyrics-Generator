import os
import json
import re
    
def parsetrimmedfile():
    path = 'GeniusLyricsSet/'
    f2 = open("Superior-trimmed.txt", "w", encoding="utf-8")

    for filename in os.listdir(path):
        f = open(path + filename, "r")
        if f.mode == "r":
            parsed_json = json.loads(f.read())
            #print(parsed_json['songs'][0]['lyrics'])
            text = str(parsed_json['songs'][0]['lyrics'])
            text = re.sub("(\[.+\])", "", text)
            text = re.sub("(?:\r?\n){2,}", " ", text)
            text = re.sub("(Chorus *(2x)*)", "", text)
            text = re.sub("(\(.*\))", "", text)
            f2.write(text)
        f.close
    f2.close

def parsefile():
    path = 'GeniusLyricsSet/'
    f2 = open("Superior.txt", "w", encoding="utf-8")

    for filename in os.listdir(path):
        f = open(path + filename, "r")
        if f.mode == "r":
            parsed_json = json.loads(f.read())
            f2.write(str(parsed_json['songs'][0]['lyrics']))
            #print(parsed_json['songs'][0]['lyrics'])
        f.close
    f2.close

def main():
    parsefile()
    parsetrimmedfile()

main()