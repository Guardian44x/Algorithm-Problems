class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        res = []
        l = len(text)
        for i in range(l-1):
            for j in range(2, l-i+1, 2):
                if text[i:i+j//2] == text[i+j//2: i+j]:
                    print(i, j, text[i:i+j])
                    res.append(text[i:i+j])
        
        return len(set(res))
        
sol = Solution()
text = "leetcodeleetcode"
res = sol.distinctEchoSubstrings(text)
print(res)