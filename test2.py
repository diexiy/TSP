import random

from crossover import crossover
from mutation import mutation

print("Testing crossover and mutation with real functions\n")

random.seed(42)

parent1 = ["A", "B", "C", "D", "E", "F"]
parent2 = ["D", "F", "A", "E", "C", "B"]
route = ["A", "B", "C", "D"]

print("Parent 1:", parent1)
print("Parent 2:", parent2)
print("\nCrossover result:")
crossover(parent1, parent2)

print("\nRoute before mutation:", route)
print("Mutation with rate 0.0:", mutation(route, 0.0))
print("Mutation with rate 1.0:", mutation(route, 1.0))

no_mutation = mutation(route, 0.0)
mutated_route = mutation(route, 1.0)

assert len(no_mutation) == len(route)
assert set(no_mutation) == set(route)
assert len(mutated_route) == len(route)
assert set(mutated_route) == set(route)

print("\nMutation checks passed.")