from itertools import permutations
inputs = open("day7/input.txt", "r")
line = inputs.readline().split(",")

int_computer_output = []


def intComputer(commands, index, inputs, firstInstruc):
    reverse_instruction = str(commands[index])[::-1]
    while(len(reverse_instruction) is not 5):
        reverse_instruction += "0"

    instruction = reverse_instruction[0]

    if instruction is not '9':
        if instruction == '5':
            first = commands[commands[index+1]
                             ] if reverse_instruction[2] == '0' else commands[index+1]
            second = commands[commands[index+2]
                              ] if reverse_instruction[3] == '0' else commands[index+2]
            pos_to_jump_to = second if first != 0 else index + 3
            intComputer(commands, pos_to_jump_to, inputs, firstInstruc)
        elif instruction == '6':
            first = commands[commands[index+1]
                             ] if reverse_instruction[2] == '0' else commands[index+1]
            second = commands[commands[index+2]
                              ] if reverse_instruction[3] == '0' else commands[index+2]
            pos_to_jump_to = second if first == 0 else index + 3
            intComputer(commands, pos_to_jump_to, inputs, firstInstruc)
        elif instruction == '3':
            if reverse_instruction[2] == "1":
                commands[index + 1] = inputs[0] if firstInstruc else inputs[1]
            else:
                commands[commands[index + 1]
                         ] = inputs[0] if firstInstruc else inputs[1]
            firstInstruc = False
            intComputer(commands, index + 2, inputs, firstInstruc)
        elif instruction == '4':
            if reverse_instruction[2] == "1":
                int_computer_output.append(commands[index + 1])
            else:
                int_computer_output.append(commands[commands[index + 1]])
            intComputer(commands, index + 2, inputs, firstInstruc)
        else:
            first = commands[commands[index+1]
                             ] if reverse_instruction[2] == '0' else commands[index+1]
            second = commands[commands[index+2]
                              ] if reverse_instruction[3] == '0' else commands[index+2]
            pos = commands[index+3]
            if instruction == '7':
                commands[pos] = 1 if first < second else 0
                intComputer(commands, index + 4, inputs, firstInstruc)
            if instruction == '8':
                commands[pos] = 1 if first == second else 0
                intComputer(commands, index + 4, inputs, firstInstruc)
            elif instruction == '1':
                commands[pos] = first + second
                intComputer(commands, index + 4, inputs, firstInstruc)
            else:
                # instruction = 2
                commands[pos] = first * second
                intComputer(commands, index + 4, inputs, firstInstruc)


def part1(inputs):
    commands = list(map(int, inputs))
    thrusters_values = []
    possible_inputs = [list(p) for p in permutations([0, 1, 2, 3, 4])]

    for inputs in possible_inputs:
        pair_of_inputs = [None, None]
        for i in range(0, 5):
            if i == 0:
                pair_of_inputs[1] = 0
            # phase setting
            pair_of_inputs[0] = inputs[i]
            intComputer(commands, 0, pair_of_inputs, True)
            pair_of_inputs[1] = int_computer_output[0]
            if i != 4:
                int_computer_output.clear()
        thrusters_values.append(int_computer_output[0])
        int_computer_output.clear()
    max = 0
    for value in thrusters_values:
        if value > max:
            max = value
    print("part1: " + str(max))


def part2(inputs):
    commands = list(map(int, inputs))
    thrusters_values = []
    possible_inputs = [list(p) for p in permutations([5, 6, 7, 8, 9])]
    test = 0

    for inputs in possible_inputs:
        pair_of_inputs = [None, None]
        looping = False
        isRunning = True
        test += 1
        while isRunning:
            for i in range(0, 5):
                if i == 0 and not looping:
                    pair_of_inputs[1] = 0
                    looping = True
                elif i == 0 and looping:
                    pair_of_inputs[1] = int_computer_output[0]
                # phase setting
                pair_of_inputs[0] = inputs[i]
                intComputer(commands, 0, pair_of_inputs, True)
                if len(int_computer_output) == 0:
                    isRunning = False
                    break
                pair_of_inputs[1] = int_computer_output[0]
                if i != 4:
                    int_computer_output.clear()
            thrusters_values.append(int_computer_output[0])
            print(test)
    max = 0
    for value in thrusters_values:
        if value > max:
            max = value
    print("part2: " + str(max))


part1(line)
part2(line)
