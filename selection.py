import random

from routes import calculate_route_distance


def fitness(route, cities):
    distance = calculate_route_distance(route, cities)
    fitness = 1/ distance
    return fitness


def select_parent_wheel(population, cities):
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


def select_survivors(population, cities, survivor_count):
    candidates = population.copy()
    survivors = []

    while len(survivors) < survivor_count:
        fitness_values = [fitness(route, cities) for route in candidates]
        selected_index = random.choices(
            range(len(candidates)),
            weights=fitness_values,
            k=1
        )[0]
        survivors.append(candidates.pop(selected_index))

    return survivors


def select_parent_tournament(population, cities):
    candidates = random.sample(population, 10)

    best_parent = candidates[0]
    best_distance = calculate_route_distance(best_parent, cities)

    for route in candidates:
        current_distance = calculate_route_distance(route, cities)

        if current_distance < best_distance:
            best_parent = route
            best_distance = current_distance

    return best_parent


def select_parent_random(population):
    parent = random.choice(population)
    return parent

