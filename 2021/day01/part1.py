import numpy as np


def read_input(input_file):
    with open(input_file, "r") as f:
        prev_depth = 0
        inc_depths = 0
        for line in f:
            depth = int(line)
            if depth > prev_depth:
                inc_depths +=1
            prev_depth = depth
    return inc_depths


def main():
    inc_depths = read_input('input.txt')
    print(f'Number of increasing depths (not including first step): {inc_depths - 1}')


if __name__ == "__main__":
    main()