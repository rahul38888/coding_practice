# https://practice.geeksforgeeks.org/problems/circular-tour-1587115620/1
# 4 6 7 4
# 6 5 3 5
# -2 1 4 -1

class Solution:
    def tour(self, lis, n):
        sum = 0
        j = 0
        for i in range(len(lis)):
            pair = lis[i]
            sum += pair[0]-pair[1]
            if sum < 0:
                sum = 0
                j = i+1

        if j>=n:
            return -1
        else:
            return j

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = []
        for i in range(1, 2 * n, 2):
            lis.append([arr[i - 1], arr[i]])
        print(Solution().tour(lis, n))
