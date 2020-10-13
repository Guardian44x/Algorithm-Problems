
import numpy as np

def PerfectSubarray(N, array):
    sums = np.array([], dtype=np.int32)
    res = 0
    for i in range(N):
        sums = np.append(sums, [0])
        sums += array[i]
        tmp_sums = sums[sums>=0]
        squas = np.sqrt(sums).astype(int)
        new_sums = squas * squas
        count = (tmp_sums == new_sums).sum()
        res += count
    return res


def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        array = list(map(int, input().split(' ')))
        res = PerfectSubarray(N, array)
        print("Case #{}: {}".format(i+1, res))


if __name__ == "__main__":
    main()
