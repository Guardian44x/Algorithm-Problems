

def RuleBreak(N, notes):
    if N <= 4:
        return 0
    symbols = [0]
    for i in range(1, N):
        if notes[i] > notes[i-1]:
            s = 1
        elif notes[i] < notes[i-1]:
            s = -1
        else:
            continue
        symbols.append(s)
    
    mark = 0
    count = 0
    res = 0
    M = len(symbols)
    if M <= 4:
        return 0

    for i in range(1, M):
        if symbols[i] != mark:
            mark = symbols[i]
            count = 1
        else:
            count += 1
            if count >= 4:
                count -= 4
                res += 1
    return res

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        notes = list(map(int, input().split(' ')))
        res = RuleBreak(N, notes)
        print("Case #{}: {}".format(i+1, res))

if __name__ == "__main__":
    main()