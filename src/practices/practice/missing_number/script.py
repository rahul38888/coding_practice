
def missing_number(array, n):
    s = 0
    for val in array:
        s += val

    return int(n*(n+1)/2 - s)


def scan_input():
    n = int(input())

    nsstr = input()
    a = list(map(lambda x: int(x), nsstr.split()))

    return a, n


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, n = scan_input()
        print(missing_number(a, n))