# https://practice.geeksforgeeks.org/problems/sequence-of-sequence1155/1

# Recusive calls
# start with 1
# find a greatest 1,2,4,8...k_value (k_value<=m), count = 1
# revert back to last 2^p and increase it by 1 and try to find a string again
# if not possible return
# if there it count +=1, repeate step 3

class Solution:
    def noSeqRec(self, arr, m, n):
        if len(arr)==n and arr[len(arr)-1] <= m:
            return m-arr[len(arr)-1]+1
        elif len(arr)==n:
            return 0

        count = 0
        if len(arr) < n:
            count_local = self.noSeqRec(arr+[arr[len(arr)-1]*2], m, n)
            count+=count_local
            while count_local != 0:
                arr[len(arr)-1]+=1
                count_local = self.noSeqRec(arr+[arr[len(arr)-1]*2], m, n)
                count+=count_local
        return count

    def numberSequence(self, m, n):
        return self.noSeqRec([1], m, n)

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        arr = input().split()
        m = int(arr[0])
        n = int(arr[1])

        ob = Solution()
        print(ob.numberSequence(m, n))