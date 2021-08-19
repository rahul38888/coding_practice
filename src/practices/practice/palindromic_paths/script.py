# https://practice.geeksforgeeks.org/problems/number-of-palindromic-paths-in-a-matrix0819/1#

# at each node recursively call itself and at bottom,left cornet determine it its a palindrome

class Solution:

    def rec(self, matrix, it, jt, ib, jb, cache):
        if it > ib or jt > jb:
            cache[(it, jt, ib, jb)] = 0
            return 0

        if matrix[it][jt] != matrix[ib][jb]:
            cache[(it, jt, ib, jb)] = 0
            return 0


        if abs(it - ib) + abs(jt - jb) < 2:
            cache[(it, jt, ib, jb)] = 1
            return 1

        coun1, count2, count3, count4 = 0,0,0,0
        if cache.__contains__((it+1, jt, ib-1, jb)):
            count1 = cache[(it+1, jt, ib-1, jb)]
        else:
            count1 = self.rec(matrix, it+1, jt, ib-1, jb, cache)

        if cache.__contains__((it+1, jt, ib, jb-1)):
            count2 = cache[(it+1, jt, ib, jb-1)]
        else:
            count2 = self.rec(matrix, it+1, jt, ib, jb-1, cache)

        if cache.__contains__((it, jt+1, ib-1, jb)):
            count3 = cache[(it, jt+1, ib-1, jb)]
        else:
            count3 = self.rec(matrix, it, jt+1, ib-1, jb, cache)

        if cache.__contains__((it, jt+1, ib, jb-1)):
            count4 = cache[(it, jt+1, ib, jb-1)]
        else:
            count4 = self.rec(matrix, it, jt+1, ib, jb-1, cache)

        count = count1+count2+count3+count4

        cache[(it, jt, ib, jb)] = count

        return count

    def countOfPalindromicPaths(self, matrix):
        return self.rec(matrix, 0, 0, len(matrix)-1, len(matrix[0])-1, {})


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
