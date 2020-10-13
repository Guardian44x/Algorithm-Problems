

def RecordBreaker(N, visitors):
    count = 0
    prev_max = 0
    if N == 1:
        return 1
    for i in range(N):
        if i == 0:
            if visitors[i] > visitors[i+1]:
                count += 1
        elif i == N-1:
            if visitors[i] > prev_max:
                count += 1
        else:
            if visitors[i] > prev_max and visitors[i] > visitors[i+1]:
                count += 1
        prev_max = max(prev_max, visitors[i])
    return count

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        visitors = list(map(int, input().split(' ')))
        res = RecordBreaker(N, visitors)
        print("Case #{}: {}".format(i+1, res))


if __name__ == "__main__":
    main()