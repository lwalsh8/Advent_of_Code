import numpy as np
from copy import copy
import sys
import datetime
start_time = datetime.datetime.now()

SWITCH_MAP = {'.': 0, '#': 1}
NUM_ITER = 100


def animate(data, len_x, len_y):
    data1 = copy(data)
    for x in range(len_x):
        for y in range(len_y):
            lower_x_bound = max(0, x-1)
            higher_x_bound = min(len_y, x+2)
            lower_y_bound = max(0, y-1)
            higher_y_bound = min(len_y, y+2)
            num_on_lights = sum(sum(data[lower_x_bound:higher_x_bound, lower_y_bound:higher_y_bound])) - data[x, y]

            if data[x, y] == 1:
                if num_on_lights == 2 or num_on_lights == 3:
                    data1[x, y] = 1
                else:
                    data1[x, y] = 0

            elif data[x, y] == 0:
                if num_on_lights == 3:
                    data1[x, y] = 1
                else:
                    data1[x, y] = 0
    return data1


def main(file):
    with open(file, 'r') as f:
        data = np.array([[SWITCH_MAP[i] for i in line.strip()] for line in f.readlines()])
    for i in range(NUM_ITER):
        data = animate(data, *data.shape)
    print(f"Lights on after {NUM_ITER} iterations: {sum(sum(data))}")
    processing_time = (datetime.datetime.now() - start_time).total_seconds()
    print("Time taken to get answer: {:.3f} seconds".format(processing_time))


if __name__ == '__main__':
    main(sys.argv[1])