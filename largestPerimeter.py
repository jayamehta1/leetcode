def largestPerimeter(nums):
    nums.sort()
    for i in range(len(nums) - 1, 1, -1):
        if nums[i] < nums[i - 1] + nums[i - 2]:
            return nums[i] + nums[i - 1] + nums[i - 2]
    return 0


# Example usage:
print(largestPerimeter([2, 1, 2]))  # Output: 5
print(largestPerimeter([1, 2, 1]))  # Output: 0
print(largestPerimeter([3, 2, 3, 4]))  # Output:s


"""976. Largest Perimeter Triangle
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0."""
