

def largest_sum_symmetry(str):
    n = len(str)
    sums = [0]*(n+1)
    for i in range(1,n+1):
        sums[i] = sums[i-1] + int(str[i-1])

    result = 0
    for size in range(2, n+1, 2):
        for i in range(0, n-size+1):
            if sums[i+int(size/2)] - sums[i] == sums[i+size] - sums[i+int(size/2)]:
                result = max(result, size)

    return result


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input()
        print(largest_sum_symmetry(str))