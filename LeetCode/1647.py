class Solution:
    def minDeletions(self, s):
        letter_cnt = [0] * 26
        for c in s:
            idx = ord(c) - ord('a')
            letter_cnt[idx] += 1
        letter_dict = dict()
        for i, c in enumerate(letter_cnt):
            if c == 0:
                continue
            if not letter_dict.has_key(c):
                letter_dict[c] = 0
            letter_dict[c] += 1
        keys = list(letter_dict.keys())
        keys.sort()
        print("keys", keys)
        left = 1
        stack = []
        res = 0
        for c in keys:
            stack.extend([_ for _ in range(left, c)])
            print(stack)
            left = c + 1
            while letter_dict[c] > 1:
                if len(stack) == 0:
                    stack.append(0)
                res = res + c - stack[-1]
                stack.pop(-1)
                letter_dict[c] -= 1
        return res

class Solution:
    def minDeletions(self, s: str) -> int:
        # Get the frequency of each character sorted in reverse order
        frequencies = sorted(Counter(s).values(), reverse=True)
        
        total_deletions = 0
        next_unused_freq = len(s)
        for freq in frequencies:
            # It is impossible for the frequency to be higher
            next_unused_freq = min(next_unused_freq, freq)
            total_deletions += freq - next_unused_freq

            # We cannot have another character with this frequency,
            # so decrement next_unused_freq
            if next_unused_freq > 0:
                next_unused_freq -= 1

        return total_deletions

Sol = Solution()
s = "bbcebab"
from collections import Counter
print(Counter(s).values())
print(s)
res = Sol.minDeletions(s)
print(res)