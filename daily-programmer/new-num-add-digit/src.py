
def mutNum(number):
    list = enumerate(str(number))
    newlist = []
    for index, digit in list:
        newlist.append(str(int(digit) + 1))
    return int(''.join(newlist))

print(mutNum(23))
