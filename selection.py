import random

from population import fake_calculate_route_distance, fake_population, fake_cities


def fitness(route, cities):
    distance = fake_calculate_route_distance(route, cities)
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

parent = select_parent(fake_population, fake_cities)

print("Selected parent:", parent)


print("Distance:", fake_calculate_route_distance(parent, fake_cities))
