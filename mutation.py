def mutation(route, mutation_rate):
    new_route = route.copy()
    route[0] = route[-1] #swap first letter and last letter
    route[-1] = route[0] #swap last letter and first letter 

    # add something to check if we should mutate or not









route =["A", "B", "C", "D"]
mutation(route, 0.05)

