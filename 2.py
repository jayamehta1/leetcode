'''Q2. How Many Numbers Are Smaller Than the Current Number
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.'''


def smallerNumbersThanCurrent(nums):
    new = []
    for i in range(len(nums)):
        k = 0
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                k += 1
        new.append(k)
    return new


print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))  # Output: [4,0,1,1,3]
print(smallerNumbersThanCurrent([6, 5, 4, 8]))  # Output: [2,1,0,3]
