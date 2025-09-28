#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Write your code here
    return sum(ar)

if __name__ == "__main__":
    # Example test
    ar = [1, 2, 3, 4, 10, 11]
    print(simpleArraySum(ar))  # Output: 31

    # Simple Array Sum

# - Task: Return the sum of all integers in the array.
# - Approach: Use Python's built-in `sum()` function.
# - Complexity: O(n) time, O(1) extra space.
# - Variants: Could implement manually with a loop to show basics.