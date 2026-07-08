# https://www.geeksforgeeks.org/problems/generate-all-possible-parentheses/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card
#
# Observations:
#   - A intermediate string with opening brackets more than n cannot become a valid result
#   - In a valid intermediate stage closing brackets should always be less than or equal to opening bracket
#   - If we are maintaining these 2 things, then when closing bracket count becomes n,
#       the result would be a valid result

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
        results = self.allParenthesis("", n, 0, 0, [])
        return results


if __name__ == "__main__":
    t = int(input())
    for i in range(0, t):
        n = int(input())
        ob = Solution()
        result = ob.AllParenthesis(n)
        result.sort()
        for i in range(0, len(result)):
            print(result[i])
