
def SearchMaxBeauty(stacks, passed, i, K, P):
    if i >= len(stacks):
        return 0
    if passed[i][P] > 0:
        return passed[i][P]
    if P == 0:
        passed[i][P] = 0
        return 0
    max_val = SearchMaxBeauty(stacks, passed, i+1, K, P)
    for j in range(min(P, K)):
        max_val = max(max_val, stacks[i][j] + SearchMaxBeauty(stacks, passed, i+1, K, P-j-1))
    passed[i][P] = max_val
    return max_val

T = int(input())
for t in range(T):
    N, K, P = list(map(int, input().split(' ')))
    stacks = []
    for i in range(N):
        plates = list(map(int, input().split(' ')))
        pre_sum = 0
        for i in range(len(plates)):
            pre_sum += plates[i]
            plates[i] = pre_sum
        stacks.append(plates)
    passed = [[-1] * (P+1) for i in range(N)]
    res = SearchMaxBeauty(stacks, passed, 0, K, P)
    print("Case #{}: {}".format(t+1, res))