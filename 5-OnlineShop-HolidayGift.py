"""
Say your online gift store has one million users that each listed a gift on a wish list. You have the prices for each of these gifts 
stored in gift_costs.txt. For the holidays, you're going to give each customer their wish list gift for free if it is under 25 dollars. 
Now, you want to calculate the total cost of all gifts under 25 dollars to see how much you'd spend on free gifts. Here's one way you could've done it.
"""

import time
import numpy as np

with open('gift_costs.txt') as f:
    gift_costs = f.read().split('\n')
    
gift_costs = np.array(gift_costs).astype(int)  # convert string to int

# Method 1
start = time.time()
total_price = 0
for cost in gift_costs:
    if cost < 25:
        total_price += cost * 1.08  # add cost after tax
print(total_price)
print('Duration: {} seconds'.format(time.time() - start))


# Better method
start = time.time()
total_price =  (gift_costs[gift_costs < 25]).sum() * 1.08
print(total_price)
print('Duration: {} seconds'.format(time.time() - start))
