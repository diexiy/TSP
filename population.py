
from routes import generate_random_route, calculate_route_distance


def generate_population(cities, size):
    population = []

    for i in range(size):
        route = generate_random_route(cities)
        population.append(route)

    return population

def get_best_route(population, cities):

    best_route = population[0]
    best_distance = calculate_route_distance(best_route, cities)

    for route in population:
        distance = calculate_route_distance(route, cities)

        if distance < best_distance:
            best_route = route
            best_distance = distance

    return best_route

