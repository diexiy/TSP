# Runs several settings of the genetic algorithm for TSP, saves all
# results to a CSV file and draws three graphs:
#   1. Route length vs number of cities
#   2. Running time vs number of cities
#   3. Convergence curve (best distance per generation)
# The line is the median over all runs, and the shaded area
# shows the 25-75 % range of the runs.

import contextlib
import csv
import io
import random
import time

import matplotlib.pyplot as plt
import numpy as np

from cities import generate_cities
from evolution import run_evolution

# ---------------- Settings (change here) ----------------
CITY_SIZES = [10,20,30,40,50]   # problem sizes to test
NUMBER_OF_RUNS = 10              # runs per setting
POPULATION_SIZE = 100
GENERATIONS = 300

# Each row is a setting that is compared. Change ONE thing at a time.
CONFIGS = {
   "Final Combination ": {"mutation_rate": 0.5, "replacement_rate": 1.0, "tournament_size": 30},

}
# -----------------------------------------------------------

rows = []                                   # one row per run
histories = {name: [] for name in CONFIGS}  # curves for the largest size
largest = max(CITY_SIZES)

for n in CITY_SIZES:
    # Same cities for all settings, so the comparison is fair
    random.seed(1000 + n)
    cities = generate_cities(n)

    for name, params in CONFIGS.items():
        for run in range(NUMBER_OF_RUNS):
            random.seed(run)                # same random start for each run
            start = time.time()
            # Silence the printing from run_evolution during the experiment
            with contextlib.redirect_stdout(io.StringIO()):
                _, best_distance, history = run_evolution(
                    cities, POPULATION_SIZE, GENERATIONS, **params
                )
            elapsed = time.time() - start

            rows.append({
                "config": name,
                "cities": n,
                "run": run,
                "best_distance": best_distance,
                "time_sec": elapsed,
            })
            if n == largest:
                histories[name].append(history)
        print(f"Done: {n} cities, {name}")

# ---------------- Save numerical results ----------------
with open("experiment_results.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["config", "cities", "run", "best_distance", "time_sec"])
    writer.writeheader()
    writer.writerows(rows)
print("Saved experiment_results.csv")


# ---------------- Draw the graphs ----------------
def quartiles(config, key, n):
    values = [r[key] for r in rows if r["config"] == config and r["cities"] == n]
    return np.percentile(values, [25, 50, 75])


fig, axes = plt.subplots(1, 3, figsize=(17, 5))
fig.suptitle(f"TSP Genetic Algorithm (population {POPULATION_SIZE}, {GENERATIONS} generations, "
             f"{NUMBER_OF_RUNS} runs per point)")

for ax, key, title, ylabel in [
    (axes[0], "best_distance", "Route length", "Distance (lower = better)"),
    (axes[1], "time_sec", "Running time", "Seconds"),
]:
    for name in CONFIGS:
        q = np.array([quartiles(name, key, n) for n in CITY_SIZES])
        ax.plot(CITY_SIZES, q[:, 1], marker="o", label=name)
        ax.fill_between(CITY_SIZES, q[:, 0], q[:, 2], alpha=0.2)
    ax.set_title(title)
    ax.set_xlabel("Number of cities")
    ax.set_ylabel(ylabel)
    ax.grid(True, alpha=0.4)
    ax.legend()

ax = axes[2]
for name in CONFIGS:
    h = np.array(histories[name])
    q25, med, q75 = np.percentile(h, [25, 50, 75], axis=0)
    gens = np.arange(len(med))
    ax.plot(gens, med, label=name)
    ax.fill_between(gens, q25, q75, alpha=0.2)
ax.set_title(f"Convergence ({largest} cities)")
ax.set_xlabel("Generation")
ax.set_ylabel("Best distance so far")
ax.grid(True, alpha=0.4)
ax.legend()

plt.tight_layout()
plt.savefig("experiment_graphs.png", dpi=150)
print("Saved experiment_graphs.png")
plt.show()