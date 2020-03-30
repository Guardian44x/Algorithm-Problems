"""
$214. Shortest Palindrome
"""

class Solution:
    def shortestPalindrome(self, s):
        if not s or len(s) == 1:
            return s
        j = 0
        for i in reversed(range(len(s))):
            if s[i] == s[j]:
                j += 1
        print(j)
        print(s[::-1][:len(s)-j], s[:j-len(s)], s[j-len(s):])
        return s[::-1][:len(s)-j] + self.shortestPalindrome(s[:j-len(s)]) + s[j-len(s):]

sol = Solution()
s = "aacecaaa"
# s = "abcd"
# s = "aabba"
print(sol.shortestPalindrome(s))