import os
import json
class Parser:

    def __init__(self):
        self.test = 0
    
    def parsefile():
        f = open("GeniusLyricsSet/lyrics_2chainz_1yeezyboot.json", "r")
        if f.mode == "r":
            parsed_json = json.loads(f.read())
            print("Artist: ", parsed_json['artist'])
            print(parsed_json['songs'][0]['lyrics'])

    def openfiles():
        path = 'GeniusLyricsSet/'
        f2 = open("Superior.txt", "a", encoding="utf-8")

        for filename in os.listdir(path):
            f = open(path + filename, "r")
            if f.mode == "r":
                parsed_json = json.loads(f.read())
                f2.write(str(parsed_json['songs'][0]['lyrics']))
                #print(parsed_json['songs'][0]['lyrics'])
            f.close
        f2.close

def main():
    ps = Parser
    ps.openfiles()

main()