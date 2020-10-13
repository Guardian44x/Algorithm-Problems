

def Countdown(N, K, array):
    # array_str = ' '.join(list(map(str, array)))
    key_str = ' '.join(list(map(str, list(range(K, 0, -1)))))
    array_str = ' '.join(array[:K])
    res = 0
    if array_str == key_str:
        res += 1
    for i in range(1, N-K+1):
        l = len(array[i-1])
        array_str = array_str[l+1:] + ' ' + array[i+K-1]
        if array_str == key_str:
            res += 1
    return res


def main():
    T = int(input())
    for i in range(T):
        N, K = list(map(int, input().split(' ')))
        array = input().split(' ')  
        res = Countdown(N, K, array)
        print("Case #{}: {}".format(i+1, res))


if __name__ == "__main__":
    main()