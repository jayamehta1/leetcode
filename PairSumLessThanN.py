def pairSumLessThanN(nums, target):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] < target:
                count += 1
    return count

print(pairSumLessThanN([1,2,3,4,5], 10))    #10
