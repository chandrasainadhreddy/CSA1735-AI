import itertools

# Function to calculate the total distance of a given tour
def calculate_total_distance(tour, distance_matrix):
    total_distance = 0
    number_of_cities = len(tour)
    for i in range(number_of_cities):
        total_distance += distance_matrix[tour[i - 1]][tour[i]]
    return total_distance

# Function to solve the TSP using brute-force approach
def solve_tsp_brute_force(distance_matrix):
    number_of_cities = len(distance_matrix)
    cities = list(range(number_of_cities))
    min_distance = float('inf')
    optimal_tour = []

    for tour in itertools.permutations(cities[1:]):
        current_tour = [0] + list(tour) + [0]
        current_distance = calculate_total_distance(current_tour, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            optimal_tour = current_tour

    return min_distance, optimal_tour

if __name__ == "__main__":
    # Example distance matrix representing the distances between cities
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    min_distance, optimal_tour = solve_tsp_brute_force(distance_matrix)

    print(f"Minimum travel distance: {min_distance}")
    print(f"Optimal tour: {optimal_tour}")
