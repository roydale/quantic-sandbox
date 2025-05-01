"""
A program that asks the user what city they're starting in and computes the sequence of cities 
to visit that results in all cities being visited once and only once at the lowest cost. The 
output should show the sequence, the cost of each leg, and the total cost.

The data is in the format "origin city | destination city | airfare".
"""

import itertools
import os

def read_airfares(filename):
    graph = {}
    cities = set()
    with open(filename, 'r') as file:
        for line in file:
            origin, destination, cost = map(str.strip, line.strip().split('|'))
            cost = float(cost)
            if origin not in graph:
                graph[origin] = {}
            graph[origin][destination] = cost
            cities.update([origin, destination])
    return graph, list(cities)

def calculate_total_cost(graph, path):
    total_cost = 0
    cost_details = []
    for i in range(len(path) - 1):
        cost = graph[path[i]].get(path[i+1], float('inf'))
        cost_details.append((path[i], path[i+1], cost))
        total_cost += cost
    return total_cost, cost_details

def find_optimal_path(graph, cities, start_city):
    other_cities = [city for city in cities if city != start_city]
    min_cost = float('inf')
    best_path = []
    best_cost_details = []

    for perm in itertools.permutations(other_cities):
        path = [start_city] + list(perm)
        total_cost, cost_details = calculate_total_cost(graph, path)
        if total_cost < min_cost:
            min_cost = total_cost
            best_path = path
            best_cost_details = cost_details

    return best_path, best_cost_details, min_cost

def main():
    current_directory = os.getcwd()
    folder_directory = f"{current_directory}\\airfareCc_files"
    airfare_file_path = f"{folder_directory}\\airfares.txt"
    
    graph, cities = read_airfares(airfare_file_path)

    start_city = input("Enter your starting city: ").strip()
    if start_city not in cities:
        print("Starting city not found in data.")
        return

    path, details, total = find_optimal_path(graph, cities, start_city)

    print("\nOptimal Route:")
    for leg in details:
        print(f"{leg[0]} -> {leg[1]}: ${leg[2]}")
    print(f"Total Cost: ${total}")

if __name__ == "__main__":
    main()
