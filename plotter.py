import matplotlib.pyplot as plt
import csv
import matplotlib.pyplot as plt



def plot_results():

    # Store the data for each run
    runs = {}

    # Read data file
    with open("results.txt", "r") as file:

        reader = csv.reader(file)

        # Skip header
        next(reader)

        for row in reader:

            label = row[0]
            city = int(row[1])
            average = float(row[2])
            stdev = float(row[3])

            # Create a new list for this run if it does not exist
            if label not in runs:
                runs[label] = {
                    "cities": [],
                    "average": [],
                    "stdev": []
                }

            # Add the data to the correct run
            runs[label]["cities"].append(city)
            runs[label]["average"].append(average)
            runs[label]["stdev"].append(stdev)


    # Plot every run
    for label in runs:

        cities = runs[label]["cities"]
        average = runs[label]["average"]
        stdev = runs[label]["stdev"]

        # Calculate standard deviation range
        lower = []
        upper = []

        for i in range(len(average)):
            lower.append(average[i] - stdev[i])
            upper.append(average[i] + stdev[i])

        # Plot average
        plt.plot(
            cities,
            average,
            marker="o",
            label=label
        )

        # Shaded standard deviation
        plt.fill_between(
            cities,
            lower,
            upper,
            alpha=0.2
        )


    plt.xlabel("Number of cities")
    plt.ylabel("Route distance")
    plt.title("TSP Performance vs Number of Cities")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()



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
    
if __name__ == "__main__":
    plot_results()