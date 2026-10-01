import random

from cities import generate_cities
from population import generate_population, get_best_route
from selection import select_parent
from routes import calculate_route_distance
from plotter import plot_route

# Gör slumpen reproducerbar med ett bestömt startläge för slumpen
random.seed(42)

# Skapa städer
cities = generate_cities(10)

# Skapa population
population = generate_population(cities, 5)

print("Population:")
for route in population:
    print(route)

# Välj två föräldrar
parent1 = select_parent(population, cities)
parent2 = select_parent(population, cities)

print("\nParent 1:")
print(parent1)

print("\nParent 2:")
print(parent2)

# Visa deras distanser
print("\nParent 1 distance:")
print(calculate_route_distance(parent1, cities))

print("\nParent 2 distance:")
print(calculate_route_distance(parent2, cities))

# Visa bästa routen också
best_route = get_best_route(population, cities)

print("\nBest route:")
print(best_route)

print("\nBest route distance:")
print(calculate_route_distance(best_route, cities))

plot_route(cities, best_route)