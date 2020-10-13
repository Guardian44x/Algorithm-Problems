def FinalLocation(moves):
    MAX_POS = 1000000000
    i, l = 0, len(moves)
    n, s, w, e = 0, 0, 0, 0
    while i < l:
        if moves[i] >= '0' and moves[i] <= '9':
            t = 0
            j = i
            left, right = 0, 0
            mark = True
            start, end = i, i
            while j < l:
                if moves[j] >= '0' and moves[j] <= '9' and mark:
                    t = t * 10 + int(moves[j])
                elif moves[j] == '(':
                    left += 1
                    if mark:
                        mark = False
                        start = j + 1
                elif moves[j] == ')':
                    right += 1
                    if right == left:
                        end = j
                        break
                j += 1
            t = int(moves[i:start-1])
            tn, ts, tw, te = FinalLocation(moves[start:end])
            n, s, w, e = n+t*tn, s+t*ts, w+t*tw, e+t*te
            n, s, w, e = n % MAX_POS, s % MAX_POS, w % MAX_POS, e % MAX_POS
            i = j
        elif moves[i] in 'NSWE':
            if moves[i] == 'N':
                n += 1
            if moves[i] == 'S':
                s += 1
            if moves[i] == 'W':
                w += 1
            if moves[i] == 'E':
                e += 1
        i += 1
    return n, s, w, e


def main():
    T = int(input())
    for i in range(T):
        moves = input()
        n, s, w, e = FinalLocation(moves)
        locc, locr = 1, 1
        locc = (locc + e - w)
        locr = (locr + s - n)
        if locc <= 0:
            locc += 1000000000
        if locr <= 0:
            locr += 1000000000
        print("Case #{}: {} {}".format(i+1, locc, locr))

if __name__ == "__main__":
    main()