# https://practice.geeksforgeeks.org/problems/subset-sums2234/1#

# sort the array
# recursive approach
# start with index i = 0
# it gives either 0 or arr[i], pass i+1, [0,arr[i]], arr recursively
# in each recursive call create array by appending array with arr[i] to array and appending

class Solution:
    def merge(self, arr1, arr2):
        i, j = 0, 0
        arr = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                arr.append(arr1[i])
                i += 1
            else:
                arr.append(arr2[j])
                j += 1

        while i < len(arr1):
            arr.append(arr1[i])
            i += 1

        while j < len(arr2):
            arr.append(arr2[j])
            j += 1

        return arr

    def sort(self, arr):
        if len(arr) <= 1:
            return arr
        m = len(arr)//2
        arr1 = self.sort(arr[:m])
        arr2 = self.sort(arr[m:])
        arr = self.merge(arr1,arr2)
        return arr

    def subsetSumsRec(self, arr, N, i, sum_arr):
        if i >= N:
            return sum_arr
        sum_arr += [x+arr[i] for x in sum_arr]
        self.subsetSumsRec(arr, N, i+1, sum_arr)
        return sum_arr

        def subsetSums(self, arr, N):
            sum_arr = [0]
            return self.sort(self.subsetSumsRec(arr, N, 0, sum_arr))

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        for x in ans:
            print(x,end=" ")
        print("")
