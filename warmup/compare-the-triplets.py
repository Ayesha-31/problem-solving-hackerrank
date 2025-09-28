#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    i = 0
    ans =[0,0]
    while(i < len(a)):
        if(a[i]>b[i]):
            ans[0] += 1
        elif a[i]<b[i]:
            ans[1] += 1
        i += 1
    return ans
        


if __name__ == "__main__":
    # Example test
    a = [5, 6, 7]
    b = [3, 6, 10]
    print(compareTriplets(a, b))  # Output: [1, 1]



# Compare the Triplets

# - Compare corresponding elements of two lists.
# - Increment Alice’s score if `a[i] > b[i]`.
# - Increment Bob’s score if `b[i] > a[i]`.
# - Complexity: O(n) time, O(1) space.