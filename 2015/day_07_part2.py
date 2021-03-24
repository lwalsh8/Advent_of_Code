## Heavily 'inspired' by solution c Part 1!

import re
import sys
import datetime
start_time = datetime.datetime.now()
import copy


signal_dict = {}

op_dict = {'ASGN': lambda x, y: y,
           'NOT': lambda x, y: ~y,
           'AND': lambda x, y: x & y,
           'OR': lambda x, y: x | y,
           'LSHIFT': lambda x, y: x << y,
           'RSHIFT': lambda x, y: x >> y}



def check_numeric(element):
    if element.isnumeric():
        return int(element)
    else:
        return run_recursive_iterator(element)


def run_recursive_iterator(operation):
    opn, input_1, input_2 = signal_dict[operation]
    result = opn(check_numeric(input_1), check_numeric(input_2))
    signal_dict[operation] = (op_dict['ASGN'], '0', str(result))
    return result


def load_input(fname):
    with open(fname) as f:
        for line in f:
            yield line.strip()
        
        
def add_to_dict(line):
    m = re.search(r'(.*) (\w*) (.*) -> (\w*)', line)
    if m:
        elements = m.groups()
    else:
        m = re.search(r'(\w*) (.*) -> (\w*)', line)
        if m:
            elements = ('0', *m.groups())
        else:
            m = re.search(r'(.*) -> (\w*)', line)
            if m:
                elements = ('0', 'ASGN', *m.groups())
            else:
                elements = ()

    if len(elements) > 0:
        input_1, opn_name, input_2, output = elements
        signal_dict[output] = (op_dict[opn_name], input_1, input_2)


def main(input_file, part_num):
    wire_of_interest = 'a'
    update_wire = 'b'
    lines = load_input(input_file)
    for line in lines:
            add_to_dict(line)
    signal_1 = run_recursive_iterator(wire_of_interest)
    print('Part1 - Signal passed to {}: {}'.format(wire_of_interest, signal_1))
    processing_time = (datetime.datetime.now() - start_time).total_seconds() * 1000
    print("Time taken to get answer: {:.3f} ms".format(processing_time))

    if part_num == 2:
        lines = load_input(input_file)
        for line in lines:
            add_to_dict(line)
        signal_dict[update_wire] = (op_dict['ASGN'], '0', str(signal_1))
        signal_2 = run_recursive_iterator(wire_of_interest)
        print('Part2 - Signal passed to {}: {}'.format(wire_of_interest, signal_2))
        processing_time = (datetime.datetime.now() - start_time).total_seconds() * 1000
        print("Time taken to get answer: {:.3f} ms".format(processing_time))

          
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("USAGE: python [script.py] [input.txt] ['part_num']")
    elif len(sys.argv) < 3:
        part_num = 1
        main(sys.argv[1], part_num)
    else:
        part_num = int(sys.argv[2])
        main(sys.argv[1], part_num)