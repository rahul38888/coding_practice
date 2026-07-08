class Solution:
    def merge(self, arr, s, m , e):
        i = s
        j = m+1
        sorted_sub_arr = []
        while i <= m and j <= e:
            if arr[i] <= arr[j]:
                sorted_sub_arr.append(arr[i])
                i += 1
            else:
                sorted_sub_arr.append(arr[j])
                j += 1
        while i <= m:
            sorted_sub_arr.append(arr[i])
            i += 1
        while j <= e:
            sorted_sub_arr.append(arr[j])
            j += 1

        arr[s:e+1] = sorted_sub_arr
        return arr

    def sort(self, arr, s, e):
        if s >= e:
            return arr
        m = int((s + e) / 2)
        arr = self.sort(arr, s, m)
        arr = self.sort(arr, m+1, e)
        arr = self.merge(arr, s, m, e)
        return arr

    def insertValue(self, arr, val):
        s, e = 0, len(arr)-1
        m = int((s+e)/2)
        if arr[e] < val:
            arr.append(val)
            return arr
        if arr[s] > val:
            arr.insert(0,val)
            return arr
        while s < e:
            if arr[m] >= val:
                e = m
            else:
                s = m+1
            m = int((s+e)/2)
        arr.insert(m, val)
        return arr

    def minCost(self, arr, n):
        if n == 1:
            return 0
        arr = self.sort(arr,0,n-1)
        result = 0
        print(arr)
        while len(arr) > 2:
            result += arr[0]+arr[1]
            arr = self.insertValue(arr[2:], arr[0]+arr[1])
            print(result)
            print(arr)

        return result + sum(arr)


import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minCost(a, n))
