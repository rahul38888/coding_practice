
class Solution:
    '''

        Problem: https://www.geeksforgeeks.org/batch/gts-1/track/gts-mathematics/problem/nth-natural-number

        Observations
        ------------
        Given 2 arrays we can observe following
            - There could be an index in arr1 after which element should be transfered to arr2
            - Similarly could be an index in arr2 after which element should be transfered to arr1
        
        Solution
        --------
        Our aim is to partition the arrays such that no element of arr1 is larger than any element of arr2

        - To find that keep 2 pointers, 1 per array pointing to starting index innitially (i, j). Also keep another pointer to end of arr1 (k)
        - In a loop move arr1 pointer to next if its value is less than value pointed by arr2 pointer.
        - If not, swap arr2 pointing value with value pointed by k. This is the point we were looking for. Move arr2 pointer to next and k backward
        - Do this untill i and k cross each other of j runs its course
        - After that sort both arrays and we are done

    '''
    def merge(self,arr1: list,arr2: list,n,m):
        i, j = 0, 0
        k = n-1
        while j < m and i <= k:
            if arr1[i] < arr2[j]:
                i += 1
            else:
                arr1[k], arr2[j] = arr2[j], arr1[k]
                j += 1
                k -= 1

        arr1.sort()
        arr2.sort()
    

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob=Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1,end=" ")
        print(*arr2)