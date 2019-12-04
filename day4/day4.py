inputs = open("day4/input.txt", "r")
line = inputs.readline()
inputRange = list(map(lambda x: int(x), line.split("-")))


def part1and2(inputRange):
    nbOfValidPasswordPart1 = 0
    nbOfValidPasswordPart2 = 0
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

        if(hasConsec and neverDescrese):
            nbOfValidPasswordPart1 += 1
        if hasConsec and neverDescrese and hasUnique(groupOfConsecutives):
            nbOfValidPasswordPart2 += 1

    print(nbOfValidPasswordPart1)
    print(nbOfValidPasswordPart2)


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


part1and2(inputRange)
