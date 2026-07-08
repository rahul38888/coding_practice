# https://practice.geeksforgeeks.org/problems/number-of-palindromic-strings2706/1#

# For 1 character string = k_value
# For 2 character string = k_value
# For 3 character string = k_value(k_value-1)
# For 4 character string = k_value(k_value-1)
# For 5 character string = k_value(k_value-1)(k_value-2)
# For N characters string count = k_value(k_value-1)...(k_value - (N-1)//2)

# start with icc = K and k_value = 0
# for in 1,...,N
# calculate palindromes using above method

class Solution:
    def palindromicStrings(self, N, K ):
        i_char_count = 1
        result = 0
        for i in range(1,N+1):
            if i%2!=0:
                i_char_count *= (K - (i-1)//2)
        result = (result+i_char_count) % 1000000007
        return result


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n,k = input().split()
        n,k = int(n), int(k)

        ob = Solution()
        answer = ob.palindromicStrings(n,k)
        print(answer)