from statistics import median


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        median_val = arr[(len(arr)-1) // 2]
        left_point = 0
        right_point = len(arr) - 1
        ans = []
        for _ in range(k):
            if (arr[right_point] - median_val) >= (median_val - arr[left_point]):
                ans.append(arr[right_point])
                right_point -= 1
            else:
                ans.append(arr[left_point])
                left_point += 1
        return ans