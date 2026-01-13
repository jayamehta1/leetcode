'''Q3. Find All Numbers Disappeared in an Array
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.'''


def findDisappearedNumbers(nums):
    s = set(nums)
    return [i for i in range(1, len(nums)+1)if i not in s]


print(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))  # Output: [5,6]
print(findDisappearedNumbers([1, 1]))  # Output: [2]
