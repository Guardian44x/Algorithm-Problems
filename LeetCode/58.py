"""
$58. Length of Last Word
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        count = 0
        a = len(s) - 1
        while a >= 0 and s[a] == ' ':
            a -= 1
        for b in range(a, -1, -1):
            c = s[b]
            if c != ' ':
                count += 1
            else:
                break
        return count