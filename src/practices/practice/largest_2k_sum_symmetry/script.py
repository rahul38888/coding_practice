# Link not found????

def largest_sum_symmetry(string: str):
    n = len(string)
    sums = [0 for _ in range(n+1)]
    for j in range(1, n + 1):
        sums[j] = sums[j - 1] + int(string[j - 1])

    result = 0
    for size in range(2, n+1, 2):
        for j in range(0, n - size + 1):
            if sums[j + int(size / 2)] - sums[j] == sums[j + size] - sums[j + int(size / 2)]:
                result = max(result, size)

    return result


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print(largest_sum_symmetry(s))
