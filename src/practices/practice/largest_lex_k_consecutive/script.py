# https://www.geeksforgeeks.org/largest-lexicographical-string-with-at-most-k-consecutive-elements/
#
# Observations:
#   - We can keep only k characters together
#   - We have to introduce different character just smaller than the current
#       after k characters in case the count of the character is more than k
#   -


def lex_largest_k_consecutive(string: str, k_value):
    char_count = [0] * 26
    for n in range(len(string)):
        char_count[ord(string[n]) - ord('a')] += 1

    m, j = 25, 25
    result = ""
    while m >= 0 and j >= 0:
        if j == m:
            if char_count[m] > k_value:
                result += chr(m + ord('a')) * k_value
                char_count[m] -= k_value
                j -= 1
            elif char_count[m] > 0:
                result += chr(m + ord('a')) * char_count[m]
                char_count[m] = 0
                m -= 1
                j = m
            else:
                m -= 1
                j = m
        else:
            if char_count[j] > 0:
                result += chr(j + ord('a'))
                char_count[j] -= 1
                j = m
            else:
                j -= 1

    return result


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        k = int(input())
        print(lex_largest_k_consecutive(s, k))
