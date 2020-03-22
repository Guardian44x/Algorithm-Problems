'''
$93. Restore IP Addresses
'''

class Solution:
    def restoreIpAddresses(self, s):
        l = len(s)
        if l > 12 or l < 4:
            return []
        res = []
        for i in range(1, l-2):
           for j in range(i+1, l-1):
               for k in range(j+1, l):  
                    tmp = [s[:i], s[i:j], s[j:k], s[k:]]
                    mark = True
                    for c in tmp:
                       if (len(c) > 1 and c[0] == '0') or int(c) > 255:
                            mark = False
                            break
                    if mark:
                        res.append(tmp)
        return [".".join(r) for r in res]

                    
                        
Sol = Solution()
s = "010010"
res = Sol.restoreIpAddresses(s)
print(res)