'''3349. Adjacent Increasing Subarrays Detection I
Given an array nums of n integers and an integer k, determine whether there exist two adjacent subarrays of length k such that both subarrays are strictly increasing. Specifically, check if there are two subarrays starting at indices a and b (a < b), where:
Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return true if it is possible to find two such subarrays, and false otherwise.

'''

def hasIncreasingSubarrays( nums, k):
   
    for i in range(len(nums) - 2*k + 1): 
        j = i + k
        new = nums[i:j] 
        new2 = nums[j:j+k]
        if (( new2 == sorted(new2)) and (new == sorted(new)) and len(set(new)) == k and len(set(new2)) == k ):
            return True
    return False   

print(hasIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1],  3))     
