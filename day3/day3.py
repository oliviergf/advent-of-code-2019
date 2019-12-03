import re
import sys
inputs = open("day3/input.txt", "r")
lines = inputs.readlines()


def part1(lines):
    wirePos1 = []
    wirePos2 = []

    addsCircuitPosition(lines[0].split(","), wirePos1)
    addsCircuitPosition(lines[1].split(","), wirePos2)

    communs = common_member(wirePos1, wirePos2)
    closest = findClosest(communs)
    print("the closest distance found is " + str(closest))


def part2(lines):
    wirePos1 = []
    wirePos2 = []

    addsCircuitPosition(lines[0].split(","), wirePos1)
    addsCircuitPosition(lines[1].split(","), wirePos2)

    communs = common_member(wirePos1, wirePos2)
    nbOfSteps = findClosestIntersection(communs, wirePos1, wirePos2)
    print("the closest nb of Steps is " + str(nbOfSteps))


def findClosestIntersection(communs, pos1, pos2):
    nbOfSteps = sys.maxsize
    for intersection in communs:
        steps1 = findStepToIntersec(intersection, pos1)
        steps2 = findStepToIntersec(intersection, pos2)
        total = steps1 + steps2
        if total < nbOfSteps:
            nbOfSteps = total
    return nbOfSteps


def findStepToIntersec(intersection, positions):
    steps = 1
    for position in positions:
        if position == intersection:
            break
        steps += 1
    return steps


def addsCircuitPosition(moves, positions):
    currentPos = [0, 0]
    regex = re.compile(r'(\d+|\s+)')

    for move in moves:
        # splits up the commands makes likes ["L","345"]
        deplacement = regex.split(move)
        for i in range(0, int(deplacement[1])):
            if deplacement[0] == 'U':
                currentPos[1] = currentPos[1] + 1
            elif deplacement[0] == 'D':
                currentPos[1] = currentPos[1] - 1
            elif deplacement[0] == 'L':
                currentPos[0] = currentPos[0] - 1
            elif deplacement[0] == 'R':
                currentPos[0] = currentPos[0] + 1
            positions.append(str(currentPos[0])+":"+str(currentPos[1]))


def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        return(a_set & b_set)
    else:
        print("No common elements")


def findClosest(communs):
    # not infinity but good enough
    closestDist = sys.maxsize
    for commun in communs:
        coords = commun.split(":")
        dist = abs(int(coords[0])) + abs(int(coords[1]))
        if dist < closestDist:
            closestDist = dist
    return closestDist


part1(lines)
part2(lines)
