from population import generate_population, get_best_route
from crossover import crossoverRandom
from mutation import mutationRandom
from routes import calculate_route_distance
from selection import select_parent_tournament, select_survivors


def run_generation(population, cities, mutation_rate=0.5, replacement_rate=1.0, tournament_size=30):
    if not 0 <= replacement_rate <= 1:
        raise ValueError("replacement_rate must be between 0 and 1")
                                #100                0.3
    survivor_count = round(len(population) * (1 - replacement_rate)) #100 *(1-0.3)=70 ju lägre replecment rate vi har detso högre elitism vi har. 
    new_population = select_survivors(population, cities, survivor_count)

    while len(new_population) < len(population):
        parent1 = select_parent_tournament(population, cities, tournament_size)
        parent2 = select_parent_tournament(population, cities, tournament_size)
        child = crossoverRandom(parent1, parent2)
        child = mutationRandom(child, mutation_rate)
        new_population.append(child)

    return new_population


def run_evolution(cities, population_size, generations, mutation_rate=0.5, replacement_rate=1.0, tournament_size=30):
    population = generate_population(cities, population_size)
    best_route = get_best_route(population, cities)
    best_distance = calculate_route_distance(best_route, cities)
    history = [best_distance]

    print("Generation 0")
    print("Best route:", best_route)
    print("Best distance:", best_distance)
    print()

    for generation in range(generations):
        population = run_generation(population, cities, mutation_rate, replacement_rate, tournament_size)
        current_best = get_best_route(population, cities)
        current_distance = calculate_route_distance(current_best, cities)

        if current_distance < best_distance:
            best_route = current_best.copy()
            best_distance = current_distance
        history.append(best_distance)

        unique_routes = len(set(tuple(route) for route in population))
        print(
            "Generation", generation + 1,
            "| Best in generation:", current_distance,
            "| Best overall:", best_distance,
            "| Unique routes:", unique_routes
        )

    return best_route, best_distance, history