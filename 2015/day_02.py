import sys
import termcolor_util as tc
from typing import Tuple
import time


test = ["1x2x1","1x1x2"]


def load_input(fname):
    with open(fname, "r") as f:
        file = f.read().strip()
        return file


def prepare_file(file):
    dimension_list = file.split("\n")
    return dimension_list


def get_dimensions(dimension_list, index):
    length = int(dimension_list[index].split("x", 2)[0])
    width = int(dimension_list[index].split("x", 2)[1])
    height = int(dimension_list[index].split("x", 2)[2])
    dim = [length, width, height]
    return dim


def get_area_sides(dimension_list, index):
    dim = get_dimensions(dimension_list, index)
    lxw = dim[0] * dim[1]
    wxh = dim[1] * dim[2]
    hxl = dim[2] * dim[0]

    area_sides = [lxw, wxh, hxl]
    return area_sides


def get_smallest_side(dimension_list, index):
    area_sides = get_area_sides(dimension_list, index)
    smallest_side_index = min(range(len(area_sides)), key=area_sides.__getitem__)
    return smallest_side_index


def get_smallest_perimeter(dimension_list, index):
    dim = get_dimensions(dimension_list, index)
    smallest_side_index = get_smallest_side(dimension_list, index)

    if smallest_side_index == 0:
        smallest_perimeter = (2 * dim[0]) + (2 * dim[1])

    elif smallest_side_index == 1:
        smallest_perimeter = (2 * dim[1]) + (2 * dim[2])

    elif smallest_side_index == 2:
        smallest_perimeter = (2 * dim[2]) + (2 * dim[0])

    return smallest_perimeter


def get_paper_needed(dimension_list, index):
    area_sides = get_area_sides(dimension_list, index)
    smallest_side_index = get_smallest_side(dimension_list, index)

    surface_area = (2 * area_sides[0]) + (2 * area_sides[1]) + (2 * area_sides[2])
    smallest_side = area_sides[smallest_side_index]
    extra_paper = smallest_side
    paper_needed = surface_area + extra_paper
    return paper_needed


def get_ribbon_needed(dimension_list, index):
    dim = get_dimensions(dimension_list, index)
    smallest_perimeter = get_smallest_perimeter(dimension_list, index)
    cubic_volume = dim[0] * dim[1] * dim[2]
    ribbon_needed = smallest_perimeter + cubic_volume
    return ribbon_needed


def part_a(dimension_list):
    total_paper_needed = 0
    for index in range(len(dimension_list)):
        added_paper = get_paper_needed(dimension_list, index)
        total_paper_needed = total_paper_needed + added_paper
    return total_paper_needed


def part_b(dimension_list):
    total_ribbon_needed = 0

    for index in range(len(dimension_list)):
        added_ribbon = get_ribbon_needed(dimension_list, index)
        total_ribbon_needed = total_ribbon_needed + added_ribbon
    return total_ribbon_needed


def main(fname):
    file = load_input(fname)
    dimension_list = prepare_file(file)
    #dimension_list = test

    start = time.time()
    print(f"The Answer to Part A is: {tc.green(part_a(dimension_list))}")
    print("Time taken to get answer: {:.6f} seconds".format(time.time() - start))

    start = time.time()
    print(f"The Answer to Part B is: {tc.green(part_b(dimension_list))}")
    print("Time taken to get answer: {:.6f} seconds".format(time.time() - start))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python [script.py] [input.txt]")
    else:
        main(sys.argv[1])
