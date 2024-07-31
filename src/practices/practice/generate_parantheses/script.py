class Solution:

    def allParenthesis(self, string: str, n: int, open_count: int, close_count: int, result: list):
        if close_count == n:
            result.append(string)
            return result
        else:
            if open_count > close_count:
                result = self.allParenthesis(string + ")", n, open_count, close_count + 1, result)
            if open_count < n:
                result = self.allParenthesis(string + "(", n, open_count + 1, close_count, result)
            return result

    def AllParenthesis(self, n):
        result = self.allParenthesis("", n, 0, 0, [])
        return result


if __name__ == "__main__":
    t = int(input())
    for i in range(0, t):
        n = int(input())
        ob = Solution()
        result = ob
        result.sort()
        for i in range(0, len(result)):
            print(result[i])
