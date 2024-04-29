# https://practice.geeksforgeeks.org/problems/chocolate-station2951/1

def chocolate_station(n, a, p):
    balance = 0
    bought = 0
    for i in range(len(a)):
        val = 0
        if i is 0:
            val = -a[i]
        else:
            val = a[i-1] - a[i]

        if val > 0:
            balance += val
        elif balance >= -val:
            balance += val
        else:
            bought += -val - balance
            balance = 0

    return p*bought


def scan_input():
    n = int(input())
    sstr = input()
    a = list(map(lambda x: int(x), sstr.split()))
    p = int(input())
    return n, a, p


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, a, p = scan_input()
        print(chocolate_station(n,a,p))
