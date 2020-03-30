"""
$5. Longest Palindromic Substring
"""

class Solution:
    def longestPalindrome(self, s):
        N = len(s)
        idxs = list(range(N))
        length = 1
        while idxs:
            length +=  2
            new_idxs = []
            for c in idxs:
                if c - 1 >= 0 and c - 2 + length <= N-1 and \
                    s[c-1] == s[c-2+length]:
                    new_idxs.append(c-1)
            if new_idxs:
                idxs = new_idxs
                continue
            else:
                length -= 2
                break
        

        idxs2 = list(range(N))
        length2 = 0
        while idxs2:
            length2 +=  2
            new_idxs2 = []
            for c in idxs2:
                if c - 1 >= 0 and c - 2 + length2 <= N-1 and \
                    s[c-1] == s[c-2+length2]:
                    new_idxs2.append(c-1)
            if new_idxs2:
                idxs2 = new_idxs2
                continue
            else:
                length2 -= 2
                break
        print(idxs, idxs2)

        if length > length2:
            return s[idxs[0]:idxs[0] + length]
        else:
            return s[idxs2[0]: idxs2[0]+length2]
        

sol = Solution()
s = "abb"
print(sol.longestPalindrome(s))