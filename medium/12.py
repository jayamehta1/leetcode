def merge(self, nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    while len(nums1) > m:
        nums1.pop()
    while len(nums2) > n:
        nums2.pop()
    nums1 += nums2
    nums1.sort()
    return nums1


merge_instance = merge(4, [-1, -1, 0, 0, 0, 0], 2, [-1, 0], 3)
print(merge_instance)  # Output: [-1,-1,-1,0,0,0]
