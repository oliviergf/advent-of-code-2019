inputs = open("day4/input.txt", "r")
line = inputs.readline()
inputRange = list(map(lambda x: int(x), line.split("-")))


def part1(inputRange):
    nbOfValidPassword = 0
    for i in range(inputRange[0], inputRange[1]):
        number = str(i)
        index = 0
        hasConsec = False
        neverDescrese = False
        for y in range(len(number)):
            if int(number[y]) < index:
                break
            if index == int(number[y]):
                hasConsec = True
            if y == len(number) - 1:
                neverDescrese = True
            index = int(number[y])

        if(hasConsec and neverDescrese):
            nbOfValidPassword += 1

    print(nbOfValidPassword)


def hasUnique(consecutives):
    uniques = {}
    for i in consecutives:
        if i not in uniques:
            uniques[i] = 1
        else:
            uniques[i] += 1
    hasSingle = False
    for key in uniques:
        if(uniques[key] == 1):
            hasSingle = True
    return hasSingle


def part2(inputRange):
    nbOfValidPassword = 0
    for i in range(inputRange[0], inputRange[1]):
        number = str(i)
        index = 0
        hasConsec = False
        neverDescrese = False
        groupOfConsecutives = []
        for y in range(len(number)):
            if int(number[y]) < index:
                break
            if index == int(number[y]):
                hasConsec = True
                groupOfConsecutives.append(index)
            if y == len(number) - 1:
                neverDescrese = True
            index = int(number[y])

        if hasConsec and neverDescrese and hasUnique(groupOfConsecutives):
            nbOfValidPassword += 1

    print(nbOfValidPassword)


part1(inputRange)
part2(inputRange)
