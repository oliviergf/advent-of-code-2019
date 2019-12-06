import math
inputs = open("day5/input.txt", "r")
line = inputs.readline().split(",")


def part1(inputs):
    commands = list(map(int, inputs))
    onlyInput = 1
    intComputer_part1(commands, 0, onlyInput)


def part2(inputs):
    commands = list(map(int, inputs))
    onlyInput = 1
    intComputer_part2(commands, 0, onlyInput)


def intComputer_part2(commands, index, onlyInput):
    reverse_instruction = str(commands[index])[::-1]
    while(len(reverse_instruction) is not 5):
        reverse_instruction += "0"

    instruction = reverse_instruction[0]

    output = ""

    if instruction is not '9':
        if instruction == '5':
            first = commands[commands[index+1]
                             ] if reverse_instruction[2] == '0' else commands[index+1]
            second = commands[commands[index+2]
                              ] if reverse_instruction[3] == '0' else commands[index+2]
            pos_to_jump_to = second if first != 0 else index + 2
            intComputer_part2(commands, pos_to_jump_to, onlyInput)
        elif instruction == '6':
            first = commands[commands[index+1]
                             ] if reverse_instruction[2] == '0' else commands[index+1]
            second = commands[commands[index+2]
                              ] if reverse_instruction[3] == '0' else commands[index+2]
            pos_to_jump_to = second if first == 0 else index + 2
            intComputer_part2(commands, pos_to_jump_to, onlyInput)
        elif instruction == '3':
            if reverse_instruction[2] == "1":
                commands[index + 1] = onlyInput
            else:
                commands[commands[index + 1]] = onlyInput
            intComputer_part2(commands, index + 2, onlyInput)
        elif instruction == '4':
            if reverse_instruction[2] == "1":
                output += str(commands[index + 1]) + ","
            else:
                output += str(commands[commands[index + 1]]) + ","
            intComputer_part2(commands, index + 2, onlyInput)
        else:
            first = commands[commands[index+1]
                             ] if reverse_instruction[2] == '0' else commands[index+1]
            second = commands[commands[index+2]
                              ] if reverse_instruction[3] == '0' else commands[index+2]
            pos = commands[index+3]
            if instruction == '7':
                print("sup")
            if instruction == '8':
                print("sup")
            elif instruction == '1':
                commands[pos] = first + second
                intComputer_part2(commands, index + 4, onlyInput)
            else:
                # instruction = 2
                commands[pos] = first * second
                intComputer_part2(commands, index + 4, onlyInput)
    print(output)


def intComputer_part1(commands, index, onlyInput):
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
            intComputer_part1(commands, index + 2, onlyInput)
        elif instruction == '4':
            if reverse_instruction[2] == "1":
                output += str(commands[index + 1]) + ","
            else:
                output += str(commands[commands[index + 1]]) + ","
            intComputer_part1(commands, index + 2, onlyInput)
        else:
            first = commands[commands[index+1]
                             ] if reverse_instruction[2] == '0' else commands[index+1]
            second = commands[commands[index+2]
                              ] if reverse_instruction[3] == '0' else commands[index+2]
            pos = commands[index+3]
            if instruction == '1':
                commands[pos] = first + second
                intComputer_part1(commands, index + 4, onlyInput)
            else:
                commands[pos] = first * second
                intComputer_part1(commands, index + 4, onlyInput)
    print(output)


# part1(line)
part2(line)
