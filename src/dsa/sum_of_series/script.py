# https://www.geeksforgeeks.org/batch/gts-1/track/gts-mathematics/problem/sum-of-the-series--141634
# 
# Appcoach is as following
# For N and a number A
# All numbers divisible by A and less than N are
#       A, 2A, 3A, ... A*N//2
#  i.e. A (1, 2, 3, .... N//2)
# Sum(A) = A(N//2)(N//2 + 1)/2
#
# So for another number B
# Sum of numbers devisibel by B amd less than N is
# Sum(B) = B(N//2)(N//2 + 1)/2
# Now if we consuder result = Sum(A) + Sum(B), we will see that there are repeatition as well
# Example for N=12, A=2 and B=4, 4 will repeate twice same as 8 and 12
# So we need to remove these number by using LCM(A, B) = L as following
# Result = Sum(A) + Sum(B) - Sum(L)
# Where sum can be derived using above formula

# TIme complexity will only come from finding the LCM, which is kwone to be O(min(A,B))


class Solution:
    def calculateSum(self, N, A, B):

        A_count = N//A
        B_count = N//B

        result = A*A_count*(1+A_count)//2 + B*B_count*(1+B_count)//2

        a = min(A,B)
        b = max(A,B)

        while a > 0:
            b, a= a, b%a

        lcm = (A*B)//b

        AB_count = N//lcm
        return result - lcm*AB_count*(1+AB_count)//2

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N,A,B = map(int,input().strip().split())
        ob = Solution()
        ans = ob.calculateSum(N, A, B)
        print(ans)