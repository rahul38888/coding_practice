# https://practice.geeksforgeeks.org/problems/count-of-sum-of-consecutives3741/1#

# O(n) : Approach is to start adding values from 1, unto a point when either sum  is N or greater than that
# if sum == N, increase result_count
# if sum > N, remove the smallest element
# if sum < N add next element
# iterate over these steps until largest number become N

# Another approach is by realising that to be the case for N
# N should be equal to a + (a+1) + ..... (a+L) or L+1 consecutive numbers
# which can be solved to L(L+1)/2 + a(L+1)
# starting with L = 1, try to find a
# if a is integer, result_count+=1
# run this on loop while increasing L, until a < 1

class Solution:
    def getCount_OrderN(self, N):
        sm = 1
        lg = -1
        result_count = 0
        csum = 0
        while lg < N:
            if csum <= N:
                if csum == N:
                    result_count+=1
                lg+=1
                csum += lg
            else:
                csum -= sm
                sm+=1

        return result_count
    
    def getCount(self, N):
        L = 2
        a = None
        result_count = 0
        while True:
            a = N/L - (L-1)/2
            if a < 1:
                break

            if a == int(a):
                result_count+=1

            L+=1

        return result_count


if __name__ == '__main__':
    t = int (input ())
    for _ in range (t):
        N=int(input())

        ob = Solution()
        print(N, ob.getCount2(N), ob.getCount(N))