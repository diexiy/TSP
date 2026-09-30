import random

def crossover(parent1, parent2):

    #the length of the parent
    length = len(parent1)

    #the starting index 
    start = length // 4

    #the ending index last number not included
    end = 3 * length // 4

    #make and empty list for child
    child = []

    #for every index from start to end add that letter from parent 1 to child
    for i in range(start, end):
        child.append(parent1[i])


    #for every index in parent 2 that does not already exist in child, add to parent 1
    for element in parent2:
        if element not in child:
            child.append(element)

    #check that child has the same length as parent1
    if len(child) != len(parent1):
        print("Error, child does not have the same length as parent1")
    #check that child does not have duplicate items
    elif(set(child) != set(parent1)):
        print("Error, child has duplicate items as parent1")
    else:
        print(child)


parent1 = ["A", "B", "C", "D", "E", "F"]
parent2 = ["D", "F", "A", "E", "C", "B"]
crossover(parent1, parent2)
'''
parent1 = ["A", "B", "C", "D", "E", "F", "G", "H"]
parent2 = ["D", "H", "F", "A", "E", "G", "C", "B"]
'''

def crossoverRandom(parent1, parent2):

    length = len(parent1)

    #if start = 6 it chooses a random number between 0 and 4 as the start index 
    start = random.randint(0, length - 2)

    #if start is 2 the end is between 3 and 5 for the end index 
    end = random.randint(start + 1, length - 1)

    child = []

    #for every index from start to end is added to child 
    for i in range(start, end):
        child.append(parent1[i])

    #for every index in parent 2 that does not already exist in child add to parent 1
    for element in parent2:
        if element not in child:
            child.append(element)

    #check that child has the same length as parent1
    if len(child) != len(parent1):
        print("Error, child does not have the same length as parent1")
    #check that child does not have duplicate items
    elif(set(child) != set(parent1)):
        print("Error, child has duplicate items as parent1")
    else:
        print(" ")
    print(child)
crossoverRandom(parent1, parent2)


