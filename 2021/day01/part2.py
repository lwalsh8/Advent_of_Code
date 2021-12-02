import numpy as np


def read_input(input_file):
    depths = []
    with open(input_file, "r") as f:
        for line in f:
            depths.append(int(line))
    return depths


def window_avgs(depths, w_size):
    return (np.mean([deps for deps in zip([depths[pos + s] for s in range(w_size)])]) for pos in range(len(depths)-w_size+1))


def var_window(window_avg_depths):
    prev_dep = 0
    inc_depth = 0
    for dep in window_avg_depths:
        if dep > prev_dep:
            inc_depth += 1
        prev_dep = dep
    return inc_depth


def main():
    w_size = 3
    depths = read_input('input.txt')
    window_avg_depths = window_avgs(depths, w_size)
    inc_depth = var_window(window_avg_depths)
    print(f'Number of increasing depths (not including first step): {inc_depth - 1}')


if __name__ == "__main__":
    main()