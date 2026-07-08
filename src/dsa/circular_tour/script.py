# https://practice.geeksforgeeks.org/problems/circular-tour-1587115620/1
# 4 6 7 4
# 6 5 3 5
# -2 1 4 -1

class Solution:
    def tour(self, lis, n):
        k = 0
        sum_from_k = 0
        sum_pre_k = 0
        for i in range(len(lis)):
            p = lis[i][0]
            d = lis[i][1]
            sum_from_k += (p - d)
            if sum_from_k < 0:
                sum_pre_k += sum_from_k 
                sum_from_k = 0
                k = i + 1
            
        if sum_pre_k + sum_from_k >= 0:
            return k
        else:
            return -1 

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = []
        for i in range(1, 2 * n, 2):
            lis.append([arr[i - 1], arr[i]])
        print(Solution().tour(lis, n))
