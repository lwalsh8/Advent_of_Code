import datetime
start_time = datetime.datetime.now()

import sys
import termcolor_util as tc
from itertools import accumulate


instruction_map = {'^':(1,0), 'v':(-1,0), '>':(0,1), '<':(0,-1)}


def load_input(fname):
    with open(fname, "r") as f:
        file = f.read().strip()
        instruction_list = [instruction_map[s] for s in file]
        return instruction_list

    
def create_seperate_lists(instruction_list):
    santas_list = instruction_list[::2]
    robos_list = instruction_list[1::2]
    return(santas_list, robos_list)


def create_coordinates(my_list):
    def update(loc, delta): return tuple(sum(pair) for pair in zip(loc, delta))
    houses = {(0, 0)}
    houses |= set(accumulate(my_list, update))
    return houses


def part_a(instruction_list):
    return len(create_coordinates(instruction_list))


def part_b(instruction_list):
    santas_list, robos_list = create_seperate_lists(instruction_list)
    santas_houses = create_coordinates(santas_list)
    robos_houses = create_coordinates(robos_list)
    return len(list(santas_houses | robos_houses))


def main(fname):
    direction_map = load_input(fname)

    print("The Answer to Part A is: {}".format(tc.green(part_a(direction_map))))
    
    processing_time = (datetime.datetime.now() - start_time).total_seconds() * 1000
    print("Time taken to get answer: {:.3f} ms".format(processing_time))
    
    
    print("The Answer to Part B is: {}".format(tc.green(part_b(direction_map))))
    
    processing_time = (datetime.datetime.now() - start_time).total_seconds() * 1000
    print("Time taken to get answer: {:.3f} ms".format(processing_time))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python [script.py] [input.txt]")
    else:
        main(sys.argv[1])
