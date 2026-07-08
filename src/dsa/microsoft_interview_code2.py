def calculate(S: str) -> int:
    length = len(S)

    if length > 100:
        return 0

    count = [0] * 100
    for i in range(length - 1):
        num = int(S[i: i + 2])
        count[num] = 1

    return sum(count)


if __name__ == '__main__':
    cache = [False] * 100
    st = "0"
    while len(st) < 100:
        new_found = False
        for i in range(10):
            new = st[-1] + str(i)
            new_str = int(new)
            if not cache[new_str]:
                st += new[-1]
                new_found = True
                cache[new_str] = True
                continue
        if not new_found:
            for j in range(len(cache)):
                if not cache[j]:
                    st += str(j)[-1]

    result = st[:100]
    print(result, len(result))
    print(calculate(result))
