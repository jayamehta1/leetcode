'''189. Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.'''


def right_rotate(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums


print(right_rotate([1, 2, 3, 4, 5, 6, 7], 3))  # Output: [5, 6, 7, 1, 2, 3, 4]
print(right_rotate([-1, -100, 3, 99], 2))  # Output: [3, 99, -1, -100]
