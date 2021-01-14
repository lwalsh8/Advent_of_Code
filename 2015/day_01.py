import sys
import termcolor_util as tc
from typing import Tuple
import time


test = ["(", ")", ")", "(", "("]


def replaced(sequence, old, new):
    return [new if x == old else x for x in sequence]


def load_input(fname):
    with open(fname, "r") as f:
        file = list(f.read())
        return file


def prepare_file(file):
    file = replaced(file, "(", 1)
    file = replaced(file, ")", -1)
    return file


def part_a(instructions):
    return sum(instructions)


def part_b(instructions):
    current_floor = 0
    instruction_index = 0
    while instruction_index < len(instructions):
        next_instruction = instructions[instruction_index]
        current_floor = current_floor + next_instruction

        if current_floor == -1:
            break
        else:
            instruction_index += 1
    return instruction_index + 1


def main(fname):
    file = load_input(fname)
    instructions = prepare_file(file)

    start = time.time()
    print(f"The Answer to Part A is: {tc.green(part_a(instructions))}")
    print("Time taken to get answer: {:.6f} seconds".format(time.time() - start))
    start = time.time()
    print(f"The Answer to Part B is: {tc.green(part_b(instructions))}")
    print("Time taken to get answer: {:.6f} seconds".format(time.time() - start))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python [script.py] [input.txt]")
    else:
        main(sys.argv[1])
