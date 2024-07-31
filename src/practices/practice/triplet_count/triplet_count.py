#User function Template for python3

class Solution:
	def countTriplet(self, arr, n):
		arr.sort()
		print(arr)
		count = 0
		s = n-1
		while s > 1:
			k, j = 0, s-1
			while k < j:
				if arr[k] + arr[j] > arr[s]:
					j -= 1
				elif arr[k] + arr[j] < arr[s]:
					k += 1
				else:
					j -= 1
					k += 1
					count += 1
			s -= 1
		return count


#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		arr = [int(x) for x in input().split()]

		ob = Solution()
		ans = ob.countTriplet(arr, n)
		print(ans)

# } Driver Code Ends