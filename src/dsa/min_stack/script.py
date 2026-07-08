# https://practice.geeksforgeeks.org/problems/get-minimum-element-from-stack/1#

# Approach is to store an array containing stack elements and minEle in separate variable
# For push
#   if minEle is None add element to s and assign minEle - element
#   if minEle <= element add element to s
#   else add 2*x-minEle in s and assign minEle the element value
# For pop
#   if s is empty return -1
#   if last element of s is >= minEle return and remove last element of s
#   else return minEle assign minEle = 2*minEle - last value of S, and also remove last element
#   assign minEle None if size of s is 0
# For getMin
#   return minEle if not None else -1

class Stack:
    def __init__(self):
        self.s = []
        self.minEle = None

    def push(self, x):
        if self.minEle is None:
            self.minEle = x
            self.s.append(x)
        else:
            if self.minEle <= x:
                self.s.append(x)
            else:
                self.s.append(2 * x - self.minEle)
                self.minEle = x

    def pop(self):
        val = -1
        if len(self.s) != 0:
            if self.s[-1] >= self.minEle:
                val = self.s[-1]
            else:
                val = self.minEle
                self.minEle = 2 * self.minEle - self.s[-1]

            del self.s[-1]
            if len(self.s) == 0:
                self.minEle = None

        return val

    def getMin(self):
        return self.minEle if self.minEle is not None else -1


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        q = int(input())

        arr = [int(x) for x in input().split()]

        stk = Stack()

        qi = 0
        qn = 1
        while qn <= q:
            qt = arr[qi]

            if qt == 1:
                stk.push(arr[qi + 1])
                qi += 2
            elif qt == 2:
                print(stk.pop(), end=' ')
                qi += 1
            else:
                print(stk.getMin(), end=' ')
                qi += 1
            qn += 1
        print()
