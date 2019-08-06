

def smorse(word):
    morse = [ ".- ", "-... ", "-.-. ", "-.. ", ". ", "..-. ", "--. ", ".... ", ".. ",".--- ", "-.- ", ".-.. ", "-- ", "-. ", "--- ", ".--. ", "--.- ",".-. ", "... ", "- ", "..- ","...- ", ".-- ", "-..- ", "-.-- ", "--.. ", "|" ]
    alpha = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z", " " ]

    decoder = dict(zip(alpha, morse))
    return ''.join(map(lambda y : decoder[y].strip(' '), word))

def find13():
    freqMap = {}
    with open('./enable1.txt') as file:
        for line in file:
            word = smorse(line.strip('\n'))
            if( word in freqMap):
                freqMap[word] += 1
            else:
                freqMap[word] = 1

    for key, value in freqMap.items():
        if (value == 13):
            return key

print(smorse(input("Enter text to be decoded: ")))
print(find13())