import matplotlib.pyplot as plt


def plot_route(cities, route):
    x = []
    y = []

    for city in route:
        x.append(cities[city][0])
        y.append(cities[city][1])

    # Stäng rutten genom att gå tillbaka till första staden
    x.append(cities[route[0]][0])
    y.append(cities[route[0]][1])

    plt.figure(figsize=(12, 8))

    # Rita rutten
    plt.plot(
        x,
        y,
        marker="o",
        linewidth=1.5,
        markersize=6
    )

    # Markera alla städer
    for city in cities:
        city_x = cities[city][0]
        city_y = cities[city][1]

        plt.scatter(city_x, city_y, s=40)

        plt.text(
            city_x + 8,
            city_y + 8,
            city,
            fontsize=9
        )

    # Markera startstad extra tydligt
    start_city = route[0]
    start_x = cities[start_city][0]
    start_y = cities[start_city][1]

    plt.scatter(
        start_x,
        start_y,
        s=150,
        marker="*",
        label=f"Start: {start_city}"
    )

    plt.title("Best TSP Route", fontsize=16)
    plt.xlabel("X coordinate")
    plt.ylabel("Y coordinate")

    plt.grid(True, alpha=0.3)
    plt.legend()

    plt.tight_layout()
    plt.show()