'''

3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest substring without duplicate characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        res = ""

        for char in s:
            if char not in res:
                res += char
            else:
                res = res[res.index(char) + 1:] + char
            
            maxlen = max(maxlen, len(res))  

        return maxlen 
               
