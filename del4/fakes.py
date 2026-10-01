fake_cities={
    "A": (0,0),
    "B": (0,3),
    "C": (4,3),
    "D": (4,0),
}

def fake_generate_population(cities, size):
    routes = [
        ["A", "B", "C", "D"],
        ["A", "C", "B", "D"],
        ["A", "D", "C", "B"],
        ["B", "A", "C", "D"]
    ]
    return routes[:size]
def fake_get_best_route(population, cities):
    return population[0]

def fake_calculate_route_distance(route, cities):
    return 20

def fake_select_parent(population, cities):
    return population[0]

def fake_crossover(parent1, parent2):
    return parent1.copy()

def fake_mutate(route, mutation_rate):
    return route.copy()

