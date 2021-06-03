import re
import sys
import datetime
start_time = datetime.datetime.now()
from collections import namedtuple
from functools import reduce

Ingredient = namedtuple('Ingredient', ['capacity', 'durability', 'flavor', 'texture'])


def parse_input(line):
    ingredient, *metrics = re.match(r'(.*): capacity (.*), durability (.*), flavor (.*), texture (.*), calories (.*)', line).groups()
    return ingredient, metrics



def main():
    ingredients = {}
    with open(sys.argv[1], 'r') as f:
        for line in f:
            ingredient, metrics = parse_input(line)
            capacity, durability, flavor, texture, _ = [int(m) for m in metrics]
            ingredients[ingredient] = Ingredient(capacity, durability, flavor, texture)
    print(ingredients)
    
    max_score = 0
    proportions = [0,0,0,0]
    totals = [0,0,0,0]
    
    best_proportions = {}
    total_vol = 100
    
    
    for first_prop in range(total_vol+1):
        proportions[0] = first_prop
        
        for sec_prop in range(total_vol+1 - first_prop ):
            proportions[1] = sec_prop
            
            for third_prop in range(total_vol+1 - first_prop - sec_prop):
                proportions[2] = third_prop
                
                fourth_prop = total_vol - first_prop - sec_prop - third_prop
                proportions[3] = fourth_prop
    
                for p, ing in zip(proportions, ingredients.keys()):
                            totals[0] = totals[0] + (p*ingredients[ing].capacity)
                            totals[1] = totals[1] + (p*ingredients[ing].durability)
                            totals[2] = totals[2] + (p*ingredients[ing].flavor)
                            totals[3] = totals[3] + (p*ingredients[ing].texture)
                totals = [max(0, t) for t in totals]

                score = reduce(lambda x, y: x*y, totals)
                totals = [0,0,0,0]

                max_score = max(score, max_score)
                if score == max_score:
                    for i, ing in enumerate(ingredients.keys()):
                        best_proportions[ing] = proportions[i]
        
    print(max_score)
    print(best_proportions)
    
    processing_time = (datetime.datetime.now() - start_time).total_seconds()
    print("Time taken to get answer: {:.3f} seconds".format(processing_time))

    
if __name__ == "__main__":
    main()
