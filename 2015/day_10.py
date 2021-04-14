import sys
from itertools import groupby
from termcolor import colored
import datetime
start_time = datetime.datetime.now()


def update_text(first_str, total_iter):
    def recursive_bit(iter_num, updated_str):
        if iter_num == total_iter:
            return updated_str
        
        iter_num +=1
        updated_str = "".join("{}{}".format(len(list(count)), int(label)) for label, count in groupby(updated_str))
        return recursive_bit(iter_num, updated_str)
    
    return recursive_bit(0, first_str)
        

def main(puzzle_input, part_num):
    first_str = puzzle_input
    if part_num == '1':
        total_iter = 40
    elif part_num == '2':
        total_iter = 50
    
    print(colored('Length of final string: {}'.format(len(update_text(first_str, total_iter))), "green"))
    processing_time = (datetime.datetime.now() - start_time).total_seconds()
    print(colored("Time taken to get answer: {:.3f} seconds".format(processing_time), "green"))
    

if __name__ == "__main__":
    if len(sys.argv) ==1:
        print("USAGE: python [script.py] [puzzle_input] [part_num]")
        print("Running with defaults: string=1113222113 for 40 iterations")
    if len(sys.argv) > 1:
        puzzle_input = sys.argv[1]
    else:
        puzzle_input = '1113222113'
        
    if len(sys.argv) > 2:
        part_num = sys.argv[2]
    else:
        part_num = '1'
    main(puzzle_input, part_num)