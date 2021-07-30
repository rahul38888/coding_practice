# https://www.geeksforgeeks.org/rearrange-characters-string-no-two-adjacent/
# https://practice.geeksforgeeks.org/contest/coding-try-outs-amazon/problems


class Item:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    

def non_repeating_arrange(str):
    char_count = []
    chars = []
    for i in range(len(str)):
        char_count[ord(str[i])-ord('a')] += 1

    i, j = 0, 0
    result = ""
    while i < 26 and j < 26:
        if i == j:
            if char_count[i] > 1:
                result += chr(i+ord('a'))
                char_count[i] -= 1
                j += 1
            elif char_count[i] > 0:
                result += chr(i+ord('a'))
                char_count[i] = 0
                i += 1
                j = i
            else:
                i += 1
                j = i
        else:
            if char_count[j] > 0:
                result += chr(j+ord('a'))
                char_count[j] -= 1
                j = i
            else:
                j += 1

    return int(i > 25)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input()
        print(non_repeating_arrange(str))