"""
$72. Edit Distance
"""

class Solution:
    def minDistance(self, word1, word2):

        vals = [[-1] * (len(word2) + 1) for i in range(len(word1)+1)]

        def miniDistance(word1, word2):
            if word1 == word2:
                vals[len(word1)][len(word2)] = 0
                return 0
            if len(word1) == 0 or len(word2) == 0:
                vals[len(word1)][len(word2)] = max(len(word2), len(word1))
                return vals[len(word1)][len(word2)]
            if vals[len(word1)][len(word2)] > -1:
                return vals[len(word1)][len(word2)]

            vals[len(word1)][len(word2)] =  min(miniDistance(word1[1:], word2)+1, \
                                            miniDistance(word1, word2[1:])+1, \
                                            miniDistance(word1[1:], word2[1:]) + (not (word1[0] == word2[0])))
            
            return vals[len(word1)][len(word2)]
    
        miniDistance(word1, word2)
        return vals[-1][-1]


sol = Solution()
word1 = "horse"
word2 = "ros"
res = sol.minDistance(word1, word2)
print(res)