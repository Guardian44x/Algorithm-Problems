
"""
Check If a String Contains All Binary Codes of Size K
"""

class Solution:
    def hasAllCodes(self, s, k):
        binary_codes = set()
        l = len(s)
        if l < (2**k + k-1):
            return False
        for i in range(k, l+1):
            if s[i-k:i] in binary_codes:
                continue
            else:
                binary_codes.add(s[i-k:i])
        # print(binary_codes)
        return len(binary_codes) == 2**k