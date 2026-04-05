"""
283. Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array."""


def moveZeroes(nums):
    s = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[s] = nums[i]
            s += 1
    for j in range(s, len(nums)):
        nums[j] = 0
    return nums


print(moveZeroes([0, 1, 0, 3, 12]))  # Output: [1,3,12,0,0]
print(moveZeroes([0]))  # Output: [0]
print(moveZeroes([1, 0, 2, 0, 3, 0, 4]))
