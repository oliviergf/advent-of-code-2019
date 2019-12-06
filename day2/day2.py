import math
inputs = open("day2/input.txt", "r")
line = inputs.readline().split(",")


def part1(inputs):
    commands = list(map(int, inputs))
    intComputer(commands, 0)
    print(commands[0])


def part2(inputs):
    for i in range(0, 100):
        for y in range(0, 100):
            commands = list(map(int, inputs))
            commands[1] = i
            commands[2] = y
            intComputer(commands, 0)
            if commands[0] == 19690720:
                print("solution found: noun is " +
                      str(i) + " and verb is " + str(y) + ", enter: " + str(100 * i + y))


def intComputer(commands, index):
    instruction = commands[index]
    if instruction != 99:
        first = commands[commands[index+1]]
        second = commands[commands[index+2]]
        pos = commands[index+3]
        if instruction == 1:
            commands[pos] = first + second
        else:
            commands[pos] = first * second
        intComputer(commands, index + 4)


part1(line)
part2(line)
