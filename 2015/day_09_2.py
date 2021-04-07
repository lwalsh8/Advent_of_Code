import sys
import re
import itertools
from collections import defaultdict
import numpy as np
import datetime
start_time = datetime.datetime.now()

# Taken from https://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/
class Graph():
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight
        


def load_input(fname):
    with open(fname, "r") as f:
        file = f.read().strip()
        flights = file.split("\n")
        for flight in flights:
            yield re.split(' to | = ', flight)

            
    
def main(input_file):
    graph = Graph()
    flights = load_input(input_file)
    for flight in flights:
        graph.add_edge(*flight[:2], int(flight[2]))
            
    all_combos = list(itertools.permutations(graph.edges))
    total_dist_for_combos = {}
    for i, combo in enumerate(all_combos):
        dist_for_combo = []
        for l in range(len(graph.edges) - 1):
            first_dest, second_dest = combo[l: l+2]
            dist = graph.weights[(first_dest, second_dest)]
            dist_for_combo.append(dist)
        total_dist_for_combos[i] = np.sum(dist_for_combo)
    
    smallest_index = min(total_dist_for_combos, key=total_dist_for_combos.get)
    longest_index = max(total_dist_for_combos, key=total_dist_for_combos.get)
    print('Path with shortest distance: {} - {}'.format(all_combos[smallest_index], total_dist_for_combos[smallest_index]))
    print('Path with longest distance: {} - {}'.format(all_combos[longest_index], total_dist_for_combos[longest_index]))
    processing_time = (datetime.datetime.now() - start_time).total_seconds() * 1000
    print("Time taken to get answer: {:.3f} ms".format(processing_time))
    
    
    
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("USAGE: python [script.py] [input.txt]")
    else:
        main(sys.argv[1])