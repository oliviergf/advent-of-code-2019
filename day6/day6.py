import sys
inputs = open(
    "day6/input.txt", "r")
orbits = list(map(lambda x: x.rstrip(), inputs.readlines()))

sys.setrecursionlimit(10**6)


class Planet:
    def __init__(self, name):
        self.orbiters = []
        self.orbits = ""
        self.name = name

    def add_orbiter(self, orbited_by):
        self.orbiters.append(orbited_by)

    def orbits_planet(self, planet):
        self.orbits = planet


def part1and2(orbits):
    galactic = {}
    for orbit in orbits:
        [planet, orbiter] = orbit.split(")")

        # adds planet in galactic
        if planet in galactic:
            galactic[planet].add_orbiter(orbiter)
        else:
            new_planet = Planet(planet)
            new_planet.add_orbiter(orbiter)
            galactic[new_planet.name] = new_planet

        # adds orbiter in galactic
        if orbiter in galactic:
            galactic[orbiter].orbits_planet(planet)
        else:
            new_planet = Planet(orbiter)
            new_planet.orbits_planet(planet)
            galactic[new_planet.name] = new_planet

    total_orbits = follow_to_COM(galactic)
    print("total orbits: " + str(total_orbits))
    part2(galactic)


def part2(galactic):
    find_santa(galactic[galactic["YOU"].orbits], galactic, 0)


def find_santa(planet_visited, galactic, path):
    if "SAN" in planet_visited.orbiters:
        print(path)
    elif planet_visited.name != "COM":
        find_santa(galactic[planet_visited.orbits], galactic, path + 1)
        for planet in galactic[planet_visited.name].orbiters:
            if planet != "YOU":
                find_santa(galactic[planet], galactic, path + 1)


def follow_to_COM(galactic):
    total_orbits = 0
    for planet in galactic:
        current_planet = galactic[planet]
        while current_planet.name != 'COM':
            current_planet = galactic[current_planet.orbits]
            total_orbits += 1
    return total_orbits


part1and2(orbits)
