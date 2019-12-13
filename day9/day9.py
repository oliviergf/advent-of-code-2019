inputs = open("day9/input.txt", "r")
line = list(map(int, inputs.readline().split(",")))


def intComputer(commands, index, onlyInput, outputs, relative_base):
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
            intComputer(commands, pos_to_jump_to,
                        onlyInput, outputs, relative_base)
        elif op_code == '6':
            pos_to_jump_to = second if first == 0 else index + 3
            intComputer(commands, pos_to_jump_to,
                        onlyInput, outputs, relative_base)
        elif op_code == '3':
            if instruction[2] == "1":
                commands[index + 1] = onlyInput
            else:
                commands[commands[index + 1]] = onlyInput
            pos_to_jump_to = index + 2
            intComputer(commands, index + 2, onlyInput,
                        outputs, relative_base)
        elif op_code == '4':
            if instruction[2] == "1":
                outputs.append(commands[index + 1])
            else:
                outputs.append(commands[commands[index + 1]])
            pos_to_jump_to = index + 2
            intComputer(commands, index + 2, onlyInput,
                        outputs, relative_base)
        else:
            pos = commands[index+3]
            if op_code == '7':
                commands[pos] = 1 if first < second else 0
            if op_code == '8':
                commands[pos] = 1 if first == second else 0
            elif op_code == '1':
                commands[pos] = first + second
            else:
                # instruction = 2
                commands[pos] = first * second
            intComputer(commands, index + 4, onlyInput, outputs, relative_base)


def part1(commands):
    onlyInput = 5
    outputs = []
    relative_base = 0
    intComputer(commands, 0, onlyInput, outputs, relative_base)
    print(outputs[0])


part1(line)
