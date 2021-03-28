# 11. Create a Python project to perform some simple statistics on a list of values.

import statistics

list_of_values = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
    elements = int(input())

    list_of_values.append(elements)  # adding the element

print(list_of_values)


def simple_stats():
    mean_list = statistics.mean(list_of_values)
    print("mean_list : ", mean_list)
    geometric_mean_list = statistics.geometric_mean(list_of_values)
    print("geometric_mean_list : ", geometric_mean_list)
    harmonic_mean_list = statistics.harmonic_mean(list_of_values)
    print("harmonic_mean_list : ", harmonic_mean_list)
    median_list = statistics.median(list_of_values)
    print("median_list : ", median_list)
    median_low_list = statistics.median_low(list_of_values)
    print("median_low_list : ", median_low_list)
    median_high_list = statistics.median_high(list_of_values)
    print("median_high_list : ", median_high_list)
    median_grouped_list = statistics.median_grouped(list_of_values)
    print("median_grouped_list : ", median_grouped_list)
    mode_list = statistics.mode(list_of_values)
    print("mode_list : ", mode_list)
    multimode_list = statistics.multimode(list_of_values)
    print("multimode_list : ", multimode_list)
    quantiles_list = statistics.quantiles(list_of_values)
    print("quantiles_list : ", quantiles_list)
    return mean_list, geometric_mean_list, harmonic_mean_list, median_list, median_low_list, median_high_list, median_grouped_list, mode_list, multimode_list, quantiles_list


simple_stats()
