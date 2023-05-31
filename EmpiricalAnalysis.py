import time
import matplotlib.pyplot as plt
from dynamic_bin import bin_packing as dynamic_binPacking
from greedy_bin import bin_packing as greedy_binPacking


# def analyze_runtime(function, items, bin_capacity):
#     start_time = time.time()
#     function(list(items), bin_capacity)  # Convert items to a list
#     end_time = time.time()
#     return end_time - start_time


# def plot_time_complexity(input_sizes, dp_runtimes, greedy_runtimes):
#     plt.plot(input_sizes, dp_runtimes, label='Dynamic Programming')
#     plt.plot(input_sizes, greedy_runtimes, label='Greedy Algorithm')
#     plt.xlabel('Input Size')
#     plt.ylabel('Runtime (seconds)')
#     plt.title('Time Complexity Analysis')
#     plt.legend()
#     plt.show()


# if __name__ == "__main__":
#     # Initialize empty lists to store input sizes and runtimes
#     input_sizes = []
#     dp_runtimes = []
#     greedy_runtimes = []

#     # Set the range of input sizes to test
#     min_input_size = 10
#     max_input_size = 100
#     step_size = 10

#     for input_size in range(min_input_size, max_input_size + 1, step_size):
#         # Create a list of items with random sizes
#         items = [(i, f"Item {i}") for i in range(1, input_size + 1)]

#         # Set the bin capacity
#         bin_capacity = input_size * 2

#         # Analyze the runtime for each function
#         dp_runtime = analyze_runtime(dynamic_binPacking, items, bin_capacity)
#         greedy_runtime = analyze_runtime(greedy_binPacking, items, bin_capacity)

#         # Append the input size and runtimes to the respective lists
#         input_sizes.append(input_size)
#         dp_runtimes.append(dp_runtime)
#         greedy_runtimes.append(greedy_runtime)

#     # Plot the time complexity analysis
#     plot_time_complexity(input_sizes, dp_runtimes, greedy_runtimes)

import time
import matplotlib.pyplot as plt
from dynamic_bin import bin_packing as dynamic_binPacking
from greedy_bin import bin_packing as greedy_binPacking

def analyze_runtime(function, items, bin_capacity):
    start_time = time.time()
    # time.sleep(1)
    function(list(items), bin_capacity)  # Convert items to a list
    end_time = time.time()
    return end_time - start_time

def plot_time_complexity(input_sizes, runtimes, algorithm_name):
    plt.plot(input_sizes, runtimes, label=algorithm_name)
    plt.xlabel('Input Size')
    plt.ylabel('Runtime (seconds)')
    plt.title('Time Complexity Analysis')
    plt.legend()
    plt.yscale('log')
    plt.show()

if __name__ == "__main__":
    # Initialize empty lists to store input sizes and runtimes
    input_sizes = []
    dp_runtimes = []
    greedy_runtimes = []

    # Set the range of input sizes to test
    min_input_size = 1000
    max_input_size = 10000
    step_size = 1000

    for input_size in range(min_input_size, max_input_size + 1, step_size):
        # Create a list of items for the greedy algorithm
        greedy_items = [(i, f"Item {i}") for i in range(1, input_size + 1)]

        # Create a list of items for the dynamic programming algorithm
        dynamic_items = list(range(1, input_size + 1))

        # Set the bin capacity
        bin_capacity = input_size * 2

        # Analyze the runtime for each function
        dp_runtime = analyze_runtime(dynamic_binPacking, dynamic_items, bin_capacity)
        greedy_runtime = analyze_runtime(greedy_binPacking, greedy_items, bin_capacity)

        # Append the input size and runtimes to the respective lists
        input_sizes.append(input_size)
        dp_runtimes.append(dp_runtime)
        greedy_runtimes.append(greedy_runtime)

    # Plot the time complexity analysis
    print(greedy_runtimes)
    plot_time_complexity(input_sizes, greedy_runtimes, 'Greedy Algorithm')
    plot_time_complexity(input_sizes, dp_runtimes, 'Dynamic Algorithm')
    


