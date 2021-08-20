# https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string1956/1#


class Solution:
    def longestPalindrome(self, S):
        i = 0
        string = ""
        for i in range(len(S)):
            x,y=i-1,i+1
            temp = S[i]
            while x >= 0 and y < len(S) and S[x] == S[y]:
                temp = S[x] + temp + S[y]
                x -= 1
                y += 1

            if len(temp) > len(string):
                string = temp

            x,y=i,i+1
            temp = ""
            while x >= 0 and y < len(S) and S[x] == S[y]:
                temp = S[x] + temp + S[y]
                x -= 1
                y += 1

            if len(temp) > len(string):
                string = temp

        return string


if __name__=='__main__':
    t=int(input())
    for _ in range(t):

        S = input().strip()
        ob=Solution()
        print(ob.longestPalindrome(S))