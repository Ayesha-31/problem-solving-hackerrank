"""
Problem: A Very Big Sum
Source: HackerRank
Category: Warmup
Difficulty: Easy
Pattern: Summation of large integers
"""

def aVeryBigSum(ar):
    result = 0
    for num in ar:
        result += num
    return result


if __name__ == "__main__":
    # Example test
    ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
    print(aVeryBigSum(ar))  # Output: 5000000015
