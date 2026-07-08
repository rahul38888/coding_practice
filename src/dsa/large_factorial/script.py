#
# Link: https://practice.geeksforgeeks.org/problems/large-factorial4721/1
#
# Observations:
#   - We should know that mod(n*m) = mod(mod(n)*mod(m))
#   - Now in calculation of mod(factorial(N)) we will also calculate
#       mod(factorial(N-1), mod(factorial(N-2), ..., mod(factorial(1).
#       So its a ood idea to cache these, to be reused by numbers less than N
#   - Lets calculate mod(factorial(N)) of largest #, others are in cache


def large_factorial(arr, length):
    max_val = arr[0]
    for j in range(1, length):
        max_val = max(max_val, arr[j])

    f_cache = [1, 1]
    for j in range(2, max_val + 1):
        f_cache.append((f_cache[j - 1] * j) % 1000000007)

    f_result = []
    for val in arr:
        f_result.append(f_cache[val])

    return f_result


def scan_input():
    n_value = int(input())
    ns_str = input()
    a_value = list(map(lambda x: int(x), ns_str.split()))
    return a_value, n_value


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, n = scan_input()
        print(" ".join(list(map(str, large_factorial(a, n)))))
