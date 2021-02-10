import datetime
start_time = datetime.datetime.now()

import sys
import hashlib


def cycle_through_numbers(puzzle_input, starting_i, num_zeroes):
    i =starting_i
    while True:
        new_input = puzzle_input+str(i)
        md5 = hashlib.md5(new_input).hexdigest()
        zeroes = len(md5) - len(md5.lstrip('0'))
        if zeroes == num_zeroes:
            break
        else:
            i +=1
    return i


def main(puzzle_input): 
    part_a = cycle_through_numbers(puzzle_input,0, 5)
    print('Answer to part a is {}'.format(part_a))
    processing_time = (datetime.datetime.now() - start_time).total_seconds() * 1000
    print("Time taken to get answer: {:.3f} ms".format(processing_time))
    
    
    part_b = cycle_through_numbers(puzzle_input,part_a, 6)
    print('\nAnswer to part b is {}'.format(part_b))
    processing_time = (datetime.datetime.now() - start_time).total_seconds() * 1000
    print("Time taken to get answer: {:.3f} ms".format(processing_time))



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python [script.py] [input]")
    else:
        main(sys.argv[1])
