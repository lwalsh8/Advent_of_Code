import sys
import string
import regex as re
from termcolor import colored
import datetime


full_alpha = []
acc_alpha = []
for c in string.ascii_lowercase: 
        full_alpha.append(c)
        if c not in ['o', 'i', 'l']:
            acc_alpha.append(c)

repeated = re.compile(r'(.)\1')


def three_consective(my_str):
    """Check if difference in full alphabet index of consecutive positions is 1"""
    for i, first_letter in enumerate(my_str[:-2]):
        first_index = full_alpha.index(first_letter)
        if full_alpha.index(my_str[i +1]) - first_index == 1:
            if full_alpha.index(my_str[i +2]) - first_index == 2:
                return True
    return False


def non_overlap_repeated(my_str):
    "Get set of all repeated characters, if at least two different repeated characters return True"
    groups = repeated.findall(my_str)
    if len(set(groups)) >= 2:
        return True
    return False

                               
                
def find_next_password(my_str_list):   
    """Starting from right, check if letter is z, if not add 1 and return string, if z
        update to a and re-enter function one letter to the left"""
    def increment_string(my_str_list, pos):
        if my_str_list[pos] != 'z':
            index = acc_alpha.index(my_str_list[pos])
            my_str_list[pos] = acc_alpha[index + 1]
            return ''.join(my_str_list)
        
        my_str_list[pos] = 'a'
        return increment_string(my_str_list, pos-1)
    
    return increment_string(my_str_list, -1)



def find_next_acceptable_password(my_str, iter_cap  = 1000000):
    """Within iteration limit, find incremented password and check if passes requirements"""
    my_str_list = [char for char in my_str]
    iter_num = 0
    while iter_num < iter_cap:
        my_str = find_next_password(my_str_list)
        if all([three_consective(my_str), non_overlap_repeated(my_str)]):
            print('Acceptable new password found')
            return my_str, iter_num
        else:
            iter_num +=1
    raise ValueError('No acceptable password found within iteration cap: ', iter_cap)
            
    
        
def main(my_str):
    print('Starting string: ',my_str)
    start_time = datetime.datetime.now()
    new_password, iter_num = find_next_acceptable_password(my_str)
    print(colored('New password: {}, num of iterations: {}'.format(new_password, iter_num), "green"))
    processing_time = (datetime.datetime.now() - start_time).total_seconds()
    print(colored("Time taken to get answer: {:.3f} seconds".format(processing_time), "green"))
    
    start_time = datetime.datetime.now()
    next_new_password, iter_num = find_next_acceptable_password(new_password)
    print(colored('Next new password: {}, num of iterations: {}'.format(next_new_password, iter_num), "green"))
    processing_time = (datetime.datetime.now() - start_time).total_seconds()
    print(colored("Time taken to get answer: {:.3f} seconds".format(processing_time), "green"))
    

    
if __name__ == "__main__":
    if len(sys.argv) ==1:
        print("USAGE: python [script.py] [input.txt]")
        print("Running with default: string=hepxcrrq")
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        with open(input_file, "r") as f:
            puzzle_input = f.read()
    else:
        puzzle_input = 'hepxcrrq'
        
    main(puzzle_input)