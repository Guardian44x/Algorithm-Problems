"""
$5298. Verbal Arithmetic Puzzle
"""

from itertools import permutations

class Solution:
    def isSolvable(self, words, result):

        def word2num(word, digit_map):
            num = 0
            for s in word:
                num = num * 10 + digit_map[s]
            return num

        digits = list(range(0, 10))
        letters = set()
        for word in words:
            letters = letters | set(word)
        letters = letters | set(result)

        letters = list(letters)
        if len(letters) > 10:
            return False

        all_digits = permutations(digits, len(letters))       

        for pos in all_digits:
            digit_map = dict(zip(letters, pos))
            numbers = [] 
            for word in words:
                num = word2num(word, digit_map)
                numbers.append(num)
            res = word2num(result, digit_map)
            if sum(numbers) == res:
                return True
        else:
            return False    
        
sol = Solution()
words = ["LEET","CODE"]
result = "POINT"
print(sol.isSolvable(words, result))