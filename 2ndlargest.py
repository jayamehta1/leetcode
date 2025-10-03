"""print the 2nd largest element in an array
If no 2nd largest element, then return -1"""


def getSecondLargest(arr):
    n = list(set(arr))
    n.sort()
    if len(n) == 1:
        return -1
    return n[-2]


print(getSecondLargest([2, 3, 6, 6, 5]))  # Output: 5
print(getSecondLargest([1, 2, 3, 4, 5]))
