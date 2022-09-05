class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def isMatch(a, b):
            if len(a) != len(b):
                return False
            dict_a2b = {}
            dict_b2a = {}
            for i in range(len(a)):
                if not dict_a2b.has_key(a[i]):
                    dict_a2b[a[i]] = b[i]
                else:
                    if dict_a2b[a[i]] != b[i]:
                        return False
                if not dict_b2a.has_key(b[i]):
                    dict_b2a[b[i]] = a[i]
                else:
                    if dict_b2a[b[i]] != a[i]:
                        return False
            return True
        
        res = []
        for word in words:
            if isMatch(word, pattern):
                res.append(word)
        return res