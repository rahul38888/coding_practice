# Link: https://practice.geeksforgeeks.org/problems/large-factorial4721/1


def large_factorial(a, n):
    maxVal = a[0]
    for i in range(1,n):
        if a[i] > maxVal:
            maxVal = a[i]

    f_cache = [1,1]
    for i in range(2, maxVal+1):
        f_cache.append((f_cache[i-1]*i)% 1000000007)

    f_result = []
    for val in a:
        f_result.append(f_cache[val])

    return f_result


def large_factorial_mine(a):
    f_array = []
    f_cache = [1, 1]
    f = 1
    for val in a:
        if val > len(f_cache)-1:
            for i in range(len(f_cache), val + 1):
                f *= i
                f_cache.append(f)
            f_array.append(f % 1000000007)
        else:
            f_array.append(f_cache[val] % 1000000007)

    return f_array


def scan_input():
    n = int(input())
    nsstr = input()
    a = list(map(lambda x: int(x), nsstr.split()))
    return a, n


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, n = scan_input()
        # print(" ".join(list(map(str, large_factorial_mine(a)))))
        print(" ".join(list(map(str, large_factorial(a,n)))))
