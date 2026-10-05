from population import generate_population, get_best_route
#from selection import select_parent
from crossover import crossoverRandom
from mutation import mutationRandom
from routes import calculate_route_distance
from crossover import crossoverRandom
from mutation import mutationRandom
from selection import select_parent_tournament, select_survivors


def run_generation(population, cities, mutation_rate, replacement_rate=0.8):
    if not 0 <= replacement_rate <= 1:
        raise ValueError("replacement_rate must be between 0 and 1")

    survivor_count = round(len(population) * (1 - replacement_rate))
    new_population = select_survivors(population, cities, survivor_count)

    while len(new_population) < len(population):

        parent1 = select_parent_tournament(population, cities)
        parent2 = select_parent_tournament(population, cities)
        child = crossoverRandom(parent1, parent2)
        child = mutationRandom(child, mutation_rate)
        new_population.append(child)

    return new_population

#result = run_generation(fake_generate_population(fake_cities, 4), fake_cities, 0.05)
#print(result)

def run_evolution(cities, population_size, generations, mutation_rate, replacement_rate=0.8):
    population = generate_population(cities, population_size)
    best_route = get_best_route(population, cities)
    best_distance = calculate_route_distance(best_route, cities)
    
    history = [best_distance]

    #printar vi våra startvärden
    print("Generation 0")
    print("Best route:", best_route)
    print("Best distance:", best_distance)
    print()
    
    for generation in range(generations):
     
        population = run_generation(population, cities, mutation_rate, replacement_rate)
        current_best = get_best_route(population, cities)
        current_distance = calculate_route_distance(current_best,cities)

        history.append(best_distance)

       
        if current_distance < best_distance:
            best_route = current_best.copy()
            best_distance = current_distance 


        unique_routes = len(set(tuple(route) for route in population))

        print(
            "Generation", generation + 1,
            "| Best in generation:", current_distance,
            "| Best overall:", best_distance,
            "| Unique routes:", unique_routes
        )
    
    return best_route, best_distance, history

#result = run_evolution(fake_cities, 4,5,0.05)
#print(result)