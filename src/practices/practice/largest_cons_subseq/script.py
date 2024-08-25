# https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1#
#
# Observations:
#   - Note that there can be multiple subsets of different size which are consecutive in themselves
#   - If smallest element of such subset is X, then X-1 would not exist in the array
#   - If largest element of such subset is Y, then Y+1 would also not exist in the array
#   - Using second point we can identify the smallest element of such subsets
#   - After that we can keep finding the next element and keep count
#   - We will stop if the next consecutive element is not present in the array
#   - We can report the max size we found
#

import atexit
import io
import sys


class Solution:
    def findLongestConseqSubseq(self, arr, n_value):
        hashed = {val for val in arr}

        count = 0
        for i in range(n_value):
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
