def crossover(parent1, parent2):
    #the length of the parent
    length = len(parent1)

    #the starting index 
    start = length // 4

    #the ending index last number not included
    end = 3 * length // 4

    #make and empty list for child
    child = []

    #for every index from 1 to 4 add that letter from parent 1 to child
    for i in range(start, end):
        child.append(parent1[i])


    #for every index in parent 2 that does not already exist in child, add to parent 1
    for element in parent2:
        if element not in child:
            child.append(element)

    print(child)
    #check that child has the same length as parent1
    print(len(child) == len(parent1))
    #check that child does not have duplicate items
    print(set(child) == set(parent1))


parent1 = ["A", "B", "C", "D", "E", "F"]
parent2 = ["D", "F", "A", "E", "C", "B"]
crossover(parent1, parent2)

'''
import random

length = len(parent1)

#if start = 6 it chooses a random number between 0 and 4 as the start index 
start = random.randint(0, length - 2)

#if start is 2 the end is between 3 and 5 for the end index 
end = random.randint(start + 1, length - 1)

#for every index from start to end is added to child 
    for i in range(start, end):
        child.append(parent1[i])

#for every index in parent 2 that does not already exist in child add to parent 1
    for element in parent2:
        if element not in child:
            child.append(element)

'''
