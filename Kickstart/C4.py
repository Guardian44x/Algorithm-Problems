

def QuerySum(array, l, r):
    val = 0
    for i in range(l, r+1):
        val += (-1) ** (i-l) * array[i] * (i-l+1)
    return val

def QuerySum2(sums, l, r):
    val = sums[l]
    i = l + 2
    while i <= r:
        val += 2 * sums[i]
        i += 2
    if i < len(sums):
        val -= (i - l - 1) * sums[i]
    i = l + 1
    while i <= r:
        val -= 2 * sums[i]
        i += 2
    if i < len(sums):
        val += (i - l - 1) * sums[i]
    return val

def Candies(N, Q, array):
    res = 0
    sums = [0] * len(array)
    gauss = [0] * len(array)
    for i in range(N-1, -1, -1):
        if i == N-1:
            sums[i] = array[i]
            gauss[i] = array[i]
        else:
            sums[i] = array[i] - sums[i+1]
            gauss[i] = sums[i] - gauss[i+1]

    for i in range(Q):
        s, a, b = input().split(' ')
        a, b = int(a), int(b)
        if s == 'U':
            array[a-1] = b
            for i in range(a-1, -1, -1):
                sums[i] = array[i] - sums[i+1]
                gauss[i] = sums[i] - gauss[i+1]
        else:
            l, r = a-1, b-1
            print("-------")
            print(array)
            print(sums)
            print(gauss)
            val = gauss[l] - (-1) **(r-l+1) * gauss[r+1] - (-1) ** (r+1-l) * (r-l+1) * sums[r+1] \
                if r < N-1 else gauss[l]
            tmp = QuerySum(array, l, r)
            print(val, tmp)
            res += val
    return res

def main():
    T = int(input())
    for i in range(T):
        N, Q = list(map(int, input().split(' ')))
        array = list(map(int, input().split(' ')))
        res = Candies(N, Q, array)
        print("Case #{}: {}".format(i+1, res))

if __name__ == "__main__":
    main()
        