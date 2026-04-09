'''56. Merge Intervals
Medium

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].'''

def merge( intervals):
        res = []
        intervals.sort(key=lambda x: x[0])
        pre = intervals[0]
        for i in intervals[1:] :
            if i[0] <= pre[1] :
                pre[1] = max(i[1], pre[1])
            else : 
                res.append(pre) 
                pre = i 
        res.append(pre) 
        print(res)       
        return res      


n = [[1,3],[2,6],[8,10],[15,18]]
merge(n)