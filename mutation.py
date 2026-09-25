import random

def mutation(route, mutation_rate):
    #copies the route 
    new_route = route.copy()
    #takes a random number between 0 and 1
    #checks if that number is less than mutation rate
    #if it is it mutates if not it does not
    #makes the mutation happen for example 5% of the time
    if random.random() < mutation_rate:
        new_route[0], new_route[-1] = new_route[-1], new_route[0]
    return new_route





route =["A", "B", "C", "D"]
new_route = mutation(route, 0.05)

print("Original:", route)
print("New:", new_route)


#mutation(route, 0.05)


'''
#change if statment to take random indexen to mutate
if random.random() < mutation_rate:
    i = random.randint(0, len(new_route) - 1)
    j = random.randint(0, len(new_route) - 1)
    new_route[i], new_route[j] = new_route[j], new_route[i]
'''

