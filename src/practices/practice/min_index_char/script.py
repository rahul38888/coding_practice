# https://practice.geeksforgeeks.org/problems/minimum-indexed-character-1587115620/1#

# The approach is to hash pattern string character and iterate over the string
# for each character in string check if it exist in hash data-structure
# if yes, return that value
# If no, then after the loop return -1

class Solution:

    def minIndexChar(self, str, pat):
        pat_h = set()
        for p in pat:
            pat_h.add(p)

        for i in range(len(str)):
            if pat_h.__contains__(str[i]):
                return i

        return -1


import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        p = str(input())
        obj = Solution()
        ans = obj.minIndexChar(s, p)
        print(ans)
