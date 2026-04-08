'''
53. Maximum Subarray

Medium
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.'''

def max_sub_array(nums):
    max_sum = nums[0]
    c_sum = nums[0]
    for i in range(1,len(nums)):
        c_sum = max(nums[i],(nums[i] + c_sum))
        max_sum = max(c_sum,max_sum)
    print(max_sum)    
    return max_sum    

nums = [-2,1,-3,4,-1,2,1,-5,4]
max_sub_array(nums)


# or

def max_sub(num):
    max_sum = float('-inf')
    s = 0
    for i in nums:
        s += i
        if s > max_sum:
            max_sum = s
        if s < 0 :
            s = 0
    print(max_sum)        
    return max_sum    

n = [-2,1,-3,4,-1,2,1,-5,4]
max_sub(n)   
