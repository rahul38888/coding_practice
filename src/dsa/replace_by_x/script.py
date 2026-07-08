
def replace_by_x(s, p):
    i = 0
    result = ""
    last_was_X = False
    while i < len(s):
        if s[i:i+len(p)] == p and not(last_was_X):
            result += "X"
            last_was_X = True
            i += len(p)
            continue
        elif s[i:i+len(p)] == p and last_was_X:
            i += len(p)
            continue
        else:
            last_was_X = False
            result += s[i]
        i += 1

    return result


def scan_input():
    s = input()
    p = input()
    return s, p


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s, p = scan_input()
        print(replace_by_x(s, p))