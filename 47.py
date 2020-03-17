"""
$47. Permutations II
"""

def Permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return 
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
                print(i, cycles)
                print(indices)
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                print(i, j, cycles)
                print(indices)
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

nums = range(5)
r = 3
for c in Permutations(nums, r):
    print(c)