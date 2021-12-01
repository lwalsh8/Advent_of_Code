import numpy as np


def read_input(input_file):
    with open(input_file, "r") as f:
        prev_depth = 0
        inc_depth = []
        for line in f:
            depth = int(line)
            if depth > prev_depth:
                inc_depth.append(1)
            else:
                inc_depth.append(0)
            prev_depth = depth
    return inc_depth


def main():
    inc_depth = read_input('input.txt')
    print(f'Number of increasing depths (not including first step): {np.sum(inc_depth) - 1}')


if __name__ == "__main__":
    main()