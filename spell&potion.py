"""2300. Successful Pairs of Spells and Potions
You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.
You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.
Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.
"""

"""Hint 1 : Notice that if a spell and potion pair is successful, then the spell and all stronger potions will be successful too.
Hint 2 : Thus, for each spell, we need to find the potion with the least strength that will form a successful pair.
Hint 3 : We can efficiently do this by sorting the potions based on strength and using binary search."""
from math import ceil
import bisect


def successfulPairs(spells, potions, success):
    potions.sort()
    result = []
    for spell in spells:
        min_po = ceil(success / spell)
        index = bisect.bisect_left(potions, min_po)
        result.append(len(potions) - index)
    return result


# Example usage:
spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
print(successfulPairs(spells, potions, success))  # Output: [4, 0, 3]
