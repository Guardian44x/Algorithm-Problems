class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        if len(s) == 2 and s == '()':
            return 1
        
        left_idx = 0
        right_idx = 0
        length = len(s)
        left_cnt = 0
        right_cnt = 0
        score = 0
        for i in range(length):
            if s[i] == '(':
                left_cnt += 1
            else:
                right_cnt += 1
            if left_cnt == right_cnt:
                right_idx = i
                if right_idx - 1 < left_idx + 1:
                    score += 1
                else:
                    # print(left_idx+1, right_idx-1, s[left_idx+1:right_idx])
                    score += 2 * self.scoreOfParentheses(s[left_idx+1:right_idx])
                left_idx = right_idx + 1
        return score

Sol = Solution()
s = "(()(()))"
ans = Sol.scoreOfParentheses(s)
print(ans)
