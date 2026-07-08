# https://www.geeksforgeeks.org/batch/gts-1/track/gts-mathematics/problem/multiply-two-strings

# approch is to use the methord of multiplication tought in primary classes
#        123
#       x 11
#       _____
#        123
#       123x
#       _____
#       1353

class Solution:
    def multiplyStrings(self,s1,s2):
        sign = 1
        m_result = 0
        if s1[0] == "-":
            sign *= -1
            s1 = s1[1:]
        if s2[0] == "-":
            sign *= -1
            s2 = s2[1:]
        
        ord0 = ord("0")
        powi = 1
        for i in range(len(s2)):
            m_local = 0
            r = 0
            powj = 1
            for j in range(len(s1)):
                m = (ord(s2[len(s2) - i - 1])-ord0)*(ord(s1[len(s1) - j - 1])-ord0)
                mr = m + r
                m_local += powj*(mr%10)
                r = mr//10
                powj *= 10
            m_result += powi*(m_local + r*powj)
            powi *= 10
        return m_result*sign


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        s1, s2 = input().split()
        ob = Solution()
        ans = ob.multiplyStrings(s1,s2)
        print(ans)