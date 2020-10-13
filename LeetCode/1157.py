"""
$1157. Online Majority Element In Subarray
"""

class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        arr_copy = self.arr.copy()
        leftb, rightb = left, right
        mid = (left + right) // 2
        idx = self.partition(arr_copy, left, right)
        while idx != mid:
            if idx > mid:
                right = idx
            else:
                left = idx
            idx = self.partition((arr_copy, left, right))
        return arr_copy[mid] if arr_copy[mid] == arr_copy[leftb] or \
                                arr_copy[mid] == arr_copy[rightb] else -1

    def partition(self, arr: List[int], left: int, right: int) -> int:
        i = left - 1
        pivot = arr[right]

        for j in range(left, right):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i+1], arr[right] = arr[right], arr[i+1]
        return i+1