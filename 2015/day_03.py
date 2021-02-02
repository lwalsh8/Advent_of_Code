import datetime
start_time = datetime.datetime.now()

import sys
import termcolor_util as tc


def load_input(fname):
    with open(fname, "r") as f:
        file = f.read().strip()
        instruction_list = [s for s in file]
        return instruction_list
    
    
def create_seperate_lists(instruction_list):
    santas_list = instruction_list[::2]
    robos_list = instruction_list[1::2]
    return(santas_list, robos_list)


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
        
    return new_N_S, new_E_W


def map_directions_to_coordinate_list(instruction_list):
    new_N_S = 0
    new_E_W = 0
    coordinates = [(0, 0)]
    for direction in instruction_list:
        new_N_S, new_E_W = add_new_direction(direction, new_N_S, new_E_W)
        coordinates.append((new_N_S, new_E_W))
    return coordinates
    


def part_a(instruction_list):
    coordinates = map_directions_to_coordinate_list(instruction_list)
    return len(set(coordinates))



def part_b(instruction_list):
    santas_list, robos_list = create_seperate_lists(instruction_list)
    santas_houses = map_directions_to_coordinate_list(santas_list)
    robos_houses = map_directions_to_coordinate_list(robos_list)
    return len(set(santas_houses + robos_houses))



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
