def longest_valid_parentheses(parans):
    stack = [-1]
    result = 0
    i = 0
    for paran in parans:
        if paran == "(":
            stack.append(i)
        else:
            if (len(stack)) > 0:
                stack.pop(len(stack) - 1)

            if len(stack) > 0:
                result = max(result, i - stack[len(stack) - 1])
            else:
                stack.append(i)
        i += 1

    return result


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        string = input()
        print(longest_valid_parentheses(string))
