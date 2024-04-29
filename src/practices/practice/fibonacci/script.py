import time


def recursive(n):
    if n <= 1:
        return n
    return recursive(n - 1) + recursive(n - 2)


def memorization(n, memory):
    if n <= 1:
        memory[n] = n
    if memory[n] is None:
        memory[n] = memorization(n - 1, memory) + memorization(n - 2, memory)
    return memory[n]


def tabulation(n):
    f = [0] * (n + 1)
    f[1] = 1

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


if __name__ == '__main__':
    n = int(input())

    result = None

    start = time.time()
    result = recursive(n)
    end = time.time()
    print("Recursive output: " + str(result) + ", time taken: " + str(end - start))

    memory = [None] * (n + 1)
    start = time.time()
    result = memorization(n, memory)
    end = time.time()
    print("Memorization output: " + str(result) + ", time taken: " + str(end - start))

    start = time.time()
    result = tabulation(n)
    end = time.time()
    print("Tabulation output: " + str(result) + ", time taken: " + str(end - start))
