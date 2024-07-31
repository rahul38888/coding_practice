
def find_subset_sliding(n, s, arr):
    start, end = 0, 0
    sum = arr[end]

    while start < n and end < n:
        if sum == s:
            return str(start + 1) + " " + str(end + 1)
        elif sum > s:
            sum -= arr[start]
            start += 1
            continue
        end += 1
        if end >= n:
            break
        sum += arr[end]

    return "-1"


def scan_input():
    nsstr = input()
    ns = list(map(lambda x: int(x), nsstr.split()))
    n, s = ns[0], ns[1]

    arrstr = input()
    arr = list(map(lambda astr: int(astr), arrstr.split()))

    return n, s, arr


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, s, arr = scan_input()
        print(find_subset_sliding(n, s, arr))
