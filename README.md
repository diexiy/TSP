# TSP
# Genetic Algorithm for the Travelling Salesman Problem (TSP)

TARI29 Artificial Intelligence, Evolutionary Computation assignment.

Group members: Leyla Alsheikha, Maria Birtman, Alma Warin, Fadumo Jama

## Overview

A genetic algorithm (GA) that finds a short closed route through a set of random
cities. A route is a permutation of the city names, starting at "A", and its
fitness is the total route length (shorter is better).

- **Selection:** tournament selection
- **Crossover:** `crossoverRandom` (a segment from parent 1, the rest in the order of parent 2)
- **Mutation:** swap of two random cities
- **Replacement:** the whole population is replaced each generation

## Files

- `main.py`: runs one GA and plots the best route (settings at the top)
- `evolution.py`: the GA loop
- `cities.py`, `routes.py`, `population.py`: cities, route length, start population
- `selection.py`, `crossover.py`, `mutation.py`: the genetic operators
- `plotter.py`: plots the route
- `experiment_plot.py`: runs the experiments and makes the graphs

## How to run

```
pip install matplotlib
python main.py              # one run
python experiment_plot.py   # experiments (takes a few minutes)
```

Final settings: 50 cities, population 100, 300 generations, mutation rate 0.5,
replacement rate 1.0, tournament size 30.

## Main findings

- Replacing the whole population worked best; keeping survivors made results worse.
- Mutation rate 0.05 was too low; 0.2 to 0.8 gave similar results.
- Tournament size 10 was too weak; 15 to 60 were similar, and run time grows with size, so 30 was chosen.
- Running time grows roughly linearly with the number of cities.