'''
$151. Reverse Words in a String
'''

class Solution:
    def reverseWords(self, s):
        s = s[::-1]
        prev = []        
        mask = ''
        res = ""
        if not s:
            return ''
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            if not ((s[i]>='a' and s[i]<='z') or (s[i]>='A' and s[i]<='Z')):
                mask = s[i]
                s = s[i+1:]
                break
        for c in s:
            if not prev and c==' ':
                continue
            if (c>='a' and c<='z') or (c>='A' and c<='Z'):
                prev.append(c)
            else:
                res += ''.join(prev[::-1]) + mask + c
                prev = []
                mask = ''
        res += ''.join(prev[::-1])
        res = res.strip()
        return res


sol = Solution()
s = "   hello world!      "
print(sol.reverseWords(s))