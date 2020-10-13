

def LastTourDay(buses, D):
    for c in buses[::-1]:
        D = D - D % c
    return D

def main():
    T = int(input())
    for i in range(T):
        N, D = list(map(int, input().split(' ')))
        buses = list(map(int, input().split(' ')))
        first_day = LastTourDay(buses, D)
        print("Case #{}: {}".format(i+1, first_day))

if __name__ == "__main__":
    main()