
'''

2465. Number of Distinct Averages

You are given a 0-indexed integer array nums of even length.

As long as nums is not empty, you must repetitively:

Find the minimum number in nums and remove it.
Find the maximum number in nums and remove it.
Calculate the average of the two removed numbers.
The average of two numbers a and b is (a + b) / 2.

For example, the average of 2 and 3 is (2 + 3) / 2 = 2.5.
Return the number of distinct averages calculated using the above process.

Note that when there is a tie for a minimum or maximum number, any can be removed.'''


def distinctavg(nums):
    nums.sort()
    avg = set()
    n = len(nums)
    left, right = 0, n-1
    while left < right:
        avg.add((nums[left] + nums[right])/2)
        left += 1
        right -= 1
    return len(avg)


nums = [4, 1, 4, 0, 3, 5]  # 2
print(distinctavg(nums))
