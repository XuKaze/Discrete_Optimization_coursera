#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
import numpy as np
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm
    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []
    for i in range(1, item_count + 1):
        line = lines[i]
        parts = line.split()
        items.append([i - 1, int(parts[0]), int(parts[1])])

    if item_count > 30:
        items_array = np.array(items)
        # a trivial algorithm for filling the knapsack
        # it takes items in-order until the knapsack is full
        value_density = np.append(items_array, (items_array[:, 1] / items_array[:, 2]).reshape(-1, 1), axis=1)
        items_array_sorted = value_density[value_density[:, 3].argsort()[::-1]]

        value = 0
        weight = 0
        taken = [0] * items_array_sorted.shape[0]
        for i in range(0, items_array_sorted.shape[0]):
            if weight + items_array_sorted[:, 2][i] <= capacity:
                value += int(items_array_sorted[:, 1][i])
                weight += int(items_array_sorted[:, 2][i])
                taken[int(items_array_sorted[:, 0][i])] = 1
    else:
        items_array = np.array(items)
        items_array_sorted = items_array[items_array[:, 2].argsort()]
        value = 0
        weight = 0
        taken = [0] * items_array_sorted.shape[0]

        for i in range(0, items_array_sorted.shape[0]):
            if weight + items_array_sorted[:, 2][i] <= capacity:
                value += items_array_sorted[:, 1][i]
                weight += items_array_sorted[:, 2][i]
                taken[items_array_sorted[:, 0][i]] = 1



    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

