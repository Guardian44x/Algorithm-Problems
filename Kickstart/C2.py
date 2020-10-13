
from collections import defaultdict

def StableWall(items, pres):
    res = []
    visited = [0] * len(items)
    idxs = dict(zip(items, list(range(len(items)))))

    def dfs(i):
        if visited[i] == 1:
            return False
        if visited[i] == 2:
            return True
        visited[i] = 1
        for pre in pres[items[i]]:
            if not dfs(idxs[pre]):
                return False
        
        visited[i] = 2
        res.append(i)
        return True
    
    for i, c in enumerate(items):
        if not dfs(i):
            return []
    return res

def main():
    T = int(input())
    for i in range(T):
        R, C = list(map(int, input().split(' ')))
        arrays = []
        for j in range(R):
            arrays.append(list(input()))
        pres = defaultdict(list)
        for j in range(R-1):
            for k in range(C):
                if arrays[j+1][k] != arrays[j][k]:
                    pres[arrays[j][k]].append(arrays[j+1][k])
        items = set()
        for j in range(R):
            items = items.union(set(arrays[j]))
        items = list(items)
        res = StableWall(items, pres)
        res = [items[i] for i in res]
        res = ''.join(res)
        if res == '':
            res = -1
        print("Case #{}: {}".format(i+1, res))

if __name__ == "__main__":
    main()