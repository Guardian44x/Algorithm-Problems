
def SearchMax(arr, passed, i, money):
    if i >= len(arr):
        return 0
    if passed[i][money] > 0:
        return passed[i][money]
    if money <= 0:
        passed[i][money] = 0
        return 0
    if money < arr[i]:
        passed[i][money] = SearchMax(arr, passed, i+1, money)
    else:
        passed[i][money] = max(SearchMax(arr, passed, i+1, money), SearchMax(arr, passed, i+1, money-arr[i])+1)
    return passed[i][money]  

def main():
    T = int(input())
    for i in range(T):
        N, B = list(map(int, input().split(' ')))
        costs = list(map(int, input().split(' ')))
        passed = [[-1] * (B+1) for i in range(N)]
        res = SearchMax(costs, passed, 0, B)
        print("Case #{}: {}".format(i+1, res))
        
if __name__ == "__main__":
    main()