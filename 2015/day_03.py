import datetime
start_time = datetime.datetime.now()

import sys
import termcolor_util as tc
from typing import Tuple


test = ["^", "v", "v", "v", "v", ">", "^"]

# Start in the centre
first_N_S = 0
first_E_W = 0
coordinates = [(0, 0)]


def load_input(fname):
    with open(fname, "r") as f:
        file = f.read().strip()
        return file


def add_new_direction(direction, last_N_S, last_E_W):

    new_N_S = last_N_S
    new_E_W = last_E_W

    if direction == "^":
        new_N_S = last_N_S + 1

    elif direction == "v":
        new_N_S = last_N_S - 1

    elif direction == ">":
        new_E_W = last_E_W + 1

    elif direction == "<":
        new_E_W = last_E_W - 1

    last_N_S = new_N_S
    last_E_W = new_E_W

    return last_N_S, last_E_W


def part_a(direction_map, coordinates, new_N_S, new_E_W):
    for direction in direction_map:
        new_N_S, new_E_W = add_new_direction(direction, new_N_S, new_E_W)
        coordinates.append((new_N_S, new_E_W))
    return len(list(set(coordinates)))


def main(fname):
    direction_map = load_input(fname)
    #direction_map = test

    print(
        "The Answer to Part A is: {}".format(
            tc.green(part_a(direction_map, coordinates, first_N_S, first_E_W))
        )
    )
    processing_time = (datetime.datetime.now() - start_time).total_seconds() * 1000
    print("Time taken to get answer: {:.3f} ms".format(processing_time))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python [script.py] [input.txt]")
    else:
        main(sys.argv[1])
