def ReachProb(W, H, L, U, R, D):
    if L <= 1 and R >= 1 and U <= 1 and D >= 1:
        return 0
    if L <= W and R >= W and U <= H and D >= H:
        return 0
    if (L == 1 and R == W) or (U == 1 and D == H):
        return 0
    probs = [[0] * H for _ in range(W)]
    probs[0][0] = 1
    step = 1
    while step < W + H:
        step += 1
        for s in range(min(step, W-1)):
            r, c = s + 1, step - s + 1
            if probs[r][c] > 0:
                if r == W-1 and c == H-1:
                    break
                elif r == W-1:
                    probs[r][c+1] += probs[r][c]
                    probs[r][c] = 0
                elif c == H-1:
                    probs[r+1][c] += probs[r][c]
                    probs[r][c] = 0
                else:
                    probs[r+1][c] += probs[r][c] * 0.5
                    probs[r][c+1] += probs[r][c] * 0.5
                    probs[r][c] = 0
    return probs[W-1][H-1]


def main():
    T = int(input())
    for i in range(T):
        W, H, L, U, R, D = list(map(int, input().split(' ')))
        res = ReachProb(W, H, L, U, R, D)
        print("Case #{}: {}".format(i+1, res))


if __name__ == "__main__":
    main()