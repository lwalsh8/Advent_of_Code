import sys
import re
import numpy as np
import datetime
start_time = datetime.datetime.now()


def load_input(fname):
    with open(fname, "r") as f:
        file = f.read().strip()
        word_list = file.split("\n")
        word_list = [w.replace('turn off', '0,') for w in word_list]
        word_list = [w.replace('turn on', '1,') for w in word_list]
        word_list = [w.replace('toggle', '2,') for w in word_list]
        word_list = [w.replace('through', ',') for w in word_list]
        word_list = [w.replace(' ', '') for w in word_list]
        word_list = [w.split(",") for w in word_list]
        word_list = [[int(i) for i in w] for w in word_list]
        return word_list

            
            
def apply_change(instr, lights_state):
    x0, x1, x2, x3, x4 = instr
    LMatrix = lights_state[x1:(x3+1),x2:(x4 +1)]
    
    if x0 == 0:
        LMatrix = LMatrix -1
        lights_state[lights_state<0] = 0
        
    if x0 == 1:
        LMatrix = LMatrix + 1

    if x0 == 2:
        LMatrix = LMatrix + 2
    
    lights_state[x1:(x3+1),x2:(x4 +1)] = LMatrix
    return lights_state
        

            
def change_lights(lights_state, instructions):
    for instr in instructions:
        light_state = apply_change(instr, lights_state)
    return light_state
    
    

def main(fname):
    start_lights_state = np.zeros([1000,1000], dtype = int)
    instructions = load_input(fname)
    

    final_state = change_lights(start_lights_state, instructions)
    print('Total brightness of lights turned on: {}'.format(np.sum(final_state)))
    processing_time = (datetime.datetime.now() - start_time).total_seconds() * 1000
    print("Time taken to get answer: {:.3f} ms".format(processing_time))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python [script.py] [input.txt]")
    else:
        main(sys.argv[1])
