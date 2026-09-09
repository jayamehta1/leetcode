""" 3870. Count Commas in Range
You are given an integer n.
Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.
In standard formatting:
A comma is inserted after every three digits from the right.
Numbers with fewer than 4 digits contain no commas.
 

Example 1:

Input: n = 1002

Output: 3

Explanation:

The numbers "1,000", "1,001", and "1,002" each contain one comma, giving a total of 3."""


def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1000:
            return 0
        else :
            return (n - 1000) + 1    
