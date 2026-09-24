from cities import generate_cities
from routes import generate_random_route
from routes import calculate_route_distance
from plotter import plot_route

cities = generate_cities(10)

print("cities: ")
print(cities)   

route = generate_random_route(cities)

print("route: ")
print(route)

total_distance = calculate_route_distance(route, cities)

print("total distance:")
print(total_distance)

plot_route(cities, route)