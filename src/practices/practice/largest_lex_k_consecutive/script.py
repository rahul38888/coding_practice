# https://www.geeksforgeeks.org/largest-lexicographical-string-with-at-most-k-consecutive-elements/

def lex_largest_k_consecutive(str, k):
    char_count = [0]*26
    for i in range(len(str)):
        char_count[ord(str[i])-ord('a')] += 1

    i, j = 25, 25
    result = ""
    while i >= 0 and j >= 0:
        if j == i:
            if char_count[i] > k:
                result += chr(i+ord('a'))*k
                char_count[i] -= k
                j -= 1
            elif char_count[i] > 0:
                result += chr(i+ord('a'))*char_count[i]
                char_count[i] = 0
                i -= 1
                j = i
            else:
                i -= 1
                j = i
        else:
            if char_count[j] > k:
                result += chr(j++ord('a'))*k
                char_count[j] -= k
                j = i
            elif char_count[j] > 0:
                result += chr(j+ord('a'))*char_count[j]
                char_count[j] = 0
                j = i
            else:
                j -= 1

    return result


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input()
        k = int(input())
        print(lex_largest_k_consecutive(str, k))