"""
$873. Length of Longest Fibonacci Subsequences.
"""
import collections

class Solution:
    def lenLongestFibSubseq(self, A):
        max_length = 0
        seq_dict = collections.defaultdict(list)
        for c in A:
            print(max_length)
            print(seq_dict)
            for subseq in seq_dict[0]:
                seq_dict[subseq[0]+c].append([c, 2])
                max_length = max(max_length, 2)
            for subseq in seq_dict[c]:
                seq_dict[subseq[0]+c].append([c, subseq[1]+1])
                max_length = max(max_length, subseq[1]+1)
            seq_dict[0].append([c, 1])
            max_length = max(max_length, 1)
        return max_length if max_length > 2 else 0
        
Sol = Solution()
A = [1, 3, 5]
print(Sol.lenLongestFibSubseq(A))