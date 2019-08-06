
def smorse(word):
    morse = [ ".- ", "-... ", "-.-. ", "-.. ", ". ", "..-. ", "--. ", ".... ", ".. ",".--- ", "-.- ", ".-.. ", "-- ", "-. ", "--- ", ".--. ", "--.- ",".-. ", "... ", "- ", "..- ","...- ", ".-- ", "-..- ", "-.-- ", "--.. ", "|" ]
    alpha = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z", " " ]

    decoder = dict(zip(alpha, morse))
    return ''.join(map(lambda y : decoder[y].strip(' '), word))

print(smorse(input("Enter text to be decoded: ")))
