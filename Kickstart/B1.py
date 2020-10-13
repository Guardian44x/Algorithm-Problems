

def CountPeaks(N, mounts):
    if N <= 2:
        return 0
    count = 0
    for i in range(1, N-1):
        if mounts[i] > mounts[i-1] and \
            mounts[i] > mounts[i+1]:
            count += 1
    return count
    

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        mounts = list(map(int, input().split(' ')))
        count = CountPeaks(N, mounts)
        print("Case #{}: {}".format(i+1, count))

if __name__ == "__main__":
    main()        