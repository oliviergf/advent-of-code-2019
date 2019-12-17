import numpy as np
space = []
for line in open("day10/input.txt", "r").readlines():
    space.append(list(line.rstrip()))


def part1():
    mostAsteroid = 0
    bestAsteroid = ""
    for i in range(len(space[0])):
        for j in range(len(space)):
            if space[i][j] == ".":
                continue
            # is an asteroid
            asteroids = findMostAsteroid(j, i)
            if(asteroids > mostAsteroid):
                mostAsteroid = asteroids
                bestAsteroid = str(i) + "," + str(j)
    print("best asteroid is " + bestAsteroid)
    print("has " + str(mostAsteroid) + " asteroids")


def findMostAsteroid(pos_x, pos_y):
    directLine = set()
    # look every case
    for i in range(len(space[0])):
        for j in range(len(space)):
            if i == pos_y and j == pos_y:
                continue
            dif_y = pos_y - i
            dif_x = pos_x - j
            directLine.add(np.arctan2(dif_x, dif_y) * 180 / np.pi)

    return len(directLine)


part1()
