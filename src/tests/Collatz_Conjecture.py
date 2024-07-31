
def lengthN(n, cache):
    count = 1
    while n > 1:
        if len(cache) >= n:
            count = count + cache[n-1]
            break
        if n % 2:
            n = 3*n + 1
        else:
            n /= 2
        count += 1
    cache[int(n)-1] = count
    return count, cache


if __name__ == '__main__':
    n = int(input())
    lengths = []
    cache = [1]
    for i in range(1, n+1):
        count, cache = lengthN(i, cache)
        lengths.append(count)

    print(lengths)