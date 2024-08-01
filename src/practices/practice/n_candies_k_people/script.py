# https://practice.geeksforgeeks.org/problems/distribute-n-candies/1#

# try to distribute as many candies as possible in a complete round
# when a candies required in a turn are more than left, then
#   find out the last person to get full turn candy
#   give remaining to next and return the array

class Solution:
    def apSum(self, a, d, n):
        return int(n*(2*a +(n-1)*d)/2)

    def distributeCandies(self, N, K):
        rem = N
        full_rounds = 0
        while rem > 0:
            this_round = self.apSum(1 + K*full_rounds,1,K)
            if this_round > rem:
                break
            rem -= this_round
            full_rounds += 1

        result = [0 for i in range(K)]
        for i in range(K):
            result[i] += self.apSum(i+1,K,full_rounds)
            extras = i+1 + full_rounds*K
            if extras > rem:
                result[i] += rem
                rem = 0
                continue
            result[i] += extras
            rem -= extras

        return result


if __name__ == '__main__':
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())

        ob = Solution()
        res = ob.distributeCandies(N,K)
        for i in res:
            print(i,end=" ")
        print()