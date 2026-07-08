# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1

# Approach is to count the occurrences and then build the arr again

class Solution:
    def sort012(self, arr, n):
        counts = {0: 0, 1: 0, 2: 0}
        for a in arr:
            counts[a] += 1

        i = 0
        for key in range(3):
            for j in range(counts[key]):
                arr[i] = key
                i += 1

        return arr


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sort012(arr, n)
        for i in arr:
            print(i, end=' ')
        print()
