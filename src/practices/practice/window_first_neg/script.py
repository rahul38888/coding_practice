

def window_first_neg(n, a, k):
    i = 0
    neg_indices = []
    neg_values = []
    while i < n:
        if a[i] < 0:
            neg_indices.append(i)
            neg_values.append(a[i])
        i+=1
    result = ""
    i = 0
    j = k-1
    while j < n:
        if(len(neg_indices) > 0 and neg_indices[0] < i):
            neg_values.pop(0)
            neg_indices.pop(0)

        if len(neg_indices) > 0:
            if neg_indices[0] >= i and neg_indices[0] <= j:
                result += " "+str(neg_values[0])
            else:
                result  += " 0"
        else:
            result += " 0"

        i += 1
        j += 1

    return result[1:]


def scan_input():
    n = int(input())
    nsstr = input()
    a = list(map(lambda x: int(x), nsstr.split()))
    k = int(input())
    return n, a, k


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, a, k = scan_input()
        print(window_first_neg(n, a, k))