inputs = open("day4/input.txt", "r")
line = inputs.readline()


def part1(line):
    inputRange = list(map(lambda x: int(x), line.split("-")))
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


part1(line)
