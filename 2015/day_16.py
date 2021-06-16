import re
import sys
import datetime
start_time = datetime.datetime.now()
from collections import namedtuple


facts_dict = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1}

all_facts = facts_dict.keys()
more_than_facts = ['cats', 'trees']
less_than_facts = ['pomeranians', 'goldfish']
equal_facts = list(set(all_facts) - set(more_than_facts + less_than_facts))


def parse_input(line):
    sue, *identifiers = re.match(r'Sue ([0-9]*): (.*), (.*), (.*)', line).groups()
    return int(sue), identifiers


def create_sue_dict(file):
    sues = {}
    with open(file, 'r') as f:
        for line in f:
            sue, identifiers = parse_input(line)
            sues[sue] = {i.split(': ')[0]: int(i.split(': ')[1]) for i in identifiers}
    return sues


def run_search(sues, part_num):
    for sue in sues.keys():
        sues_facts = sues[sue].keys()
        
        if part_num == '1':
            rel_dict = {c: facts_dict[c] for c in [e for e in all_facts if e in sues_facts]}
            sues_rel_dict = {c: sues[sue][c] for c in rel_dict.keys()}
            if rel_dict == sues_rel_dict:
                return sue
            
        elif part_num == '2':
            matching = True
            rel_dict = {c: facts_dict[c] for c in [e for e in equal_facts if e in sues_facts]}
            sues_rel_dict = {c: sues[sue][c] for c in rel_dict.keys()}
            less_than_dict = {c: facts_dict[c] for c in [e for e in less_than_facts if e in sues_facts]}
            more_than_dict = {c: facts_dict[c] for c in [e for e in more_than_facts if e in sues_facts]}
        
            if rel_dict == sues_rel_dict:
                for c in less_than_dict.keys():
                    if less_than_dict[c] <= sues[sue][c]:
                        matching = False
                for c in more_than_dict.keys():
                    if more_than_dict[c] >= sues[sue][c]:
                        matching = False
                if matching:
                    return sue
                            
            
def main(puzzle_input, part_num):
    sues = create_sue_dict(puzzle_input)
    sue = run_search(sues, part_num)
    
    print('Sue {} is the matching sue with facts: {}'.format(sue, sues[sue]))
    processing_time = (datetime.datetime.now() - start_time).total_seconds() *1000
    print("Time taken to get answer: {:.3f} milliseconds".format(processing_time))

    
    
if __name__ == "__main__":
    if len(sys.argv) ==1:
        print("USAGE: python [script.py] [puzzle_input] [part_num]")
        print("Running with defaults: input.txt part 1")
    if len(sys.argv) > 1:
        puzzle_input = sys.argv[1]
    else:
        puzzle_input = "input.txt"
        
    if len(sys.argv) > 2:
        part_num = sys.argv[2]
    else:
        part_num = '1'
    main(puzzle_input, part_num)
