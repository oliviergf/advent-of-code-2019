inputs = open("day6/input.txt", "r")
orbits = list(map(lambda x: x.rstrip(), inputs.readlines()))


class Planet:
    def __init__(self, name):
        self.orbiters = []
        self.orbits = ""
        self.name = name

    def add_orbiter(self, orbited_by):
        self.orbiters.append(orbited_by)

    def orbits_planet(self, planet):
        self.orbits = planet


def part1(orbits):
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

    direct_orbits = len(galactic)
    indirect_orbits = follow_to_COM(galactic)
    print(indirect_orbits)


def follow_to_COM(galactic):
    indirectOrbits = 0
    for planet in galactic:
        current_planet = galactic[planet]
        while current_planet.name != 'COM':
            current_planet = galactic[current_planet.orbits]
            indirectOrbits += 1
    return indirectOrbits


part1(orbits)
