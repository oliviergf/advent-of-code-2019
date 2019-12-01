import math
inputs = open("day1/input.txt", "r")
lines = inputs.readlines()


def calcFuel(lines):
    totalFuel = 0
    for line in lines:
        totalFuel += math.floor(int(line) / 3) - 2
    return totalFuel


def recursiveFuel(fuel):
    addedFuel = math.floor(fuel / 3) - 2
    if addedFuel <= 0:
        return 0
    else:
        return addedFuel + recursiveFuel(addedFuel)


def calcFuelPart2(lines):
    totalFuel = 0
    for line in lines:
        totalFuel += recursiveFuel(int(line))
    return totalFuel


def part1(lines):
    print(calcFuel(lines))


def part2(lines):
    print(calcFuelPart2(lines))


part1(lines)
part2(lines)
