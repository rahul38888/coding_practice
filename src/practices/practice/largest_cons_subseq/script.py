# https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1#

#  approach is to keep a hash of the arr
#  iterate over arr and if it is the first element of the subsequence, get size of the subsequence
#  return max count

import atexit
import io
import sys


class Solution:
    def findLongestConseqSubseq(self, arr, N):
        hashed = {val for val in arr}

        count = 0
        for i in range(N):
            if not hashed.__contains__(arr[i] - 1):
                val = arr[i]
                temp = 0
                while hashed.__contains__(val):
                    temp += 1
                    val += 1
                count = max(count, temp)

        return count


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        print(Solution().findLongestConseqSubseq(a, n))
