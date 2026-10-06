# Group members: Leyla Alsheikha, Maria Birtman, Alma Warin, Fadumo Jama
# Runs the genetic algorithm for TSP with the final settings,
# prints the result and plots the best route.

import random

from cities import generate_cities
from evolution import run_evolution
from plotter import plot_route

# settings
NUMBER_OF_CITIES = 50
POPULATION_SIZE = 100
GENERATIONS = 300
MUTATION_RATE = 0.5
REPLACEMENT_RATE = 1.0     # 1.0 = no elitism, whole population is replaced
TOURNAMENT_SIZE = 30

#random.seed(50)
random.seed(1000 + NUMBER_OF_CITIES)
cities = generate_cities(NUMBER_OF_CITIES)
random.seed()

best_route, best_distance, history = run_evolution(
    cities,
    POPULATION_SIZE,
    GENERATIONS,
    mutation_rate=MUTATION_RATE,
    replacement_rate=REPLACEMENT_RATE,
    tournament_size=TOURNAMENT_SIZE,
)

with open("history.txt", "w") as file:
    for generation, distance in enumerate(history):
        file.write(f"Generation {generation}: {distance}\n")

print("\n--- RESULT ---")
print("Cities:")
print(cities)

print("\nBest route:")
print(best_route)

print("\nBest distance:")
print(best_distance)

plot_route(cities, best_route)