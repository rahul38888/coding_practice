def solution(buckets: str):
    # Implement your solution here
    bs = 0
    for p in buckets:
        if p == "B":
            bs += 1

    if bs == 0:
        return 0

    r = -1
    for d in range(0, 2):
        f = d
        l = d + 2 * (bs - 1)
        if l >= len(buckets):
            break

        may = 0
        for i in range(f, l + 1, 2):
            if buckets[i] == "B":
                may += 1

        r = max(r, may)
        l += 2
        while l < len(buckets):
            may += buckets[l] == "B"
            may -= buckets[f] == "B"
            r = max(r, may)
            f += 2
            l += 2

    return r if r < 0 else (bs-r)


if __name__ == '__main__':
    print(solution("BB.B.BBB..."))
