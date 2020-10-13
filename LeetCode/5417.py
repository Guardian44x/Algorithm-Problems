"""
$ Maximum Number of Vowels in a Substring of Given Length
""" 

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        res = count
        i = k
        while i < len(s):
            pre = s[i-k]
            if pre in vowels:
                count -= 1
            now = s[i]
            if now in vowels:
                count += 1
            res = max(count, res)
            i += 1
        return res