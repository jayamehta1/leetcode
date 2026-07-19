'''

1209. Remove All Adjacent Duplicates in String II

You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.'''


class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        f1 = []
        for ch in s:
            if f1 and f1[-1][0] == ch:
                f1[-1][1] += 1
                if f1[-1][1] == k:
                    f1.pop()
            else:
                f1.append([ch, 1])

        ans = []
        for cr, cnt in f1:
            ans.append(cr * cnt)

        return "".join(ans)
