# https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/

# approach is to use (a*b)%m = (a%m*b%m)%m recursively by deviding n by 2 and solving for that

class Solution:
    def PowMod(self, x, n, m):
        if m == 1:
            return 0
        if n == 1:
            return x%m
        pm = self.PowMod(x, n//2, m)
        if n%2 == 0:
            return (pm*pm)%m
        else:
            return (((pm*pm)%m)*x)%m


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        x, n , m = input().split()
        x = int(x)
        n = int(n)
        m = int(m)
        ob = Solution()
        ans = ob.PowMod(x, n, m)
        print(ans)