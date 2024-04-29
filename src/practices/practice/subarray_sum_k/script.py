#User function Template for python3

# 10 2 -2 -20 10
# -10

class Solution:
    def findSubArraySum(self, Arr, N, k):
        sums = []
        count = 0
        for i in range(N):
            if i is 0:
                sums[i]=Arr[i]
            else:
                sums[i] = sums[i-1]+Arr[i]
            if sum[i] == k:
                count+=1
        for i in range(1, n):
            sum[i]-=Arr[i-1]


# code here

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.findSubArraySum(Arr, N, k))
# } Driver Code Ends