'''961. N-Repeated Element in Size 2N Array
You are given an integer array nums with the following properties:

nums.length == 2 * n.
nums contains n + 1 unique values, n of which occur exactly once in the array.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.'''


def repeatedNTimes(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1


print(repeatedNTimes([1, 2, 3, 3]))  # Output: 3
print(repeatedNTimes([2, 1, 2, 5, 3, 2]))  # Output: 2


def repeatedNTimes_v2(nums):
    n = len(nums)//2
    nums.sort()
    if (nums[0] == nums[1]):
        return nums[n-1]
    return nums[n]


print(repeatedNTimes_v2([1, 2, 3, 3]))  # Output: 3
print(repeatedNTimes_v2([2, 1, 2, 5, 3, 2]))  # Output: 2


def repeatedNTimes_v3(nums):
    from collections import Counter
    count = Counter(nums)
    for num in count:
        if count[num] == len(nums)//2:
            return num
    return -1


print(repeatedNTimes_v3([1, 2, 3, 3]))  # Output: 3
print(repeatedNTimes_v3([2, 1, 2, 5, 3, 2]))  # Output: 2
