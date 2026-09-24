import random 
from cities import distance

def generate_random_route(cities):
    start_city = "A"

    remaining_cities = list(cities.keys())
    remaining_cities.remove(start_city)


    
    random.shuffle(remaining_cities)

    route = [start_city] + remaining_cities

    return route


def calculate_route_distance(route, cities):
    total_distance = 0

    for i in range(len(route)-1):
        total_distance += distance(route[i], route[i + 1], cities)

    total_distance += distance (route[-1], route[0], cities)

    return total_distance
