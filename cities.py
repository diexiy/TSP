import random

def generate_cities(n):
    cities = {} # cities är en tom diconary, INTE en lista 

    for i in range(n):
        letter = chr(65 + i) # A = letter 65 och chr() är en inbyggd Python-funktion som tar ett heltal och tolkar det som en Unicode-kodpunkt
        x_coordinate = random.randint(0, 100)
        y_coordinate = random.randint(0, 100)


        cities[letter] = (x_coordinate, y_coordinate)
    return cities



def distance(city1, city2, cities): 
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]

    result = ((x2 - x1 )**2 + (y2 - y1 )**2) ** 0.5

    return result



