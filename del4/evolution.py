from fakes import fake_cities, fake_generate_population, fake_select_parent, fake_crossover, fake_mutate, fake_get_best_route, fake_calculate_route_distance

def run_generation(population, cities, mutation_rate):
    new_population = []

    best= fake_get_best_route(population, cities)
    new_population.append(best)

    while len(new_population) < len(population):
        parent1 = fake_select_parent(population, cities)
        parent2 = fake_select_parent(population, cities)
        child = fake_crossover(parent1, parent2)
        child = fake_mutate(child, mutation_rate)
        new_population.append(child)
    return new_population

#result = run_generation(fake_generate_population(fake_cities, 4), fake_cities, 0.05)
#print(result)

def run_evolution(cities, population_size, generations, mutation_rate):
    population = fake_generate_population(cities, population_size)

    best_route = fake_get_best_route(population, cities)
    best_distance = fake_calculate_route_distance(best_route, cities)
    history = [best_distance]
    
    for generation in range(generations):
        population = run_generation(population, cities, mutation_rate)
        current_best = fake_get_best_route(population, cities)
        current_distance = fake_calculate_route_distance(current_best,cities)
        if current_distance < best_distance:
            best_route = current_best
            best_distance = current_distance 
        history.append(best_distance)
    return best_route, best_distance, history

#result = run_evolution(fake_cities, 4,5,0.05)
#print(result)