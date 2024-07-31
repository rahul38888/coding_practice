def power_of_five(value):
    temp = 5
    while temp != value and temp < value:
        temp *= 5

    if temp == value:
        return True
    else:
        return False


def cutting_binary(b):
    if b is "1":
        return 1
    part_val = 0
    count = 0
    for i in range(len(b)):
        bn = int(b[i])
        part_val = part_val*2 + bn
        if i + 1 < len(b) and b[i + 1] is '0':
            continue
        elif power_of_five(part_val):
            count += 1
            part_val = 0
        elif i is len(b)-1:
            count = 0
    if count is 0:
        return -1
    return count


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        b = input()
        print(cutting_binary(b))
