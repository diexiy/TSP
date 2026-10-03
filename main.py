import random

from cities import generate_cities
from evolution import run_evolution
from plotter import plot_route
from bruteforce import brute_force_tsp

# settings
NUMBER_OF_CITIES = 100
POPULATION_SIZE = 100
GENERATIONS = 500
MUTATION_RATE = 0.05

random.seed(50)

cities = generate_cities(NUMBER_OF_CITIES)

random.seed()

best_route, best_distance, history = run_evolution(
    cities,
    POPULATION_SIZE,
    GENERATIONS,
    MUTATION_RATE
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

'''
optimal_route, optimal_distance = brute_force_tsp(cities)

print("\n--- COMPARISON ---")
print("GA distance:", best_distance)
print("Optimal distance:", optimal_distance)

difference = best_distance - optimal_distance
percentage = (difference / optimal_distance) * 100

print("Difference:", difference)
print("GA is", percentage, "% above optimal")


'''