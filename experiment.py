import random
from cities import generate_cities
from evolution import run_evolution
import statistics
from plotter import plot_results
import os

NUMBER_OF_CITIES = 25
POPULATION_SIZE = 100
GENERATIONS = 5
MUTATION_RATE = 1

NUMBER_OF_RUNS = 5

# Samma karta varje gång
random.seed(50)

#os.remove("results.txt") if os.path.exists("results.txt") else None
if not os.path.exists("results.txt"):
    with open("results.txt", "a") as file:
        file.write("Cities,Average,Stdev,Best,Worst\n")


for city in [5, 10, 15, 20, 25]:
    cities = generate_cities(city)
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
    stdev = statistics.stdev(results) if len(results) > 1 else 0
    
    print("\n--- FINAL RESULTS ---")
    print("All distances:")
    print(results)

    print("\nAverage distance:")
    print(average)

    print("\nBest run:")
    print(min(results))

    print("\nWorst run:")
    print(max(results))
    
    with open("results.txt", "a") as file:
        file.write("Run mutation rate " + str(MUTATION_RATE) + ",")

        file.write(str(city) + ",")
        file.write(str(average) + ",")
        file.write(str(stdev) + ",")
        file.write(str(min(results)) + ",")
        file.write(str(max(results)) + ",")
        file.write("\n")

plot_results()