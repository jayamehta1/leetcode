'''125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.'''

def validpal(s):
    clean = "".join(char for char in s if char.isalnum()).lower()
    if clean == clean[::-1]:
        return True
    return False

s = "A man, a plan, a canal: Panama"
validpal(s)

