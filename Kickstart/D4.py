

def Query(N, diffs, S, K):
    status = [-1] * N
    left, right = diffs[S-1], diffs[S]
    leftp, rightp = S-1, S+1
    t = S
    while K > 1:
        K -= 1
        # print(K, leftp, rightp)
        if left < right:
            t = leftp
            leftp = leftp - 1
            left = diffs[leftp]
        else:
            t = rightp
            rightp += 1
            right = diffs[rightp-1]
    return t


def main():
    T = int(input())
    for i in range(T):
        N, Q = list(map(int, input().split(' ')))
        diffs = list(map(int, input().split(' ')))
        diffs = [float("inf")] + diffs + [float("inf")]
        res = []
        for j in range(Q):
            S, K = list(map(int, input().split(' ')))
            pos = Query(N, diffs, S, K)
            res.append(str(pos))
        res = ' '.join(res)
        print("Case #{}: {}".format(i+1, res))

if __name__ == "__main__":
    main()
        