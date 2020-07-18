import math
import numpy as np
test_scores=[80,90,67,89,99]

// Method 1
s1=[score ** .5 * 10 for score in test_scores]
print(sum(s1)/len(s1))

// Better
curved_test_scores=[math.sqrt(score) * 10 for score in test_scores]
print(np.mean(curved_test_scores))
