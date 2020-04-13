"""
$32. Longest Valid Parentheses
"""

class Solution:
    def longestValidParentheses(self, s):
        left = 0
        right = 0
        count = 0
        for c in s:
            if c == "(":
                left += 1
            else:
                right += 1
            if right > left:
                count = max(count, min(left, right))
                left, right = 0, 0
        left2, right2 = 0, 0
        j = 0
        t = left + right
        while j < t:
            if s[len(s)-1-j] == ')':
                right2 += 1
            else:
                left2 += 1
            if left2 > right2:
                left -= left2
                right -= right2
                count = max(count, min(left2, right2))
                left2, right2 = 0, 0
            j += 1
        return max(min(left, right), count) * 2
    
sol = Solution()
s = "()((()()((()"
print(sol.longestValidParentheses(s))