# https://practice.geeksforgeeks.org/problems/geek-collects-the-balls5515/1#

# Refined problem
# Find largest sum till switching points

# keep i,j index for a and b
# keep sum_a and sum_b
# iterate over both such that lower one is increased
# and larger one remains same till lower one >= larger one
# update sum_a/sum_b as integrating
# after reaching switching point (i==j) compare sum_a and sum_b and add max to total_sum
# exit when i and j both run its course
# return total sum

class Solution:
    def maxBalls(self, N, M, a, b):
        i, j = 0, 0
        sum_a, sum_b = 0,0
        total_sum = 0
        while i<N and j<M:
            if a[i] == b[j]:
                a_m = a[i]
                b_m = b[j]
                while i<N and a[i] == a_m:
                    sum_a += a[i]
                    i+=1
                while j<M and b[j] == b_m:
                    sum_b += b[j]
                    j+=1
                total_sum += max(sum_a,sum_b)
                sum_a = 0
                sum_b=0
            elif a[i] < b[j]:
                sum_a += a[i]
                i += 1
            else:
                sum_b += b[j]
                j += 1

        while i<N:
            sum_a += a[i]
            i+=1

        while j<M:
            sum_b += b[j]
            j+=1

        total_sum += max(sum_a,sum_b)

        return total_sum


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M = [int(x) for x in input().split()]
        a = input().split()
        b = input().split()
        for i in range(N):
            a[i] = int(a[i])
        for i in range(M):
            b[i] = int(b[i])

        ob = Solution()
        print(ob.maxBalls(N, M, a, b))