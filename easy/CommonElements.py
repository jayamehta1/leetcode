'''2956. Find Common Elements Between Two Arrays
Easy

You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. Calculate the following values:

answer1 : the number of indices i such that nums1[i] exists in nums2.
answer2 : the number of indices i such that nums2[i] exists in nums1.
Return [answer1,answer2].

'''


def commonletter(nums1,nums2):
    count1 = 0
    set1 = set(nums1)
    set2 = set(nums2)

    for x in nums1:
        if x in set2:
            count1 += 1
    count2 = sum(1 for x in nums2 if x in set1)    
    return [count1, count2]   
a = [2, 3, 2]
b= [1, 2]
commonletter(a,b)