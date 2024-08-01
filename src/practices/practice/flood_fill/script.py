# https://practice.geeksforgeeks.org/problems/flood-fill-algorithm1856/1#

# newColor can be same as well

# keep n*m memory to track visited pixels
# fill sr,sc
# check neighbor pixels
#   !visited
#   valid index
# recursivly call floodFill

class Solution:
    def floodFillRec(self, image, sr, sc, oldColor, newColor, visited):
        image[sr][sc] = newColor
        visited[sr][sc] = True
        if sr-1 >=0 and image[sr-1][sc] == oldColor and not visited[sr-1][sc]:
            self.floodFillRec(image,sr-1,sc,oldColor,newColor, visited)

        if sc-1 >=0 and image[sr][sc-1] == oldColor and not visited[sr][sc-1]:
            self.floodFillRec(image,sr,sc-1,oldColor,newColor, visited)

        if sr+1 <len(image) and image[sr+1][sc] == oldColor and not visited[sr+1][sc]:
            self.floodFillRec(image,sr+1,sc,oldColor,newColor, visited)

        if sc+1 < len(image[0]) and image[sr][sc+1] == oldColor and not visited[sr][sc+1]:
            self.floodFillRec(image,sr,sc+1,oldColor,newColor, visited)

    def floodFill(self, image, sr, sc, newColor):
        visited = [[False for i in range(m)] for i in range(n)]
        oldColor = image[sr][sc]
        self.floodFillRec(image, sr, sc, oldColor, newColor, visited)
        return image

import sys
sys.setrecursionlimit(10**7)
if __name__ == '__main__':

    T=int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        image = []
        for _ in range(n):
            image.append(list(map(int, input().split())))
        sr, sc, newColor = input().split()
        sr = int(sr); sc = int(sc); newColor = int(newColor);
        obj = Solution()
        ans = obj.floodFill(image, sr, sc, newColor)
        for _ in ans:
            for __ in _:
                print(__, end = " ")
            print()