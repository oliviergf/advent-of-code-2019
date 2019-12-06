import math
inputs = open("day5/input.txt", "r")
line = inputs.readline().split(",")


def part1(inputs):
    commands = list(map(int, inputs))
    onlyInput = 1
    intComputer(commands, 0, onlyInput)


# def part2(inputs):
#     for i in range(0, 100):
#         for y in range(0, 100):
#             commands = list(map(int, inputs))
#             commands[1] = i
#             commands[2] = y
#             intComputer(commands, 0)
#             if commands[0] == 19690720:
#                 print("solution found: noun is " +
#                       str(i) + " and verb is " + str(y) + ", enter: " + str(100 * i + y))


def intComputer(commands, index, onlyInput):
    reverse_instruction = str(commands[index])[::-1]
    while(len(reverse_instruction) is not 5):
        reverse_instruction += "0"

    instruction = reverse_instruction[0]

    output = ""

    if instruction is not '9':
        if instruction == '3':
            if reverse_instruction[2] == "1":
                commands[index + 1] = onlyInput
            else:
                commands[commands[index + 1]] = onlyInput
            intComputer(commands, index + 2, onlyInput)
        elif instruction == '4':
            if reverse_instruction[2] == "1":
                output += str(commands[index + 1]) + ","
            else:
                output += str(commands[commands[index + 1]]) + ","
            intComputer(commands, index + 2, onlyInput)
        else:
            first = commands[commands[index+1]
                             ] if reverse_instruction[2] == '0' else commands[index+1]
            second = commands[commands[index+2]
                              ] if reverse_instruction[3] == '0' else commands[index+2]
            pos = commands[index+3]
            if instruction == '1':
                commands[pos] = first + second
                intComputer(commands, index + 4, onlyInput)
            else:
                commands[pos] = first * second
                intComputer(commands, index + 4, onlyInput)
    print(output)


part1(line)
# part2(line)
