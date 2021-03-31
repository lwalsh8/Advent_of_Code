import sys
import re
import numpy as np
import datetime
start_time = datetime.datetime.now()


pattern_list = [r"(^\"|\"$)",
                r"(\\\\)|(\\\")|(\\x[0-9a-fA-F]{2})",
                r"(\\\")(?![^\"]*$)",
                r"(\\\\)"
                r"(^\")",
                r"(\"$)",
                r"(\\x[0-9a-fA-F]{2})"]


def load_input(fname):
    with open(fname) as f:
        for line in f:
            yield line.strip()
            
            
def part_1(line):
    line_sub = re.sub(pattern_list[0], '', line)
    line_sub = re.sub(pattern_list[1], 'R', line_sub) # Simplifying sub by adding 'R' for replaced character
    return len(line_sub)
        
        
def part_2(line):
    line_sub = re.sub(pattern_list[2], "\\\\\\\\\\\\\\\\", line)
    line_sub = re.sub(pattern_list[3], "\\\\\\\\\\\"", line_sub)
    line_sub = re.sub(pattern_list[4], '"\\"', line_sub)
    line_sub = re.sub(pattern_list[5], '\\""', line_sub)
    line_sub = re.sub(pattern_list[6], "\\\\\\1", line_sub)
    return len(line_sub)
    
    
def main(input_file):
    part_1_chars = 0
    part_2_chars = 0
    orig_length = 0
    lines = load_input(input_file)
    for line in lines:
        orig_length += len(line)
        part_1_chars += part_1(line)
        part_2_chars += part_2(line)
    

    print('Part 1: Difference: {}'.format(orig_length - part_1_chars))
    print('Part 2: Difference: {}'.format(part_2_chars - orig_length))
    
    processing_time = (datetime.datetime.now() - start_time).total_seconds() * 1000
    print("Time taken to get answer: {:.3f} ms".format(processing_time))
    
    
    
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("USAGE: python [script.py] [input.txt]")
    else:
        main(sys.argv[1])