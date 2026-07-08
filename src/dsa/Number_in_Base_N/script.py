
if __name__ == '__main__':
    b = int(input("Base: "))
    N = int(input("N: "))

    res = 0
    p = 1
    while N > 0:
        print(res, p, N)
        res += p*(N % b)
        p = p * 10
        N = N//b

    print(res)
