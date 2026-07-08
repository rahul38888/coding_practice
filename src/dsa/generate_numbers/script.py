# https://www.geeksforgeeks.org/batch/gts-1/track/gts-mathematics/problem/generating-numbers

# For given N, we hav to find N numbers that satisfy the following equation
#     2^i * 3^i * 5^k_value * 7^l       Where i,j,k_value,l are non negative integers

# Approach: 
#     The approch is to start with number 1 as curent number.
#     We will then loop until we have N numbers.
#         We will multiply the curent number with 2, 3, 5, and 7 and store it in a min-heap if its not already there.
#         In each next iteration we will update current number by popping a new number from the heap


import heapq

class Solution:
    def generateNumbers(self, N):
        if N < 1:
            return []
        
        factors = [2, 3, 5, 7]
        result = []
        
        set_array = {1}
        heap = [1]
        heapq.heapify(heap)
        
        while len(result) < N:
            cur_val = heapq.heappop(heap)
            result.append(cur_val)
            
            for f in factors:
                new_val = cur_val * f
                if new_val not in set_array:
                    set_array.add(new_val)
                    heapq.heappush(heap, new_val)
        
        return result

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        ob = Solution()
        res = ob.generateNumbers(N)
        for i in res:
            print(i,end=" ")
        print()