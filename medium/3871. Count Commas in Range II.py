"""
3871. Count Commas in Range II
You are given an integer n.
Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.
In standard formatting:

A comma is inserted after every three digits from the right.
Numbers with fewer than 4 digits contain no commas."""

def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 1000
        ans = 0
        # if n < 1000:
        #     return 0
        while num <= n:
            ans += n - num + 1
            num *= 1000
        return ans 
