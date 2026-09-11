"""3483. Unique 3-Digit Even Numbers
You are given an array of digits called digits. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.

Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.
Example 1:

Input: digits = [1,2,3,4]

Output: 12

Explanation: The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 cannot be formed because there is only 1 copy of the digit 2."""

def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        ans = []
        for num in range(100,1000,2):
            s = str(num)
            valid = True
            # if all(s.count(d) <= digits.count(int(d)) for d in set(s)):
            for d in set(s):
                if s.count(d) > digits.count(int(d)):
                    valid = False
                    break
            if valid:    
                    ans.append(num)
        return len(ans)  
