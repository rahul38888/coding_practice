
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

        AB_count = (N - N%lcm)//lcm
        return result - lcm*AB_count*(1+AB_count)//2

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N,A,B = map(int,input().strip().split())
        ob = Solution()
        ans = ob.calculateSum(N, A, B)
        print(ans)