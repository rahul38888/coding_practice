def max_sum_subarray(n, arr):
    p = -1
    pre_neg_sum = 0
    temp_sum = 0
    for i in range(n):
        temp_sum += arr[i]
        if pre_neg_sum > temp_sum:
            pre_neg_sum = temp_sum
            p = i

    s = n
    post_neg_sum = 0
    temp_sum = 0
    for i in range(n):
        temp_sum += arr[n - i - 1]
        if post_neg_sum > temp_sum:
            post_neg_sum = temp_sum
            s = n - i - 1
    print(p, s)
    if p >= s:
        max = arr[0]
        for i in range(n):
            if max < arr[i]:
                max = arr[i]
        return str(max)

    sum = 0
    for i in range(p + 1, s):
        sum += arr[i]

    return str(sum)


def scan_input():
    n = int(input())
    arrstr = input()
    arr = list(map(lambda astr: int(astr), arrstr.split()))

    return n, arr


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, arr = scan_input()
        print(max_sum_subarray(n, arr))
