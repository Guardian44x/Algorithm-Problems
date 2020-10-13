"""
$915. Partition Array into Disjoint Intervals
"""

class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        left_max_list = [0] * len(A)
        right_min_list = [0] * len(A)
        left_max_list[0] = A[0]
        right_min_list[-1] = A[-1]
        for i in range(1, len(A)):
            left_max_list[i] = max(left_max_list[i-1], A[i])
        for i in range(len(A)-2, 0, -1):
            right_min_list[i] = min(right_min_list[i+1], A[i])
        for i in range(0, len(A)-1):
            if left_max_list[i] <= right_min_list[i+1]:
                return i+1
        return len(A)