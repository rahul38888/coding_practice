# https://practice.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1#

# 0 : 000
# 1 : 001
# 2 : 010
# 3 : 011
# 4 : 100
# 5 : 101
# 6 : 110
# 7 : 111

# Approach is to use following properties:
# 1st bit follows the pattern 0,1
# 2nd bit follows the pattern 0,0,1,1
# 3rd bit follows the pattern 0,0,0,0,1,1,1,1
# iterate over bit and keep adding the sums of that ro bit using

class Solution:
    def countSetBits(self, n):
        count = 0
        group_size = 1
        num = n
        while num:
            comp_groups = (n + 1) // group_size
            rem = ((n + 1) % group_size)
            extra = rem if comp_groups % 2 else 0
            count += (comp_groups // 2) * group_size + extra

            group_size *= 2
            num = num // 2

        return count


if __name__ == "__main__":
    for _ in range(int(input())):
        ob = Solution()
        print(ob.countSetBits(int(input())))
