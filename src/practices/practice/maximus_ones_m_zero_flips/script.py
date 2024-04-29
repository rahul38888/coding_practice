# https://practice.geeksforgeeks.org/problems/maximize-number-of-1s0905/1#

# m is maximum of number zeroes allowed
# to flip, n is size of array

# Real problem: find the largest subarray with zeros <= m

#   0s <= m (j++, size++, calculate zeros)
#   0s > m  (i++,size--)


def findZeroes(arr, n, m):
    i, j = 0, 0
    zero_count = 0
    max_size = 0
    size = 0
    while j < n:
        zero_count += arr[j] == 0
        size = j - i + 1
        if zero_count <= m:
            max_size = max(max_size, size)
        else:
            zero_count -= arr[i] == 0
            i += 1
        j += 1

    return max_size


if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        m = int(input())
        ans = findZeroes(arr, n, m)
        print(ans)
        tc = tc - 1
