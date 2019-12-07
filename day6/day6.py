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
    you_first_planet = galactic["YOU"].orbits
    santa_first_planet = galactic["SAN"].orbits
    you_path = find_path_to_COM(galactic[you_first_planet], galactic)
    santa_path = find_path_to_COM(galactic[santa_first_planet], galactic)
    you_path.reverse()
    santa_path.reverse()
    last_commun_element = 0
    commun_Path = True
    while commun_Path:
        if you_path[last_commun_element].name == santa_path[last_commun_element].name:
            last_commun_element += 1
        else:
            commun_Path = False
    print("shortest path to santa :" + str(len(you_path) +
                                           len(santa_path) - last_commun_element*2))


def find_path_to_COM(first_planet, galactic):
    planet_visited = first_planet
    path_to_com = []
    while planet_visited.name != "COM":
        path_to_com.append(planet_visited)
        planet_visited = galactic[planet_visited.orbits]
    return path_to_com


def follow_to_COM(galactic):
    total_orbits = 0
    for planet in galactic:
        current_planet = galactic[planet]
        while current_planet.name != 'COM':
            current_planet = galactic[current_planet.orbits]
            total_orbits += 1
    return total_orbits


part1and2(orbits)
