def least_to_palindrome(pal):
    stack = []
    for p in pal:
        if len(stack)>0:
            if stack[len(stack)-1] == p:
                stack.pop(len(stack)-1)
            else:
                stack.append(p)
        else:
            stack.append(p)

    return len(stack)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        string = input()
        print(least_to_palindrome(string))
