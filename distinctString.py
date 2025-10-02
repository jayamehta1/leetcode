"""2053. Kth Distinct String in an Array
A distinct string is a string that is present only once in an array.
Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".
Note that the strings are considered in the order in which they appear in the array."""

from collections import Counter


def kthDistinct(arr, k):
    count = Counter(arr)
    for ch in arr:
        if count[ch] == 1:
            k -= 1
            if k == 0:
                return ch
    return ""


print(kthDistinct(["d", "b", "c", "b", "c", "a"], 2))  # Output: "a"
print(kthDistinct(["aaa", "aa", "a"], 1))  # Output: "
