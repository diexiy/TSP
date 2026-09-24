import random  

fake_cities = {
    "A": (0, 0),
    "B": (0, 3),
    "C": (4, 3),
    "D": (4, 0)
}

def fake_generate_random_route(cities):
    route = list(cities.keys())
    random.shuffle(route)
    return route

print("Route:")

print(fake_generate_random_route(fake_cities))



def generate_population(cities, size):
    population = []

    for i in range(size):
        route = fake_generate_random_route(cities)
        population.append(route)

    return population

population = generate_population(fake_cities, 5)

print("Population:")
for route in population:
    print(route)

def fake_calculate_route_distance(route, cities):
    fake_distances = {
        ("A", "B", "C", "D"): 14,
        ("A", "C", "B", "D"): 22,
        ("A", "D", "C", "B"): 18,
        ("B", "A", "C", "D"): 20
    }

    return fake_distances[tuple(route)]

fake_population = [
    ["A", "B", "C", "D"],
    ["A", "C", "B", "D"],
    ["A", "D", "C", "B"],
    ["B", "A", "C", "D"]
]


def fake_calculate_route_distance(route, cities):
    fake_distances = {
        ("A", "B", "C", "D"): 14,
        ("A", "C", "B", "D"): 8,
        ("A", "D", "C", "B"): 18,
        ("B", "A", "C", "D"): 20
    }

    return fake_distances[tuple(route)]

fake_population = [
    ["A", "B", "C", "D"],
    ["A", "C", "B", "D"],
    ["A", "D", "C", "B"],
    ["B", "A", "C", "D"]
]

def get_best_route(population, cities):

    best_route = population[0]
    best_distance = fake_calculate_route_distance(best_route, cities)

    for route in population:
        distance = fake_calculate_route_distance(route, cities)

        if distance < best_distance:
            best_route = route
            best_distance = distance

    return best_route

best = get_best_route(fake_population, fake_cities)

print("Best route:")
print(best)

print("Best distance:")
print(fake_calculate_route_distance(best, fake_cities))