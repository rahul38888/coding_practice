# https://practice.geeksforgeeks.org/problems/number-of-palindromic-paths-in-a-matrix0819/1#

# at each node recursively call itself and at bottom,left cornet determine it its a palindrome

class Solution:
    def palindrom(self ,string):
        i, j = 0 ,len(string)-1
        while i< j:
            if string[i] != string[j]:
                return False
            i+=1
            j-=1
        return True

    def rec(self, matrix, i, j, cur_str):
        print(i, j)
        if i == len(matrix[0])-1 and j == len(matrix)-1:
            return int(self.palindrom(cur_str + matrix[j][i]))

        count = 0
        if i + 1 < len(matrix[0]):
            count += self.rec(matrix, i + 1, j, cur_str + matrix[j][i])

        if j + 1 < len(matrix):
            count += self.rec(matrix, i, j + 1, cur_str + matrix[j][i])

        return count

    def countOfPalindromicPaths(self, matrix):
        print(matrix)
        return self.rec(matrix, 0, 0, "")


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n);
        m = int(m);
        matrix = []
        for _ in range(n):
            cur = input()
            temp = []
            for __ in cur:
                temp.append(__)
            matrix.append(temp)
        obj = Solution()
        ans = obj.countOfPalindromicPaths(matrix)
        print(ans)
