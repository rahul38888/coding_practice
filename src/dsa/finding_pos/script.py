# https://practice.geeksforgeeks.org/problems/finding-position2223/1

def finding_pos(n):
    pos = 1
    while pos*2 <= n:
        pos *= 2
    return pos


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(finding_pos(n))