'''2716. Minimize String Length
Given a string s, you have two types of operation:

Choose an index i in the string, and let c be the character in position i. Delete the closest occurrence of c to the left of i (if exists).
Choose an index i in the string, and let c be the character in position i. Delete the closest occurrence of c to the right of i (if exists).
Your task is to minimize the length of s by performing the above operations zero or more times.

Return an integer denoting the length of the minimized string.'''


def minimizedStringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for ch in s:
            if ch not in stack:
                stack.append(ch)
        return len(stack) 
