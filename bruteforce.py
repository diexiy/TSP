from itertools import permutations
from routes import calculate_route_distance


def brute_force_tsp(cities):
    start_city = "A"

    other_cities = list(cities.keys())
    other_cities.remove(start_city)

    best_route = None
    best_distance = float("inf")

    for permutation in permutations(other_cities):

        route = [start_city] + list(permutation)

        current_distance = calculate_route_distance(route, cities)

        if current_distance < best_distance:
            best_distance = current_distance
            best_route = route

    return best_route, best_distance