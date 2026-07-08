
def string_ignorance(s):
    tracker = set()
    result = ""
    for c in s:
        try:
            tracker.remove(c.lower())
        except KeyError:
            tracker.add(c.lower())
            result += c
    return result


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print(string_ignorance(s))