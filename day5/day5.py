inputs = open("day5/input.txt", "r")
line = inputs.readline().split(",")

# to whoever might look at this code, i know it's absolute garbage. I got lazy on this one.
# BUT! it works xD also its recursive so its cool


def part1(inputs):
    commands = list(map(int, inputs))
    onlyInput = 1
    intComputer_part1(commands, 0, onlyInput)


def part2(inputs):
    commands = list(map(int, inputs))
    onlyInput = 5
    outputs = []
    intComputer_part2(commands, 0, onlyInput, outputs)
    print(outputs[0])


def intComputer_part2(commands, index, onlyInput, outputs):
    instruction = str(commands[index])[::-1]
    while(len(instruction) is not 5):
        instruction += "0"

    op_code = instruction[0]

    if op_code is not '9':
        # first value
        if instruction[2] == "0":
            # position mode
            first = commands[commands[index+1]]
        elif instruction[2] == "1":
            # immediate mode
            first = commands[index+1]
        elif instruction[2] == "2":
            # relative mode
            print("relative")

         # second value
        if instruction[3] == "0":
            # position mode
            second = commands[commands[index+2]]
        elif instruction[3] == "1":
            # immediate mode
            second = commands[index+2]
        elif instruction[3] == "2":
            # relative mode
            print("relative")

        if op_code == '5':
            pos_to_jump_to = second if first != 0 else index + 3
            intComputer_part2(commands, pos_to_jump_to,
                              onlyInput, outputs)
        elif op_code == '6':
            pos_to_jump_to = second if first == 0 else index + 3
            intComputer_part2(commands, pos_to_jump_to,
                              onlyInput, outputs)
        elif op_code == '3':
            if instruction[2] == "1":
                commands[index + 1] = onlyInput
            else:
                commands[commands[index + 1]] = onlyInput
            intComputer_part2(commands, index + 2, onlyInput,
                              outputs)
        elif op_code == '4':
            if instruction[2] == "1":
                outputs.append(commands[index + 1])
            else:
                outputs.append(commands[commands[index + 1]])
            intComputer_part2(commands, index + 2, onlyInput,
                              outputs)
        else:
            pos = commands[index+3]
            if op_code == '7':
                commands[pos] = 1 if first < second else 0
            elif op_code == '8':
                commands[pos] = 1 if first == second else 0
            elif op_code == '1':
                commands[pos] = first + second
            else:
                # instruction = 2
                commands[pos] = first * second
            intComputer_part2(commands, index + 4, onlyInput, outputs)


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
