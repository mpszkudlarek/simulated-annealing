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
    current_solution = initial_solution
    c_max = current_solution
    best_c_max = current_solution

    current_energy = cost_function(current_solution)
    pi = current_energy

    temp = initial_temperature

    for iteration in range(num_iterations):
        new_solution = current_solution + random.uniform(-1, 1)
        new_energy = cost_function(new_solution)

        if accept_probability(current_energy, new_energy, temp) > random.uniform(0, 1):
            current_solution = new_solution
            current_energy = new_energy

        if new_energy < pi:
            c_max = new_solution
            pi = new_energy

        if new_energy < cost_function(best_c_max):
            best_c_max = new_solution

        temp *= cool_rate

    if cost_function(c_max) < cost_function(best_c_max):
        return c_max, pi
    else:
        return best_c_max, pi


def get_user_input():
    user_solution = float(input("Enter the initial solution: "))
    user_temp = float(input("Enter the initial temperature: "))
    user_iter = int(input("Enter the number of iterations: "))
    user_cooling_rate = float(input("Enter the cooling rate: "))
    return user_solution, user_temp, user_iter, user_cooling_rate


def print_results(c_max, pi, measurement_time):
    print('\n--------------------Results:--------------------\n')
    print("c_max:", c_max)
    print("pi:", pi)
    print("Execution time:", measurement_time, "seconds")


solution, temperature, iterations, cooling_rate = get_user_input()

start_time = time.time()
final_c_max, final_pi = simulated_annealing(solution, temperature, iterations, cooling_rate)
execution_time = time.time() - start_time

print_results(final_c_max, final_pi, execution_time)
