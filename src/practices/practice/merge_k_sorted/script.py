# https://practice.geeksforgeeks.org/problems/merge-k-sorted-arrays/1


class Solution:
    def max_index(self, arr, p, K):
        m_i = None
        for i in range(K):
            if m_i is None and p[i] < K:
                m_i = i
            if p[i] < K and arr[m_i][p[m_i]] > arr[i][p[i]]:
                m_i = i
        return m_i

    def merge_last_two(self, arr, K):
        a = []
        i, j = 0, 0
        x, y = len(arr)-2, len(arr)-1
        while i < len(arr[x]) and j < len(arr[y]):
            if arr[x][i] < arr[y][j]:
                a.append(arr[x][i])
                i += 1
            else:
                a.append(arr[y][j])
                j += 1
        while i<len(arr[x]):
            a.append(arr[x][i])
            i += 1
        while j<len(arr[y]):
            a.append(arr[y][j])
            j += 1
        arr.pop()
        arr.pop()
        arr.append(a)

    def mergeKArrays(self, arr, K):
        while len(arr) > 1:
            self.merge_last_two(arr, K)
        return arr[0]


# code here
# return merged list

# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        numbers = [[0 for _ in range(n)] for _ in range(n)]
        line = input().strip().split()
        for i in range(n):
            for j in range(n):
                numbers[i][j] = int(line[i * n + j])
        ob = Solution();
        merged_list = ob.mergeKArrays(numbers, n)
        for i in merged_list:
            print(i, end=' ')
        print()
# } Driver Code Ends
