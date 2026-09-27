import random

from routes import calculate_route_distance


def fitness(route, cities):
    distance = calculate_route_distance(route, cities)
    return 1 / distance


def select_parent(population, cities):
    fitness_values = []

    for route in population:
        route_fitness = fitness(route, cities)
        fitness_values.append(route_fitness)

    parent = random.choices(
        population,
        weights=fitness_values,
        k=1
    )[0]

    return parent

