"""
$1146. Snapshot Array
"""

class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[[-1, 0]] for i in range(length)]
        self.snap_id = -1

    def set(self, index: int, val: int) -> None:
        if self.arr[index][-1][0] == self.snap_id:
            self.arr[index][-1][1] = val
        else:
            self.arr[index].append([self.snap_id, val])
        # print(self.arr)

    def snap(self) -> int:
        self.snap_id += 1 
        return self.snap_id

    def get(self, index: int, snap_id: int):
        val = 0
        if self.arr[index][-1][0] < snap_id:
            return self.arr[index][-1][1]
        left, right = 0, len(self.arr[index])
        while left < right:
            mid = (left + right) // 2
            # print(index, snap_id, left, right, mid)
            if self.arr[index][mid][0] >= snap_id:
                right = mid
            else:
                left = mid
            if left + 1 == right: 
                break
        return self.arr[index][left][1]