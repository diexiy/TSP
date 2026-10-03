import random
from cities import generate_cities
from evolution import run_evolution

NUMBER_OF_CITIES = 100
POPULATION_SIZE = 100
GENERATIONS = 500
MUTATION_RATE = 0.05

NUMBER_OF_RUNS = 20

# Samma karta varje gång
random.seed(50)
cities = generate_cities(NUMBER_OF_CITIES)

results = []

for run in range(NUMBER_OF_RUNS):

    # Ny slump för själva GA:n
    random.seed()

    best_route, best_distance, history = run_evolution(
        cities,
        POPULATION_SIZE,
        GENERATIONS,
        MUTATION_RATE
    )

    results.append(best_distance)

    print("Run", run + 1, "| Best distance:", best_distance)


average = sum(results) / len(results)

print("\n--- FINAL RESULTS ---")
print("All distances:")
print(results)

print("\nAverage distance:")
print(average)

print("\nBest run:")
print(min(results))

print("\nWorst run:")
print(max(results))