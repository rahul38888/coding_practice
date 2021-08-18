# https://practice.geeksforgeeks.org/problems/yes-xor-no2901/1#

# It is a trick question

# we know that if a^b=c, then a^c=b and b^c=a
# using this lets say a is from A and b is from b
# if c = a^b, there can be 2 cases, c is present in either or not
#   if c is present in A, then count would increase by 2 as c^b = a
#   if c is present in B, then again count would increase by 2 as c^a = b
#   if c is not present, then count would not increase
# Hence count will be always Even
class Solution:
    def yesXorNo(self, N, A, B):
        return "Yes"


if __name__ == '__main__':
    t = int (input ())
    for _ in range (t):
        N=int(input())
        A=list(map(int,input().split()))
        B=list(map(int,input().split()))

        ob = Solution()
        print(ob.yesXorNo(N,A,B))