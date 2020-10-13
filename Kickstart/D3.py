
def BeautyOfTreeRe(N, A, B, nodes):
    nodes = [-1] + nodes
    Achilds = [0] * N
    Bchilds = [0] * N
    for i in range(N-1, 0, -1):
        p = i
        for j in range(A):
            p = nodes[p] - 1
            if p < 0:
                break
        if p >= 0:
            Achilds[p] += 1 + Achilds[i]
        p = i
        for j in range(B):
            p = nodes[p] - 1
            if p < 0:
                break
        if p >= 0:
            Bchilds[p] += 1 + Bchilds[i]
    res = 0 
    for i in range(N):
        res += (Achilds[i] + 1) * N + (Bchilds[i] + 1) * N - \
                (Achilds[i] + 1) * (Bchilds[i] + 1)
    return res / N ** 2

def BeautyOfTree(N, A, B, nodes):
    childs = [[] for i in range(N)]
    for i, c in enumerate(nodes):
        childs[c-1].append(i+1)
    Achilds = [-1] * N
    Bchilds = [-1] * N

    def CountChilds(A, kids, t):
        if kids[t] >= 0:
            return kids[t]
        elif len(childs[t]) == 0:
            kids[t] = 0
            return kids[t]
        else:
            now_stage = [t]
            for _ in range(A):
                next_stage = []
                for c in now_stage:
                    if len(childs[c]) == 0:
                        continue
                    else:
                        next_stage += childs[c]
                now_stage = next_stage
            if len(now_stage) == 0:
                kids[t] = 0
            else:
                val = 0
                for c in now_stage:
                    val += CountChilds(A, kids, c) + 1
                kids[t] = val
            return kids[t]
        
    res = 0 
    for i in range(N):
        res += (Achilds[i] + 1) * N + (Bchilds[i] + 1) * N - \
                (Achilds[i] + 1) * (Bchilds[i] + 1)
    return res / N ** 2


def main():
    T = int(input())
    for i in range(T):
        N, A, B = list(map(int, input().split(' ')))
        nodes = list(map(int, input().split(' ')))
        res = BeautyOfTreeRe(N, A, B, nodes)
        print("Case #{}: {}".format(i+1, res))

if __name__ == "__main__":
    main()