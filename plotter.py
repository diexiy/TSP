import matplotlib.pyplot as plt

def plot_route(cities, route):
    x = []
    y = []

    for city in route:
        x.append(cities[city][0])
        y.append(cities[city][1])

    # lägg till första staden igen så rutten stängs
    x.append(cities[route[0]][0])
    y.append(cities[route[0]][1])

    plt.plot(x, y, marker="o")

    for city in cities:
        plt.text(cities[city][0], cities[city][1], city)

    plt.show()