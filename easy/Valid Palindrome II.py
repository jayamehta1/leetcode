'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
'''

def validPalindrome(s):
    def check(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        
    i, j = 0, len(s) - 1
        
    while i < j:
        if s[i] != s[j]:
            return check(i, j - 1) or check(i + 1, j)
        i += 1
        j -= 1
        
    return True

s = "aba"
validPalindrome(s)