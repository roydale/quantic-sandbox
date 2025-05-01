import os
import itertools

"""
A program that asks the user what city they're starting in and computes the sequence of cities 
to visit that results in all cities being visited once and only once at the lowest cost. The 
output should show the sequence, the cost of each leg, and the total cost.

The data is in the format "origin city | destination city | airfare".
"""

# Define the graph as a dictionary where keys are cities and values are lists of (destination, airfare) tuples.
graph = {}

# Read the airfare data from a file and populate the graph.
current_directory = os.getcwd()
folder_directory = f"{current_directory}\\airfare_files"
airfare_file_path = f"{folder_directory}\\airfares.txt"

with open(airfare_file_path, 'r') as file:
    for line in file:
        origin, destination, airfare = map(str.strip, line.split(' | '))  # Strip leading/trailing spaces
        airfare = float(airfare)

        if origin not in graph:
            graph[origin] = []
        graph[origin].append((destination, airfare))

# Function to calculate the total cost of a path.
def calculate_path_cost(path):
    total_cost = 0.0
    for i in range(len(path) - 1):
        origin, destination = path[i], path[i + 1]
        for dest, cost in graph[origin]:
            if dest == destination:
                total_cost += cost
                break
    return total_cost

# Function to find the optimal tour using itertools.permutations.
def find_optimal_tour(start_city):
    all_cities = list(graph.keys())
    all_cities.remove(start_city)
    optimal_tour = None
    min_cost = float('inf')

    for permuted_cities in itertools.permutations(all_cities):
        tour = [start_city] + list(permuted_cities) + [start_city]
        tour_cost = calculate_path_cost(tour)

        if tour_cost < min_cost:
            min_cost = tour_cost
            optimal_tour = tour

    return optimal_tour, min_cost

# Get user input for the starting city.
start_city = input("Enter the city you're starting in: ")

if start_city in graph:
    optimal_tour, total_cost = find_optimal_tour(start_city)

    # Print the optimal tour and total cost.
    print("Optimal Tour:")
    for city in optimal_tour:
        print(f"City: {city}")
    print(f"Total Cost: ${total_cost:.2f}")
else:
    print("City not found in the data.")