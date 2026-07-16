
# 844. Backspace String Compare

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        f1 = []
        f2 =[]
        for ch in s:
            if ch == '#':
                if f1:
                    f1.pop()
            else:
                f1.append(ch)
        for ch in t:
            if ch == '#':
                if f2:
                    f2.pop()
            else:
                f2.append(ch)        
             


        if f1 == f2:
            return True
        else:
            return False   
