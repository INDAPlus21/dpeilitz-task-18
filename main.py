import json

word_dict = {}


def write_to_Dict():
    #Goes through the the token.txt file and enters every line into the word_dict dictionary. Skips every duplicate letter.
    with open('token.txt', 'r') as token:
        lines = token.readlines()
        #temp = 0
        for line in lines:
            #temp += 1
            # if temp > 4200:
            #temp = 0
            # break
            line = line.replace("\n", "")
            key = line.split(" ")[0]
            value = line.split(" ")[1]
            if word_dict.get(key):
                word_dict[key].append(value)
            else:
                word_dict[key] = [value]


def write_indexFile():
    #Prints the content of the word_dict to the indexFile

    with open('indexFile.txt', "w") as file:
        output = ""
        for data in word_dict.keys():
            output += data
            for i in word_dict[data]:
                output += " %s " % i
            print(output)
            file.write(output + "\n")
            output = ""



def find_word(word):
    #Scans through the corpus, finds all occurences of the word and prints the sentence that they are in.
    get_magic()
    print(word_dict["aa"])
    value = word_dict[word]
    print("Found " + str(len(value)) + " matches")
    with open('korpus', "r") as text:
        for i in value:
            left = int(i)-20
            output = text.seek(left)
            print(text.read(40))


def write_magicFile():
    # Writes the word_dict to the magicFile and stores it as a json.
    magic = open("magicFile.json", "w")
    json.dump(word_dict, magic)
    magic.close()


def get_magic():
    # Gets all data from the magic file and outputs it to the word_dict 
    with open('magicFile.json') as file:
        global word_dict
        word_dict = json.load(file)


def test():
    #REMOVE ASAP
    search = input("Slå in sökord vettja")
    find_word(search)


def construct():
    #Constructs everything
    write_to_Dict()
    write_indexFile()
    write_magicFile()

#construct()

find_word("a")
