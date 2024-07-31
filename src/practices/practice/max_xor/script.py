
class Solution:
    def max_xor(self, arr, n):
        pass


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int,input().split()))
        ob = Solution();
        print(ob.max_xor(arr,n))