import math
import random
import time


def cost_function(x):
    return x ** 2


def accept_probability(curr_energy, new_energy, temp):
    if new_energy < curr_energy:
        return 1.0
    return math.exp((curr_energy - new_energy) / temp)


def simulated_annealing(initial_solution, initial_temperature, num_iterations, cool_rate):
    curr_solution = initial_solution
    best_solution = curr_solution

    current_energy = cost_function(curr_solution)
    best_energy = current_energy

    temp = initial_temperature

    for iteration in range(num_iterations):
        new_solution = curr_solution + random.uniform(-1, 1)
        new_energy = cost_function(new_solution)

        if accept_probability(current_energy, new_energy, temp) > random.uniform(0, 1):
            curr_solution = new_solution
            current_energy = new_energy

        if new_energy < best_energy:
            curr_solution = new_solution
            current_energy = new_energy

        if new_energy < best_energy:
            best_solution = new_solution
            best_energy = new_energy

        temp *= cool_rate
    return best_energy, best_solution


def get_user_input():
    user_solution = float(input("Enter the initial solution: "))
    user_temp = float(input("Enter the initial temperature: "))
    user_iter = int(input("Enter the number of iterations: "))
    user_cooling_rate = float(input("Enter the cooling rate: "))
    return user_solution, user_temp, user_iter, user_cooling_rate


def print_results(best_solution, best_energy, measurement_time):
    print('\n--------------------Results:--------------------\n')
    print("Best solution:", best_solution)
    print("Best energy:", best_energy)
    print("Execution time:", measurement_time, "seconds")


solution, temperature, iterations, cooling_rate = get_user_input()

start_time = time.time()
final_solution, final_energy = simulated_annealing(solution, temperature, iterations, cooling_rate)
execution_time = time.time() - start_time

print_results(final_solution, final_energy, execution_time)
