'''
$522. Longest Uncommon Subsequence II
'''

class Solution:
    def findLUSlength(self, strs):
        str_list = [[] for i in range(11)]
        for str in strs:
            str_list[len(str)].append(str)

        def a_sub_b(a, b):
            i, j = 0, 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            if i == len(a):
                return True

        subsequences = []
        for i in range(10, -1, -1):
            single_str = []
            duplicate_str = []
            for str in str_list[i]:
                for i in range(len(duplicate_str)):
                    if a_sub_b(str, duplicate_str[i]):
                        if str in single_str:
                            single_str.remove(str)
                        break
                else:
                    single_str.append(str)
                    duplicate_str.append(str)
            for p in single_str:
                for q in subsequences:
                    if a_sub_b(p, q):
                        break
                else:
                    return len(p)
            subsequences.extend(single_str + duplicate_str)
        else:
            return -1
            

                

sol = Solution()
strs = ["j","j","viez","ogk","ogk","lfn","ypmhwx","ypmhwx","m","m","ak","ivivzoncju","ivivzoncju","wmybi","wmybi","dyzfjg","dyzfjg"]
print(sol.findLUSlength((strs)))