
class Solution:
    '''
        Problem: https://www.geeksforgeeks.org/batch/gts-1/track/gts-mathematics/problem/nth-natural-number

        Observations
        ------------
        Talking in general terms, we can see that if we remove all numbers containing a perticular digit, 
        we would end up with a series of numbers representing a number system made of only nine symbols (in our case 0 to 8)

        So we can see this problem as finding Nth number in a number system written by only nine symbols

        Solution
        --------
        Our aim is to caculate one digit at a time, starting from 0th digit.
        - We will keep a multiplier `p` to keep track of what digit we are caculating. It will have value of 1 in begining
        - We will keep another variable named `res` which will store the value upto a digit in each iteration, and final value after loop exit.
        - The loop will be run untill N is greater than 0, as we will be updating the N by removing its 0th digit in each iteration (based on the new number sytem). This is done by updating it with `N//9`
        - The current 0th digit can be extracted from N by modulating it with 9 uisng `N % 9`
        - `res` will be updating with `p * (N % 9)`, which is how we add a digit if you think it in terms of 10 Base number system
        - `p` will be multiplied with 10, which means we will be handling with next digit of `N`
        - After we come out from the loop we `res` contain the number we seek.
    '''
    def findNth(self,N):
        res = 0
        p = 1
        while N > 0:
            res += p*(N % 9)
            p = p * 10
            N = N//9

        return res

t=int(input())
for i in range(0,t):
    n=int(input())
    obj=Solution()
    s=obj.findNth(n)
    print(s)
